import asyncio
import json
import pathlib
from urllib import parse
from contextlib import asynccontextmanager

import aiohttp
import time

import biodome
import pytest
import zmq
from zmq.asyncio import Context, Socket

import sqlite_server.zmain as zmain
from sqlite_server.util import printl


@asynccontextmanager
async def server():
    print('Starting server task')
    t = asyncio.create_task(zmain.zmain())
    try:
        yield
    finally:
        print('Cancelling server task')
        t.cancel()
        await t


def test_query():
    responses = []
    dbname = '34feba8fb61144dfb5cb9d4ecdd08683'

    sql = 'SELECT * from frame_posting WHERE frame_id = 1'
    url = f'http://127.0.0.1:8080/{dbname}/{parse.quote_plus(sql)}'
    printl(url)

    payload = json.dumps(dict(dbname=dbname, query=sql))

    print(1)
    ctx = Context()
    print(2)
    s: Socket = ctx.socket(zmq.ROUTER)
    s.setsockopt(zmq.ROUTER_MANDATORY, 1)
    print(3)
    port = s.bind_to_random_port(addr='tcp://*')
    print(f'Bound to port: {port}')

    async def test():
        printl(time.perf_counter())
        msg = payload

        async def receiver():
            while True:
                try:
                    print(f'Waiting for reply...')
                    m = await asyncio.wait_for(s.recv_multipart(), .01)
                    break
                except asyncio.TimeoutError:
                    print('timed out waiting')
                    continue

            print('got message back')
            responses.append(m[1].decode())
            print(m)
            return

        async with server():
            t = asyncio.create_task(receiver())
            print(f'Sending string: {msg}')
            while True:
                try:
                    print('trying to send...')
                    await s.send_multipart([b'NO_IDENTITY', msg.encode()])
                    break
                except Exception as e:
                    print(e)
                    await asyncio.sleep(0.1)
                    continue

            await t

    with biodome.env_change('TARGET_SERVER_PORT', port), \
            biodome.env_change('TARGET_SERVER_URL', '127.0.0.1'):
        asyncio.run(test())

    s.close(1)
    ctx.destroy()

    printl(responses)
    print('leaving test!')
    assert responses[0] == (
        '[(1, 0, 194), (1, 1, 1101), (1, 2, 12), (1, 3, 23), (1, 4, 247), (1, 5, 2), '
        '(1, 6, 94), (1, 7, 196), (1, 8, 56), (1, 9, 9), (1, 10, 127), (1, 11, 13), '
        '(1, 12, 11), (1, 13, 4), (1, 14, 508), (1, 15, 181), (1, 16, 314), (1, 17, '
        '19), (1, 18, 144), (1, 19, 35), (1, 20, 128), (1, 21, 75), (1, 22, 15), (1, '
        '23, 1), (1, 24, 426), (1, 25, 2), (1, 26, 160), (1, 27, 102), (1, 28, 9), '
        '(1, 29, 245), (1, 30, 3817), (1, 31, 1), (1, 32, 276), (1, 33, 4), (1, 34, '
        '23), (1, 35, 98), (1, 36, 940), (1, 37, 2), (1, 38, 1), (1, 39, 57), (1, 40, '
        '4), (1, 41, 1734), (1, 42, 1344), (1, 43, 4), (1, 44, 18), (1, 45, 75), (1, '
        '46, 3), (1, 47, 17), (1, 48, 350), (1, 49, 177), (1, 50, 313), (1, 51, 1), '
        '(1, 52, 2117), (1, 53, 20), (1, 54, 4), (1, 55, 198), (1, 56, 890), (1, 57, '
        '3), (1, 58, 290), (1, 59, 4), (1, 60, 92), (1, 61, 2), (1, 62, 774), (1, 63, '
        '13), (1, 64, 36), (1, 65, 56), (1, 66, 80), (1, 67, 39), (1, 68, 92), (1, '
        '69, 521), (1, 70, 2), (1, 71, 6), (1, 72, 1276), (1, 73, 5099), (1, 74, '
        '389), (1, 75, 31), (1, 76, 199), (1, 77, 23), (1, 78, 30), (1, 79, 593), (1, '
        '80, 8), (1, 81, 5740)]'
    )
