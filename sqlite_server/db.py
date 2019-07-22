import asyncio
from weakref import WeakValueDictionary

import aiosqlite


async def dbtask(dbname: str, q: asyncio.Queue):
    # db = await aiosqlite.connect(...)
    # cursor = await db.execute('SELECT * FROM some_table')
    # row = await cursor.fetchone()
    # rows = await cursor.fetchall()
    # await cursor.close()
    # await db.close()
    async with aiosqlite.connect(dbname) as db:
        while True:  # Change to a delay-based expiry
            query, f = await q.get()
            result = []
            async with db.execute(query) as cursor:
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
        dbtasks[dbname] = t

    f = asyncio.Future()
    t.q.put_nowait((query, f))
    result = await f
    return str(result)
