import os

from pydantic import BaseModel


class BotConfig(BaseModel):
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    WEBHOOK_URL: str = os.getenv("WEBHOOK_URL")
    SECRET: str = os.getenv("SECRET")
    WEBHOOK_PATH: str = os.getenv("WEBHOOK_PATH")
    CLEAR_LOGS: bool = os.getenv("CLEAR_LOGS")


config = BotConfig()
