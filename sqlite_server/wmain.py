import asyncio
import pathlib
from urllib import parse

from aiohttp import web
from . import db
from . import zmain


async def query(request: web.Request) -> web.Response:
    print('got request:', request)
    dbname = request.match_info.get("dbname", "Anonymous")
    dbname = pathlib.Path(__file__).parent.parent / f'tests/{dbname}/storage.db'
    query = request.match_info.get("query", "Anonymous")
    query = parse.unquote_plus(query)
    print('dbname', dbname)
    print('query', query)
    result = await db.run_query(dbname, query)
    # print(result)
    return web.Response(text=str(result))
    # return web.Response(text='123')


async def handle(request: web.Request) -> web.Response:
    name = request.match_info.get("name", "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


async def wmain(app):
    # Taken from https://aiohttp.readthedocs.io/en/stable/web_advanced.html#application-runners
    app.add_routes(
        [
            web.get("/", handle),
            web.get("/{name}", handle),
            # Change query to a param
            web.get("/{dbname}/{query}", query),
        ]
    )
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()
    try:
        while True:
            await asyncio.sleep(10)
    except asyncio.CancelledError:
        print('server cancelled, running cleanup')
        await runner.cleanup()
        print('done')

if __name__ == '__main__':
    # We'll use aiohttp to also run the main event loop (it prefers to do
    # that).
    app = web.Application()
    # Start up the zmq long-lived task
    asyncio.create_task(zmain.zmain())
    asyncio.create_task(wmain(app))
