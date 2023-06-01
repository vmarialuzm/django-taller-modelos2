#usamos as para poner un alias
from .celery import app as celery_app

__all__ = ('celery_app',)

