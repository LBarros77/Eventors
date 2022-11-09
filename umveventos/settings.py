import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'nux-4vko2*7qm8&%r6mwlucqs3eo8+llcl@r3z29wr=-p(e2&9'

DEBUG = True

ALLOWED_HOSTS = ['104.248.9.242', '127.0.0.1', '165.227.79.63','expocigrabackoffice.appdoevento.com.br']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'bootstrap4',
    'crispy_forms',
    # 'django-advanced-filters',
    'system',
    'six',
    'widget_tweaks',
    'qrcode',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'umveventos.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
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

WSGI_APPLICATION = 'umveventos.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'umveventos',
        'USER': 'appdoevento',
        'PASSWORD': 'sRrGncYyB$',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'

DATE_FORMAT = 'j N, Y'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CRISPY_TEMPLATE_PACK = 'bootstrap4'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

ACCOUNT_ADAPTER = 'system.adapter.AccountAdapter'

EMAIL_USE_SSL = False
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'mail.wcore.com.br'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'umv@appdoevento.com.br'
EMAIL_HOST_PASSWORD = 'Wcore32101234'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

LOGGING = {
   'version': 1,
   'disable_existing_loggers': False,
   'handlers': {
      'file': {
         'level': 'DEBUG',
         'class': 'logging.FileHandler',
         'filename': '/tmp/debug.log',
      },
   },
   'loggers': {
      'django': {
         'handlers': ['file'],
         'level': 'DEBUG',
         'propagate': True,
      },
   },
}
