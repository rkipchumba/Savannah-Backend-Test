from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-!1krs3+qkskbkqau)yom_%@k6+qn(5k9i&je!md@k-1ve5si7='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'customers_orders',
    'social_django'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',

]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id_connect.OpenIdConnectAuth',
    'django.contrib.auth.backends.ModelBackend'
)

SOCIAL_AUTH_OPENIDCONNECT_KEY = '654541876298-m4upiusv9rjo88qmjvh4rtcvn8ng67tj.apps.googleusercontent.com'
SOCIAL_AUTH_OPENIDCONNECT_SECRET = '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'
SOCIAL_AUTH_OPENIDCONNECT_URL_AUTH = 'https://accounts.google.com/o/oauth2/auth'
SOCIAL_AUTH_OPENIDCONNECT_URL_KEYSET = 'https://www.googleapis.com/oauth2/v3/certs'
SOCIAL_AUTH_OPENIDCONNECT_URL_TOKEN = 'https://accounts.google.com/o/oauth2/token'
SOCIAL_AUTH_OPENIDCONNECT_URL_USERINFO = 'https://www.googleapis.com/oauth2/v3/userinfo'

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

ROOT_URLCONF = 'savannah_task.urls'

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

WSGI_APPLICATION = 'savannah_task.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rodgers',
        'USER': 'rodgers',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

USERNAME = 'sandbox'
API_KEY = 'e68a6ba30bff8ea7204421b6f805d0c44d0ebb957e966c8d812be5085aa377d3'


"""
To enhance the security of the application, including protection 
against Cross-Site Scripting (XSS) attacks, restrict the types of 
content that can be loaded on  web pages
"""
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

