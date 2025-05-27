import aiohttp
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.keyboards import get_main_markup
from src.utils import get_logger

router = Router()
logger = get_logger().getChild(__name__)


@router.message(CommandStart())
async def start_handler(message: Message, _):
    logger.info(f"User: {message.from_user.id} - click /start😇")
    lang = message.from_user.language_code
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post("http://web_application:8000/auth/register",
                                    json={"telegram_id": message.from_user.id}) as response:
                logger.info(f"Response from server: {await response.json()}")
        except aiohttp.ClientError as e:
            logger.error(f"Error: {e}")
    await message.answer(_("Welcome! Choose an action:"), reply_markup=get_main_markup(_))
    logger.debug(f"User`s language is {lang}")
