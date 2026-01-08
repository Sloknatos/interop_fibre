from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_host: str
    database_user: str
    database_password: str
    database_db: str
    database_port: int
    sqlite_path: str
    openapi_url: str = "/openapi.json"

    model_config = SettingsConfigDict()


settings = Settings(_env_file=".env")
