from app import create_app
from celery import Celery

app = create_app()
celery = app.celery

@celery.task
def your_async_task():
    # Your task logic - MUST BE INDENTED
    print("Task executed")  # Example implementation
    # Add your actual task code here
