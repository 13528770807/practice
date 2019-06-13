import time
from celery import Celery


celery = Celery('q01_celery', broker='redis://localhost:6379/0')


@celery.task
def hello():
    time.sleep(2)
    return "hello world !!!"


if __name__ == "__main__":
    print(dir(celery.start()))
    celery.star()


# celery -A q01_celery worker --loglevel=info
