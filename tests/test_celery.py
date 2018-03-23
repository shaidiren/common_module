# coding: utf-8


from celery_project.tasks import sendmail, add

if __name__ == '__main__':
    # r = sendmail.delay(dict(to='daixiaoyun@hundun.cn'))
    # print r.status
    # print r.get(timeout=3)

    r = add.delay(3, 4)
    print r.status
    print r.get()
