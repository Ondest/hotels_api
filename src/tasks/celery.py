from celery import Celery


celery = Celery("tasks", broker="redis://localhost:5000/0", include=["src.tasks.tasks"])
# celery.conf.broker_url = "redis://localhost:6379/0"
