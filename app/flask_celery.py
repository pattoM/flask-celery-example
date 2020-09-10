from celery import Celery
from datetime import timedelta 



def make_celery(app):
    #celery beat run once a day - play with schedule timedelta
    CELERYBEAT_SCHEDULE = {
    'email-video-links': {
        'task': 'site_async_tasks.send_video_links',
        'schedule': timedelta(seconds=86400)
        },
    }

    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
        include=['app.site.site_async_tasks']
    )
    #the include line above is important - defining path to tasks so that celery can discover them
    celery.conf.update(app.config)
    celery.conf.beat_schedule = CELERYBEAT_SCHEDULE 

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
