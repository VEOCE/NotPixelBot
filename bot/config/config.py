from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    
    AUTO_UPGRADE_PAINT_REWARD: bool = False
    AUTO_UPGRADE_RECHARGE_SPEED: bool = False
    AUTO_UPGRADE_RECHARGE_ENERGY: bool = False
    AUTO_TASK: bool = True

    USE_NEW_PAINT_METHOD: bool = True
    USE_CUSTOM_TEMPLATE: bool = True
    CUSTOM_TEMPLATE_ID: int = 6624523270
    USE_RANDOM_TEMPLATES: bool = False
    RANDOM_TEMPLATES_ID: list[int] = [6493211155, 6989019093, 917981974, 7319890725, 799818229, 1972552043, 7114665280, 5323541038, 1964161795, 5522474073,
                                      6578955397, 737065053, 347622105, 446378180, 379402843, 6914611412, 1325258259, 175225616, 2107125948, 1811879982, 5465341011, 1678134459]

    NIGHT_MODE: bool = False
    SLEEP_TIME: list[int] = [0, 7]  # your time zone

    DELAY_EACH_ACCOUNT: list[int] = [10, 15]
    DELAY_START_BOT: list[int] = [1, 15]
    SLEEP_TIME_BETWEEN_EACH_ROUND: list[int] = [1000, 1500]

    ADVANCED_ANTI_DETECTION: bool = False

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()