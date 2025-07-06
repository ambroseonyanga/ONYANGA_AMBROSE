from telegram import Bot
import asyncio

BOT_TOKEN = "8101571943:AAE0uR8ZR6-GsKNSOQPlOGg81rR-aTvnO6k"

async def get_updates():
    bot = Bot(token=BOT_TOKEN)
    updates = await bot.get_updates()
    for update in updates:
        print(update)

asyncio.run(get_updates())
