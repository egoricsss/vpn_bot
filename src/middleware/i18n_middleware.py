from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from typing import Callable, Awaitable, Any
from src.utils import get_translator


class I18nMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: dict[str, Any]
    ) -> Any:
        user: User = data.get("event_from_user")
        if user:
            lang = user.language_code
            data["_"] = get_translator(lang)
        return await handler(event, data)
