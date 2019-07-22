import asyncio
import pathlib
from urllib import parse

import aiohttp
from aiohttp import web
import time
import pytest

import sqlite_server.wmain as wmain
from sqlite_server.util import printl


@pytest.fixture(scope='module')
def server():
    loop = asyncio.get_event_loop()
    app = web.Application()
    t = loop.create_task(wmain.wmain(app))
    print('running server')
    try:
        printl('yielding to tests...')
        yield app, loop
        printl('back from tests...')
    finally:
        printl('cancelling server task...')
        t.cancel()
        printl('waiting for server to close...')
        loop.run_until_complete(t)
        printl('server closed')


def test_blah(server):
    app, loop = server
    responses = []

    async def test():
        printl(time.perf_counter())
        async with aiohttp.ClientSession() as session:
            async with session.get('http://127.0.0.1:8080/caleb') as resp:
                printl(resp.status)
                r = await resp.text()
                responses.append(r)

    loop.run_until_complete(test())
    printl(responses)


def test_query(server):
    app, loop = server
    responses = []
    dbname = '34feba8fb61144dfb5cb9d4ecdd08683'

    sql = 'SELECT * from frame_posting WHERE frame_id = 1'
    url = f'http://127.0.0.1:8080/{dbname}/{parse.quote_plus(sql)}'
    printl(url)

    async def test():
        printl(time.perf_counter())
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                printl(resp.status)
                r = await resp.text()
                responses.append(r)

    loop.run_until_complete(test())
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
