from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from src.utils import get_logger, _, set_language

router = Router()
logger = get_logger().getChild(__name__)


@router.message(CommandStart())
async def start(message: Message):
    logger.info(f"User: {message.from_user.id} - click /start😇")
    lang = message.from_user.language_code
    await message.answer(_("Hello! I am your VPN bot"))
    logger.info(f"User`s language is {lang}")
