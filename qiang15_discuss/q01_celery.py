import time
from celery import Celery


app = Celery('q01_celery', broker='redis://localhost:6379/15')


@app.task
def hello():
    time.sleep(2)
    return "hello world !!!"


# if __name__ == "__main__":
#     print(dir(app.start()))
#     app.star()


# celery -A q01_celery worker --loglevel=info
