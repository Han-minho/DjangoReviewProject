"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from django.utils.translation import gettext_lazy as _
import shop.context_processor

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u3p0$p+fm0_0)!-0i8wd$c$*nq@o#h9=td31ewj$^+mefw!kxq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'mysite.com', 'localhost', '127.0.0.1', 'ee03-221-146-62-123.ngrok.io',
]

SITE_ID = 1
# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'social_django',
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'blog.apps.BlogConfig',
    'taggit',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.postgres',
    'shop.apps.ShopConfig',
    'rosetta',
    'parler',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "shop.context_processor.cart",
                # 'social_django.context_processors.backends',
                # 'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_dummy',
        'USER': 'blog_dummy',
        'PASSWORD': '1234',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# 이메일 서버 구성
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_POST = 587
EMAIL_USE_TLS = True

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# SESSION_REDIS_ALIAS = "default"
#
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient"
#         }
#     }
# }

CART_SESSION_ID = 'cart'

AUTHENTICATION_BACKENDS = [
    'social_core.backends.naver.NaverOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]
SOCIAL_AUTH_NAVER_KEY = 'JiARA_lKm_5xm9Sd9l4x'
SOCIAL_AUTH_NAVER_SECRET = 'TXMPVDfEVC'

# 네이버 소셜 로그인 데이터 범위
SOCIAL_AUTH_NAVER_EXTRA_DATA = ['profile_image']

SOCIAL_AUTH_JSONFIELD_ENABLED = True

# SOCIAL_AUTH_POSTGRES_JSONFIELD = True  # Before
# SOCIAL_AUTH_JSONFIELD_ENABLED = True  # After
#
# SOCIAL_AUTH_JSONFIELD_CUSTOM = 'django.contrib.postgres.fields.JSONField'
#
# SOCIAL_AUTH_JSONFIELD_CUSTOM = 'django.db.models.JSONField'
#
# SOCIAL_AUTH_URL_NAMESPACE = 'social'

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]
LANGUAGES = [
    ('en', _('English')),
    ('ko', _('Korean')),
]

PARLER_LANGUAGES = {
    1: (
        {'code': 'en'},
        {'code': 'ko'},
    ),
    'default': {
        'fallback': 'en',
        'hide_untranslated': False,
    }
}

CELERY_TASK_ALWAYS_EAGER = True

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1

LOGIN_REDIRECT_URL = 'home'

# Stripe 설정
# Publishable key
# STRIPE_PUBLISHABLE_KEY = 'pk_test_51NiU7PCwCR8LeetfU8mQr7VCIF5mrXxHQZlIMNhKoyshyjZrbGjljVb6zikMcFdB1yv5GcU7fsQeYl3DRU8NW1Yx00WdrGvZ9v'
# Secret key
# STRIPE_SECRET_KEY = 'sk_test_51NiU7PCwCR8LeetflVLWoyUA2rOxaY0a1xk5GmjONzWpoVCTlgPyueHBipBsAosSpTfF5aQi8mzHWvgkee3zrHqe006nOQNICk'
# STRIPE_API_VERSION = '2022-08-01'

# CSRF_TRUSTED_ORIGINS = ['https://ee03-221-146-62-123.ngrok.io']

# 토스 API 키 설정
TOSS_CLIENT_KEY = 'test_ck_Z61JOxRQVE1BbyNmGzaVW0X9bAqw'
TOSS_SECRET_KEY = 'test_sk_Z1aOwX7K8me4vxjJgmW8yQxzvNPG'
TOSS_API_VERSION = '2022-11-16'
