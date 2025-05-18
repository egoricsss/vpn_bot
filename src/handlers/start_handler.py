from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from src.utils import get_logger

router = Router()
logger = get_logger().getChild(__name__)


@router.message(CommandStart())
async def start(message: Message):
    logger.info(f"Пользователь: {message.from_user.id} - нажал /start😇")
    await message.answer("Привет! Я бот для оплаты VPN.")
