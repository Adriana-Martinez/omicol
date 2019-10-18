from os import environ


class Config(object):
    SECRET_KEY = 'key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # THEME SUPPORT
    #  if set then url_for('static', filename='', theme='')
    #  will add the theme name to the static URL:
    #    /static/<DEFAULT_THEME>/filename
    # DEFAULT_THEME = "themes/dark"
    DEFAULT_THEME = None


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        environ.get('OMI_DATABASE_USER', 'postgres'),
        environ.get('OMI_DATABASE_PASSWORD', 'postgres'),
        environ.get('OMI_DATABASE_HOST', 'localhost'),
        environ.get('OMI_DATABASE_PORT', 5432),
        environ.get('OMI_DATABASE_NAME', 'oomi')
    )


class DebugConfig(Config):
    DEBUG = True


config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}