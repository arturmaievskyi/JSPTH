from celery import Celery

# Initialize Celery
celery_app = Celery("email_tasks", broker="redis://localhost:6379/0")

# Celery configuration
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_backend="redis://localhost:6379/0",
    timezone="UTC",
)
