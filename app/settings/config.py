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
    'host': 'staging-auth.czakxqyqrlce.us-east-1.rds.amazonaws.com',
    'port': '5432',
}


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    # CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
    # ALLOWED_EMAIL_DOMAINS = "azent.com"
    NAME = "development" #change it to APP_ENV
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    POSTGRES["host"] = "localhost"
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Welcome@123@localhost:5432/backendservice'


class DockerConfig(DevelopmentConfig):
    NAME = "docker"
    # CELERY_BROKER_URL = 'redis://redis:6379/0'
    # MONGO_DB_URL = f'mongodb+srv://admin:{mongo_db_password}@staging-main.tosjl.mongodb.net/base-python-dev?retryWrites=true&w=majority'
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    NAME = "testing"
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    # MONGO_DB_URL ="mongodb://localhost/base-python-repo-test"



class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True
    NAME = "staging"
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    # MONGO_DB_URL = f'mongodb+srv://admin:{mongo_db_password}@staging-main.tosjl.mongodb.net/base-python-staging?retryWrites=true&w=majority'


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False
    # ALLOWED_EMAIL_DOMAINS = "*"
    # CELERY_BROKER_URL = 'redis://production-redis.a9qdyp.ng.0001.aps1.cache.amazonaws.com:6379/0'
    NAME = "production"
    POSTGRES["host"] = "platform-production-db.cafeuaekamgm.ap-south-1.rds.amazonaws.com"
    POSTGRES["db"] = "auth_service"
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    # MONGO_DB_URL = f'mongodb+srv://admin:{mongo_db_password}@staging-main.tosjl.mongodb.net/base-python-prod?retryWrites=true&w=majority'



app_config = {
    'development': DevelopmentConfig,
    'docker': DockerConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
