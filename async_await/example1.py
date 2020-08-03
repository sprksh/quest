import signal
import sys
import asyncio
import aiohttp
import json
import requests
from asgiref.sync import sync_to_async
# loop = asyncio.get_event_loop()
# client = aiohttp.ClientSession()
client = ''

# get_json_async = sync_to_async(get_json_sync, thread_sensitive=True)

@sync_to_async
def get_json_sync(c, url):
    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url)
    print(response.status_code)
    print("Got response for %s\n" % url)
    return response.json()

get_json_async = sync_to_async(get_json_sync)

async def get_json(client, url):
    print("Getting response for %s\n" % url)
    async with aiohttp.ClientSession() as s, s.get(url) as response:
        assert response.status == 200
        print("Got response for %s\n" % url)
        return await response.read()

async def get_reddit_top(subreddit, client):
    data = await get_json_sync(client, 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5')
    # if not client == '':
    #     j = json.loads(data.decode('utf-8'))
    # else:
    # j = json.loads(data.decode('utf-8'))
    j = data
    print(data)
    print('DONE:', subreddit + '\n')

# def signal_handler(signal, frame):
#     loop.stop()
#     # client.close()
#     sys.exit(0)

# signal.signal(signal.SIGINT, signal_handler)

async def runner():
    await asyncio.gather(
        get_reddit_top('python', client), 
        get_reddit_top('programming', client),
        get_reddit_top('compsci', client))
    print("ran all tasks\n")
    return

if __name__ == '__main__':
    asyncio.run(runner())
