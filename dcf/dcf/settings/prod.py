from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')o)2qy1p@g60s2g^u+d4@r5p11umug@m4h=dhurk47h!6xxzsy'

# Add your site's domain name(s) here.
ALLOWED_HOSTS = ['www.derrickcazardfoundation.org']

# To send email from the server, we recommend django_sendmail_backend
# Or specify your own email backend such as an SMTP server.
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-backend
EMAIL_BACKEND = 'django_sendmail_backend.backends.EmailBackend'

# Default email address used to send messages from the website.
DEFAULT_FROM_EMAIL = 'Derrick Cazard Foundation <info@derrickcazardfoundation.org>'

# A list of people who get error notifications.
ADMINS = [
    ('Administrator', 'admin@derrickcazardfoundation.org'),
]

# A list in the same format as ADMINS that specifies who should get broken link
# (404) notifications when BrokenLinkEmailsMiddleware is enabled.
MANAGERS = ADMINS

# Email address used to send error messages to ADMINS.
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'HOST': 'localhost',
#         'NAME': 'dcf',
#         'USER': 'dcf',
#         'PASSWORD': '',
#         # If using SSL to connect to a cloud mysql database, spedify the CA as so.
#         'OPTIONS': { 'ssl': { 'ca': '/path/to/certificate-authority.pem' } },
#     }
# }

# Use template caching to speed up wagtail admin and front-end.
# Requires reloading web server to pick up template changes.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
        },
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache'),  # noqa
        'KEY_PREFIX': 'coderedcms',
        'TIMEOUT': 14400,  # in seconds
    }
}

try:
    from .local_settings import *  # noqa
except ImportError:
    pass
