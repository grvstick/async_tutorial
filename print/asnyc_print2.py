import asyncio
from loguru import logger

async def main():
    await asyncio.gather(task1(), task2())

async def task1():
    for n in range(5):
        logger.info(n)
        await asyncio.sleep(0)

async def task2():
    for n in range(5):
        logger.info(n)
        await asyncio.sleep(0)

asyncio.run(main())