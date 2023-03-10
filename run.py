from aiogram import executor
from config import dp, logger
from handlers import client


async def on_startup(_):
    logger.info("Bot is online")


if __name__ == '__main__':
    client.register_handlers_client(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
