from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from aiohttp.web import Application

from src.core.config import config


async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(
        f"{config.WEBHOOK_URL}{config.WEBHOOK_PATH}", secret_token=config.SECRET
    )


def setup_webhook(app: Application, dp: Dispatcher, bot: Bot) -> None:
    webhook_handler = SimpleRequestHandler(
        dispatcher=dp, bot=bot, secret_token=config.SECRET
    )
    webhook_handler.register(app, path=config.WEBHOOK_PATH)
