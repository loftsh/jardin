# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'DJANGO SECRET'


# Logging settings
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
        },
        'telegram_main_chan': {
            'class': 'telegram_handler.TelegramHandler',
            'level': 'ERROR',
            'token': 'TELEGRAM TOKEN',
            'chat_id': 'TELEGRAM CHAN ID'
        },
        'telegram_debug_chan': {
            'class': 'telegram_handler.TelegramHandler',
            'level': 'DEBUG',
            'token': 'TELEGRAM TOKEN',
            'chat_id': 'TELEGRAM CHAN ID'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
        'loft': {
            'handlers': ['console', 'telegram_main_chan', 'telegram_debug_chan'],
            'level': 'DEBUG'
        }
    }
}
