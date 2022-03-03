import os
import logging

logger = logging.getLogger('backend')

POSTGRES_DB_PASSWORD = None
try:
    POSTGRES_DB_PASSWORD = os.environ["postgres_db_password"]
except: 
    logger.warning("No postgres password set in the os enviroment")

POSTGRES = {
    'user': 'postgres',
    'pw': POSTGRES_DB_PASSWORD,
    'db': 'backendservice',
    'host': 'localhost',
    'port': '5432',
}


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    NAME = "development" #change it to APP_ENV
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    POSTGRES["host"] = "localhost"
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


class DockerConfig(DevelopmentConfig):
    NAME = "docker"
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    NAME = "testing"
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True
    NAME = "staging"
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False
    NAME = "production"
    POSTGRES["host"] = "polyglot.cxisjiaafl0q.eu-west-2.rds.amazonaws.com"
    POSTGRES["db"] = "backend_service"
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


app_config = {
    'development': DevelopmentConfig,
    'docker': DockerConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
