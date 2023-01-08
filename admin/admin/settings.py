"""
Django settings for admin project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(cx1!)ziag&g9k(xn%h1odef+t432cggcby4o0(*=r*787@8#r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'constance',
    'rest_framework',
    'corsheaders',
    'products',
    'drf_yasg',
    'graphene_django',
    'health_check',                             # required
    'health_check.db',                          # stock Django health checkers
    'health_check.cache',
    'health_check.storage',
    'health_check.contrib.redis',               # requires Redis broker
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REDIS_URL = "redis://" + os.environ.get('REDIS_HOST', 'localhost') + ":6379"

HEALTH_CHECK = {
    # View
    'SERVICE_NAME': None,
    'CHECK_DATABASE': True,
    'CHECK_CACHE': True,

    # Middleware
    'HEADER_FIELD': 'X-Health',
    'HEADER_VALUE': 'health-check',
    'ALLOWED_PATHS': None,  # all others urls, use original ALLOWED_HOSTS. Ex: ['api/v1/health', '/health'], None allow all
    'ALLOWED_HOSTS': None,  # check request host is in a list, Ex: ['127.0.0.1', 'www.domain.com'], None allow all
}
print(REDIS_URL)

CONSTANCE_CONFIG = {
    'THE_ANSWER': (42, 'Answer to the Ultimate Question of Life, '
                       'The Universe, and Everything')
}
CONSTANCE_BACKEND = 'constance.backends.redisd.RedisBackend'
CONSTANCE_BACKEND = 'constance.backends.redisd.CachingRedisBackend'
# optionally set a value ttl
CONSTANCE_REDIS_CACHE_TIMEOUT = 60
CONSTANCE_REDIS_CONNECTION = {
    'host': os.environ.get('REDIS_HOST', '127.0.0.1'),
    'port': 6379,
    'db': 0,
}

FORCE_SCRIPT_NAME = os.environ.get('BASE_PATH', '')


ROOT_URLCONF = 'admin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'admin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'porsfkci',
        'USER': 'porsfkci',
        'PASSWORD': 'dNAVaiU2ngO5fYftVz9EFBtslSfvJKOE',
        'HOST': 'mouse.db.elephantsql.com', # Service name from docker-compose.yml
        'PORT': 5432, # Service port from docker-compose.yml,
        'OPTIONS': {
            'connect_timeout': 3,
        }
    }
}

SWAGGER_SETTINGS = {
   'USE_SESSION_AUTH': False,
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1", 
]