import logging
import asyncio
import json
from typing import Dict
import pathlib

import zmq
from zmq.asyncio import Context, Socket

from . import settings
from . import db


logger = logging.getLogger(__name__)


async def process_db_action(sock: Socket, raw_msg: bytes):
    msg: Dict = json.loads(raw_msg)
    dbname = msg['dbname']
    query = msg['query']
    dbname = pathlib.Path(__file__).parent.parent / f'tests/{dbname}/storage.db'
    print('dbname', dbname)
    print('query', query)
    result = await db.run_query(dbname, query)
    raw_result = result.encode()
    print(f'Query result: {raw_result}')
    await sock.send(raw_result)


async def process_messages(sock: Socket):
    while True:
        try:
            logger.debug('Waiting for query...')
            raw_msg = await sock.recv()
            logger.debug(f'Got message: {raw_msg}')
            asyncio.create_task(process_db_action(sock, raw_msg))
        except asyncio.CancelledError:
            raise
        except Exception:
            logger.exception('Unexpected error:')


async def zmain():
    logger.info(123)
    ctx = Context()
    logger.info(456)
    sock: Socket = ctx.socket(zmq.DEALER)
    logger.info(789)
    idd = settings.IDENTITY
    logger.info(idd)
    sock.identity = idd.encode()
    logger.info(345)
    connection_string = f'tcp://{settings.TARGET_SERVER_URL()}:{settings.TARGET_SERVER_PORT():d}'
    logger.info(f'Connecting to {connection_string}')
    sock.connect(connection_string)
    try:
        await process_messages(sock)
    except asyncio.CancelledError:
        pass
    finally:
        sock.close(1)
        ctx.destroy()
