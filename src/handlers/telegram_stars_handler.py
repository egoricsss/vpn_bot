from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data.startswith("plan_"))
async def initiate_stars_payment(callback: CallbackQuery, _):
    await callback.answer("Payment accepted 18-05-2025::1937")
    # Вызов FastAPI для инициации платежа
    # async with httpx.AsyncClient() as client:
    #     response = await client.post("http://fastapi:8000/stars/initiate",
    #                                  json={"user_id": callback.from_user.id, "plan_id": plan_id})