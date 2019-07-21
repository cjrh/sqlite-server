import asyncio
from aiohttp import web
from . import db
from . import zmain


async def query(request: web.Request) -> web.Response:
    dbname = request.match_info.get("dbname", "Anonymous")
    query = request.match_info.get("query", "Anonymous")
    result = await db.run_query(dbname, query)
    return web.Response(text=result)


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
        await runner.cleanup()

if __name__ == '__main__':
    # We'll use aiohttp to also run the main event loop (it prefers to do
    # that).
    app = web.Application()
    # Start up the zmq long-lived task
    asyncio.create_task(zmain.zmain())
    asyncio.create_task(wmain(app))
