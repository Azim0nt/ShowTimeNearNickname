import time
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import pytz

api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"
username = "YOU_NICKNAME"  # Замените на свое имя пользователя

client = TelegramClient("carpediem", api_id, api_hash)
client.start()

def convert_time_to_string(dt):
    return f"{dt.hour}:{dt.minute:02}"

async def main():
    while True:
        current_time = convert_time_to_string(datetime.now().astimezone(pytz.timezone('Asia/Tashkent')))
        new_first_name = f"{username} | {current_time}"
        await client(UpdateProfileRequest(first_name=new_first_name))
        description = f"Сейчас время: {current_time}"
        await client(UpdateProfileRequest(about=description))
        time.sleep(60)

if __name__ == '__main__':
    import asyncio
    asyncio.get_event_loop().run_until_complete(main())
    