from pathlib import Path

HOME = Path().home()
KEY_DIR = HOME.joinpath('keys')
DATA_DIR = HOME.joinpath('data')
_LOG_DIR = HOME.joinpath('logs')


def get_local_secret(fpath: Path) -> str:
    """Grabs a locally-stored secret for debugging"""
    with fpath.open('r') as f:
        return f.read().strip()


class Config(object):
    """
    Default config
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'sqlite://{DATA_DIR.joinpath("abulmisk.sqlite")}'
    SECRET_KEY = get_local_secret(KEY_DIR.joinpath('ABUL_SECRET_KEY'))
    REGISTER_KEY = get_local_secret(KEY_DIR.joinpath('REGISTRATION_KEY'))
    STATIC_DIR_PATH = '../static'
    TEMPLATE_DIR_PATH = '../templates'


class BaseConfig(Config):
    """
    Base config class
    """
    DEBUG = True
    TESTING = False


class ProductionConfig(BaseConfig):
    """
    Production-specific config
    """
    DEBUG = False
    LOG_DIR = _LOG_DIR.joinpath('abulmisk_prod')
    LOG_DIR.mkdir(parents=True, exist_ok=True)


class DevelopmentConfig(BaseConfig):
    """
    Development-specific config
    """
    DEBUG = True
    TESTING = True
    TEMPLATES_AUTO_RELOAD = True
    LOG_DIR = _LOG_DIR.joinpath('abulmisk_dev')
    LOG_DIR.mkdir(parents=True, exist_ok=True)
