from pydantic_settings import BaseSettings, SettingsConfigDict

class TelegramSettings(BaseSettings):
    bot_token: str
    chat_id: int

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    

class Settings(BaseSettings):
    admin_email: str
    
    model_config = SettingsConfigDict(
        env_file=".env"
    )


# settings = Settings()
