import asyncio

from CONFIG.CONFIG import *
from src.handlers import shop

shop.activate.activate(dp)

async def start():

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logger.info('The bot has successfully running!')
    asyncio.run(start())