import asyncio
from weakref import WeakValueDictionary

import aiosqlite
from aiohttp import web


async def dbtask(dbname: str, q: asyncio.Queue):
    async with aiosqlite.connect(dbname) as db:
        while True:  # Change to a delay-based expiry
            query, f = await q.get()
            result = []
            async with db.execute("SELECT * FROM some_table") as cursor:
                async for row in cursor:
                    result.append(row)
            await db.commit()
            f.set_result(result)


dbtasks = WeakValueDictionary()


async def run_query(dbname, query: str) -> str:  # JSON data
    t: asyncio.Task = dbtasks.get(dbname)
    if not t:
        q = asyncio.Queue()
        t = asyncio.create_task(dbtask(dbname, q))
        t.q = q

    f = asyncio.Future()
    await q.put((query, f))
    result = await f
    return str(result)


async def query(request):
    dbname = request.match_info.get("dbname", "Anonymous")
    query = request.match_info.get("query", "Anonymous")
    result = await run_query(dbname, query)
    return web.Response(text=result)


async def handle(request):
    name = request.match_info.get("name", "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


app = web.Application()
app.add_routes(
    [
        web.get("/", handle),
        web.get("/{name}", handle),
        web.get("/{dbname}/{query}", query),
    ]
)

web.run_app(app)
