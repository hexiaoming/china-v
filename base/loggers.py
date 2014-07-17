LOGGING = {
    'version': 1,
    'dusable_existing_loggers': True,
    'formatters': {
        'normal': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(message)s'
            }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'django': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'interval': 1,
            'backupCount': 5,
            'filename': 'logs/django.log',
            'formatter': 'normal'
        },
        'base': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'interval': 1,
            'backupCount': 5,
            'filename': 'logs/base.log',
            'formatter': 'normal'
        },
        'analysis': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'interval': 1,
            'backupCount': 5,
            'filename': 'logs/analysis.log',
            'formatter': 'normal'
        },
        'promotion': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'interval': 1,
            'backupCount': 5,
            'filename': 'logs/mobile.log',
            'formatter': 'normal'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['django'],
            'propagate': False,
            'level': 'DEBUG'
        },
        'analysis': {
            'handlers': ['analysis', 'console'],
            'propagate': False,
            'level': 'DEBUG'
        },
        '': {
            'handlers': ['base'],
            'level': 'DEBUG'
        }
    }
}

