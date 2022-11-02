from pydantic import BaseSettings


class EnvSettings(BaseSettings):
    token: str
    owner_id: int

    class Config:
        env_file: str = '.env'


cfg = EnvSettings()
