from pathlib import Path

from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    db_user: SecretStr
    db_password: SecretStr
    db_host: SecretStr
    db_port: SecretStr
    db_ams: str
    db_mcs: str
    auth_url: str
    lras_url: str
    dps_url: str
    lcs_url: str
    elma: dict
    datalake: dict

    @property
    def auth_body(self) -> dict:
        return {
            'elma': self.elma,
            'datalake': self.datalake
        }

    @property
    def database_url(self) -> dict:
        base_url = f'postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/'
        urls = {
            'ams': base_url + self.db_ams,
            'mcs': base_url + self.db_mcs
        }
        return urls

    class Config:
        env_file = (
            BASE_DIR / '.env.template',
            BASE_DIR / '.env',
        )
        env_file_encoding = 'utf-8'
        extra = 'ignore'


settings = Settings()
