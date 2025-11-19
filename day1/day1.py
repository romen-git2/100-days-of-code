import asyncio
import aiohttp
import time

# single async fetch function
async def fetch_url(session, url):
    print(f"Starting fetch {url}")
    try:
        async with session.get(url) as response:
            text = await response.text()
            print(f"Fetched: {url} (Status: {response.status})")
            return f"URL: {url} | Length: {len(text)}"
    except Exception as e:
        return f"Error fetching {url}: {str(e)}"


async def main():
    urls = [
        "https://python.org",
        "https://google.com",
        "https://github.com"
    ]

    # single session for efficiency
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            # creating task for each url
            task = fetch_url(session, url)
            tasks.append(task)
        print("Starting concurrent fetch")
        startTime = time.time()
        # asyncio.gather() runs all tasks concurrently
        results = await asyncio.gather(*tasks)
        endTime = time.time()
        print(f"All done in {endTime-startTime:2f} seconds")
        for result in results:
            print(result)

if __name__ == "__main__":
    asyncio.run(main())
