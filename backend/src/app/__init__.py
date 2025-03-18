from flask import Flask
from flask_celery import make_celery
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.ProductionConfig')
    
    # Initialize Celery
    app.config.update(
        CELERY_BROKER_URL=app.config['CELERY_BROKER_URL'],
        CELERY_RESULT_BACKEND=app.config['CELERY_RESULT_BACKEND']
    )
    make_celery(app)
    
    # Register blueprints
    from .routes.device_routes import device_bp
    from .routes.user_routes import user_bp
    from .routes.attendance_routes import attendance_bp
    
    app.register_blueprint(device_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(attendance_bp)
    
    return app
