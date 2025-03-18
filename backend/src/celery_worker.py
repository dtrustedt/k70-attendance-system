from src.app import create_app
from src.app.config import Config

app = create_app()
celery = app.celery
