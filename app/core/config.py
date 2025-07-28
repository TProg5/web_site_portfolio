from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

class TelegramSettings(BaseSettings):
    BOT_TOKEN: str
    CHAT_ID: int

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    

class Settings(BaseSettings):
    ADMIN_EMAIL: str
    DEFAULT_LOCALE: str
    SUPPORTED_LOCALE: List[str]
    
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

#Singletones
settings = Settings()
telegram_settings = TelegramSettings()