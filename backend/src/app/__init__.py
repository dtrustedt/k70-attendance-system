from flask import Flask
from celery import Celery  # Changed import
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.ProductionConfig')

    # Initialize Celery properly
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['CELERY_RESULT_BACKEND']
    )
    celery.conf.update(app.config)
    
    # Store celery instance in app context
    app.celery = celery  # Optional but useful for access

    # Register blueprints
    from .routes.device_routes import device_bp
    from .routes.user_routes import user_bp
    from .routes.attendance_routes import attendance_bp

    app.register_blueprint(device_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(attendance_bp)

    # Import tasks after celery is initialized
    from . import tasks  # Important for task registration

    return app
