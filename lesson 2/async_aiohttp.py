import asyncio

from aiohttp import ClientSession
from bs4 import BeautifulSoup
from loguru import logger

urls = [ 
    "https://www.naver.com",
    "https://www.google.com",
    "https://www.daum.net",
    "https://python.org",
    "https://pypi.org",
    "https://talkpython.fm",
    "https://training.talkpython.fm",
    "https://fastapi.tiangolo.com/",
    "https://svelte.dev",
    "https://kit.svelte.dev",
    "https://pydantic-docs.helpmanual.io/",
]

async def main():
    async with ClientSession() as session:
        tasks = [asyncio.create_task(fetch(session, url)) for url in urls]
        await asyncio.gather(*tasks)


async def fetch(session: ClientSession, url):
    logger.info(f"Fetch start: {url}")
    async with session.get(url) as resp:
        soup = BeautifulSoup(await resp.text(), 'html.parser')
    logger.info(f"Fetch end: {url} {soup.find('title')}")


if __name__ == "__main__":
    asyncio.run(main())