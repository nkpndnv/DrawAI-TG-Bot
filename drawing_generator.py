import aiohttp
import config

async def generate_drawing(text):
    async with aiohttp.ClientSession() as session:
        async with session.post(config.DRAWING_API_URL, json={'text': text}) as response:
            if response.status == 200:
                data = await response.json()
                return data.get('image.url')
            else:
                return None