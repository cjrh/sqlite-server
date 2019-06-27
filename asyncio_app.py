import asyncio


async def main():
    await asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    tasks = asyncio.Task.all_tasks()
    group = asyncio.gather(*tasks)
    group.cancel()
    try:
        loop.run_until_complete(group)
    except asyncio.CancelledError:
        pass
    loop.close()