# update/override all values for production environment
from django.conf import settings

if not settings.DEBUG:

    import os

    BASE_DIR = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    ALLOWED_HOSTS = [
        'www.globaltrademotors.com',
        'globaltrademotors.com',
        'trademotors.webfactional.com'
    ]

    EMAIL_HOST = 'smtp.webfaction.com'
    EMAIL_HOST_USER = 'trademotors'
    EMAIL_HOST_PASSWORD = 'sitture2'
    SERVER_EMAIL = 'info@globaltrademotors.com'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['/home/trademotors/webapps/trademotors_static/'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'trademotors',
            'USER': 'trademotors',
            'PASSWORD': 'sitture2',
        }
    }

    STATIC_ROOT = '/home/trademotors/webapps/trademotors_static/'
    MEDIA_ROOT = '/home/trademotors/webapps/trademotors_media/'
    STATICFILES_DIRS = (
        # '/home/trademotors/webapps/trademotors_static/static/static/',
        os.path.join(os.path.dirname(BASE_DIR), 'static', 'templates'),
        os.path.join(os.path.dirname(BASE_DIR), 'static', 'static'),
    )
