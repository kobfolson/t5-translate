from pydantic import BaseSettings


class AppConfig(BaseSettings):
    URL_PREFIX: str = "/api/v1"
    MODEL_DATA: str = "/opt/model-data"
    RELEASE_ID: str = "1.0.0"


settings = AppConfig()
