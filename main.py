from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.webhook.aiohttp_server import setup_application
from aiohttp import web

from src.core.config import config
from src.handlers import start_router
from src.utils import get_logger, on_startup, setup_webhook

logger = get_logger().getChild(__name__)


def main() -> None:
    logger.info("Начало конфигурации бота🤑")
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.startup.register(on_startup)
    bot = Bot(
        token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    app = web.Application()
    setup_webhook(app, dp, bot)
    setup_application(app, dp, bot=bot)
    web.run_app(app, host="0.0.0.0", port=8080)
    logger.info("Бот запущен😋")


if __name__ == "__main__":
    main()
