from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings, case_sensitive=False):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    db_host: str
    db_port: str
    db_name: str
    db_password: str
    db_username: str
    jwt_secret: str
    jwt_algo: str
    jwt_expire_minutes: int

settings = Settings()