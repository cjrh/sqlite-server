import asyncio
import aiohttp
from aiohttp import web

import sqlite_server.wmain as wmain


def test_blah():
    app = web.Application()
    t = asyncio.create_task(wmain.wmain(app))

    responses = []

    async def test():
        async with aiohttp.ClientSession() as session:
            async with session.get('http://localhost:8080/caleb') as resp:
                print(resp.status)
                r = await resp.text()
                responses.append(r)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
    print(responses)
    t.cancel()
    loop.run_until_complete(t)
