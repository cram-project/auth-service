from os import getenv


class Settings:
    DB_HOST: str = getenv("DB_HOST")
    DB_PORT: int = getenv("DB_PORT")
    DB_NAME: str = getenv("DB_NAME")
    DB_USER: str = getenv("DB_USER")
    DB_PASSWORD: str = getenv("DB_PASSWORD")

    SECRET_KEY: str = getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_EXPIRE_MIN: int = 15
    REFRESH_EXPIRE_DAYS: int = 30

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()
