import logging
import httpx

from app.core.response import APIResponse
from app.core.config import TelegramSettings, telegram_settings

logger = logging.getLogger(__name__)


async def send_telegram_message(
    message: str,
    settings: TelegramSettings = telegram_settings
):  
    """Utility that allows you to send a message to Telegram Bot"""

    url: str = f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": settings.CHAT_ID,
        "text": message,
        "parse_mode": "HTML",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, data=params)
            response_data = response.json()
        except Exception as e:
            logger.exception("Telegram request failed")
            return {"status": False, "message": f"Exception: {str(e)}"}
        
    if response.status_code in (200, 201):
        return APIResponse(
            status=True,
            message="Telegram's API send message"
        ).model_dump()
    

    return APIResponse(
        status=False,
        message=f"Telegram error: {response_data.get('description')}"
    ).model_dump()
