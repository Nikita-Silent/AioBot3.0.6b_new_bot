from pydantic import BaseSettings, SecretStr, PostgresDsn, RedisDsn, validator


class Settings(BaseSettings):
    # Желательно вместо str использовать SecretStr
    # для конфиденциальных данных, например, токена бота
    bot_token: SecretStr
    main_chat_id: int
    second_chat_id: int
    redis_dsn: str
    db_name: str
    db_user: str
    db_host: str
    db_port: int
    db_password: str

    @validator("bot_fsm_storage")
    def validate_bot_fsm_storage(cls, v):
        if v not in ("memory", "redis"):
            raise ValueError("Incorrect 'bot_fsm_storage' value. Must be one of: memory, redis")
        return v

    @validator("redis_dsn")
    def validate_redis_dsn(cls, v, values):
        if values["bot_fsm_storage"] == "redis" and not v:
            raise ValueError("Redis DSN string is missing!")
        return v

    @validator("webhook_path")
    def validate_webhook_path(cls, v, values):
        if values["webhook_domain"] and not v:
            raise ValueError("Webhook path is missing!")
        return v

    # Вложенный класс с дополнительными указаниями для настроек
    class Config:
        # Имя файла, откуда будут прочитаны данные
        # (относительно текущей рабочей директории)
        env_file = '.env'
        # Кодировка читаемого файла
        env_file_encoding = 'utf-8'


# При импорте файла сразу создастся
# и провалидируется объект конфига,
# который можно далее импортировать из разных мест
config = Settings()
