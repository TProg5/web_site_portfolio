import logging
import httpx

from app.core.config import TelegramSettings

logger = logging.getLogger(__name__)


async def send_telegram_message(
    message: str,
    settings: TelegramSettings = TelegramSettings()
):
    url: str = f"https://api.telegram.org/bot{settings.bot_token}/sendMessage"

    params = {
        "chat_id": settings.chat_id,
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
        return {"status": True, "message": "Telegram's API send message"}
    
    return {
        "status": False,
        "message": f"Telegram error: {response_data.get('description')}",
    }