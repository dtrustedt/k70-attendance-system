# Change imports to use absolute paths
from app import create_app  # Instead of relative import
from app.tasks import celery  # If you have tasks defined

app = create_app()
