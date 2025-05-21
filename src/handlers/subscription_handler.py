from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from src.utils import get_logger

router = Router()
logger = get_logger().getChild(__name__)

@router.message(Command("subscription"))
async def show_subscription(message: Message, _):
    # Проверка подписки через FastAPI
    # Отправка информации о подписке
    logger.info(f"User: {message.from_user.id} click /subscription")
    await message.answer(_("Your subscription is active until 2025-12-31."))


@router.callback_query(F.data == "subscription")
async def subscription_info(callback: CallbackQuery, _):
    await callback.message.edit_text(_("Subscription details..."))