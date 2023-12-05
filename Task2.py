import aiohttp
import asyncio
import json


async def download_comments(subreddit):
    url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}"

    headers = {
        'User-Agent': 'YourUserAgentHere',  
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Failed to download comments for subreddit {subreddit}. Status code: {response.status}")
                return None


async def main():
    subreddit_name = "python"

    comments = await download_comments(subreddit_name)

    if comments:

        output_file = f"{subreddit_name}_comments.json"
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(comments['data'], json_file, ensure_ascii=False, indent=2)
        print(f"Downloaded {len(comments['data'])} comments. Stored in {output_file}")
    else:
        print("Failed to download comments.")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
