from bs4 import BeautifulSoup
from loguru import logger
import requests

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

def main():
    for url in urls:
        fetch(url)

def fetch(url):
    logger.info(f"Fetch start: {url}")
    with requests.get(url) as resp:
        soup = BeautifulSoup(resp.text, 'html.parser')
    logger.info(f"Fetch end: {url} {soup.find('title')}")


if __name__ == "__main__":
    main()