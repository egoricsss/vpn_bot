from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from src.utils import get_logger

router = Router()
logger = get_logger().getChild(__name__)


@router.message(Command("help"))
async def help_handler(message: Message, _):
    logger.info(f"User: {message.from_user.id} click - /help")
    await message.answer(_("Use /start to begin interaction with the bot."))
