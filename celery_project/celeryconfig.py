# coding: utf-8

BROKER_URL = 'amqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'redis://localhost'

CELERY_TASK_SERIALIZER = 'msgpack'  # 任务序列化和发序列化
CELERY_RESULT_SERIALIZER = 'json'  # 读取任务结果使用json格式
CELERY_TASK_RESULT_EXPIRES = 60 * 60  # 任务过期时间
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = False
# CELERY_IGNORE_RESULT = True     # 丢弃结果
CELERYD_SEND_EVENTS = True
CELERY_TASK_SEND_SENT_EVENT = True
CELERYD_CONCURRENCY = 4             # 启动的worker数量

# 定时任务
from datetime import timedelta
from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    # Executes every 30 seconds.
    'add-every-30-seconds': {
        'task': 'celery_project.tasks.log_test',
        'schedule': timedelta(seconds=60),
        'args': ()
    },
    # Executes every Monday morning at 7:30 A.M
    # 'add-every-monday-morning': {
    #     'task': 'tasks.add',
    #     'schedule': crontab(hour=7, minute=30, day_of_week=1),
    #     'args': (16, 16),
    # },
}
