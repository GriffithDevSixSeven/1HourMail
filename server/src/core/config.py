from pydantic_settings import BaseSettings,SettingsConfigDict
from pathlib import Path

ENV_FILE = Path(__file__).resolve().parent.parent.parent/".env"

class RedisSettings(BaseSettings):
    REDIS_URL : str
    
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8"
    )

redis_setting = RedisSettings()


    