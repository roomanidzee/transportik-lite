from datetime import timedelta

from transportik.settings.components import config

JWT_AUTH = {
    'JWT_VERIFY': config['jwt']['verify_token'],
    'JWT_VERIFY_EXPIRATION': config['jwt']['verify_expiration'],
    'JWT_EXPIRATION_DELTA': timedelta(seconds=config['jwt']['expiration_time']),
    'JWT_AUTH_HEADER_PREFIX': config['jwt']['header']
}
