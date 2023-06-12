from pydantic import BaseSettings, SecretStr


class TrackerSettings(BaseSettings):
    secret_key: SecretStr
    db_url: SecretStr
    migrate_db: bool = False
    flask_app: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
