from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Any


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="env/.env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        env_ignore_empty=True,
        extra="ignore",
    )

    @staticmethod
    def parse_to_list(v: Any) -> list[str]:
        return list(map(str, v.split(",")))


class BotConfig(BaseConfig):
    BOT_TOKEN: str = None


dp = Dispatcher()


@dp.message(CommandStart())
async def start(message):
    await message.answer("Привет! Я бот для оплаты VPN.")


if __name__ == "__main__":
    import asyncio

    bot = Bot(
        token=BotConfig().BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    asyncio.run(dp.start_polling(bot))
