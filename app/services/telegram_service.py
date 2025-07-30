import logging
import aiohttp

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

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=params) as response:
                response_data = await response.json()

                if response.status == 200:
                    return APIResponse(
                        success=True,
                        message="Telegram's API sent the message"
                    ).model_dump()

                logger.error(f"Telegram error response: {response_data}")
                return APIResponse(
                    success=False,
                    message=f"Telegram error: {response_data.get('description')}"
                ).model_dump()

    except Exception as e:
        logger.exception("Telegram request failed")
        return APIResponse(
            success=False,
            message=f"Exception: {str(e)}"
        ).model_dump()
