from aiohttp import web
from . import db


async def query(request: web.Request) -> web.Response:
    dbname = request.match_info.get("dbname", "Anonymous")
    query = request.match_info.get("query", "Anonymous")
    result = await db.run_query(dbname, query)
    return web.Response(text=result)


async def handle(request: web.Request) -> web.Response:
    name = request.match_info.get("name", "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(
        [
            web.get("/", handle),
            web.get("/{name}", handle),
            # Change query to a param
            web.get("/{dbname}/{query}", query),
        ]
    )

    web.run_app(app)
