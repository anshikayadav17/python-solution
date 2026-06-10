import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            print(await r.text())

asyncio.run(
    fetch("https://example.com")
)
