# holds different app configuration settings
import os


class Config:
    """
    Parent configuration class
    """
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')


class DevelopmentConfig(Config):
    """
    Development configuration
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Configurations for production
    """
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """
    Configurations for Testing
    """
    TESTING = True
    DEBUG = True


config_environment = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

