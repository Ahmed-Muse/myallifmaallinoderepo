"""
Django settings for allifproject project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w3(g392k5f%a)m_@-)=di9&&_)qy@x9@=_3#l!#$&g&@cfin03'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['194.195.244.199','http://www.allifmaalltd.com/','localhost','allifmaalltd.com','www.allifmaalltd.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "myfirstapp",
    "login",
    'crispy_forms',
    "allifmaalapp",
    
    "django.contrib.humanize",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'allifproject.urls'

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

WSGI_APPLICATION = 'allifproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


#PATH WHERE UPLOADED FILES WILL BE STORED...in the media folder
MEDIA_ROOT=os.path.join(BASE_DIR,'static/media')
MEDIA_URL='/media/'#fetch images/media using this path when viewing through the browser..

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
"""
arabic-reshaper==2.1.4
asgiref==3.5.2
asn1crypto==1.5.1
certifi==2022.9.24
cffi==1.15.1
charset-normalizer==2.1.1
click==8.1.3
colorama==0.4.5
cryptography==38.0.1
cssselect2==0.7.0
Django==4.1.1
django-crispy-forms==1.14.0
future==0.18.2
html5lib==1.1
humanize==4.4.0
idna==3.4
lxml==4.9.1
oscrypto==1.3.0
Pillow==9.2.0
pycparser==2.21
pyHanko==0.14.0
pyhanko-certvalidator==0.19.5
PyPDF3==1.0.6
python-bidi==0.4.2
pytz==2022.2.1
pytz-deprecation-shim==0.1.0.post0
PyYAML==6.0
qrcode==7.3.1
reportlab==3.6.11
requests==2.28.1
six==1.16.0
sqlparse==0.4.2
svglib==1.4.1
tinycss2==1.1.1
tqdm==4.64.1
tzdata==2022.2
tzlocal==4.2
uritools==4.0.0
urllib3==1.26.12
webencodings==0.5.1
xhtml2pdf==0.2.8

"""
