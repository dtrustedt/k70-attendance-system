import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://redis:6379/0')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://redis:6379/0')
    DEVICE_TIMEOUT = int(os.environ.get('DEVICE_TIMEOUT', 30))
    MAX_CONNECTIONS = int(os.environ.get('MAX_CONNECTIONS', 10))

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
