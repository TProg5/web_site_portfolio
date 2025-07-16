from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # admin_email: str
    # bot_token: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )

settings = Settings()


print(settings) 