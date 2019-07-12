import logging
import asyncio
import json
from typing import Dict

import zmq
from zmq.asyncio import Context, Socket

from . import settings
from . import db


logger = logging.getLogger(__name__)


async def process_db_action(sock: Socket, id_: bytes, raw_msg: bytes):
    msg: Dict = json.loads(raw_msg)
    dbname = msg['dbname']
    query = msg['query']
    result = await db.run_query(dbname, query)
    raw_result = json.dumps(dict(result=result)).encode()
    await sock.send_multipart([id_, raw_result])


async def process_messages(sock: Socket):
    # After making connection, send our identity
    await sock.send_json(dict(
        identity=settings.IDENTITY
    ))
    while True:
        try:
            id_, raw_msg = await sock.recv_multipart()
            asyncio.create_task(process_db_action(sock, id_, raw_msg))
        except asyncio.CancelledError:
            raise
        except Exception:
            logger.exception('Unexpected error:')


async def zmain():
    ctx = Context()
    sock: Socket = ctx.socket(zmq.DEALER)
    sock.identity = settings.IDENTITY
    sock.connect(f'tcp://{settings.TARGET_SERVER_URL}:{settings.TARGET_SERVER_PORT:d}')
    try:
        await process_messages(sock)
    except asyncio.CancelledError:
        pass
    finally:
        sock.close(1)
        ctx.destroy()
