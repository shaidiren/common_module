# coding: utf-8


DEBUG = True

if DEBUG:
    # test config
    settings = {
        'DATABASES': {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'test.db'
            },
            'auth': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'auth.db'
            }
        },
        'INSTALLED_APPS': [],
        'DATABASE_ROUTERS': ['orm.router.AuthRouter']
    }

else:
    # online config
    settings = {
        'DATABASES': {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'test.db'
            }
        },
        'INSTALLED_APPS': [],
        'DATABASE_ROUTERS': ['orm.router.AuthRouter']
    }
