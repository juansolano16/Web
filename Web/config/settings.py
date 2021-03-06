"""
Django settings for Web project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!3eii%1+7=2p&r@qbsyhth3mbssh1ax*1tuc*$(xyu5_y#dr8n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

################################################
######## CONTROL DE ARCHIVOS STATICOS ##########
if DEBUG:
    folder_img = r'\\10.10.10.66\imagenes'
    static_files_ = (os.path.join(BASE_DIR, 'static'), folder_img,)
    static_url_img = '/static/'
    path_electronicos = r'\\10.10.10.63\comprobantes'
    path_bodegaV = r'\\10.10.10.66\Users\Administrador.MULTIMOTOS-SA\Desktop\BodegaProveedores'

else:
    folder_img = '/home/Web/imagenes'
    static_files_ = (os.path.join(BASE_DIR, 'static'),)
    static_url_img = '/static/img_66/'
    path_electronicos = '/home/Web/ComprobantesElectronicos'
    path_bodegaV = '/home/Web/vbodegas'


###############################################
###############################################
ALLOWED_HOSTS = ['*', ]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps Terceros
    'rest_framework',
    'widget_tweaks',
    'django_q',
    'compressor',
    'django_embed_template',
    'crispy_forms',
    # 'djcelery',

    # Apps Creadas
    'core.inventario',
    'core.homepage',
    'core.login',
    'core.user',
    'core.facturacion',
    'core.personal',
    'core.notificaciones',
    'core.electronicos',
    'core.Repositorio',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'crum.CurrentRequestUserMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/sqlite3'),
    },
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'unnopartsdb',
        'USER': 'stock',
        'PASSWORD': '.multim0t0s.',
        'HOST': '10.10.10.32',
        'PORT': '1521',
    },
    'mysql': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gestioncomprobante',
        'USER': 'user',
        'PASSWORD': '',
        'HOST': '10.10.10.63',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}

DATABASE_ROUTERS = ['db.router.OracleRouter', 'db.router.MySqlRouter']

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-ec'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Guayaquil'
USE_I18N = True
USE_L10N = True
USE_TZ = True

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = static_files_

# https://django-compressor.readthedocs.io/en/stable/settings/#base-settings
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)
COMPRESS_ENABLED = True


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = '/login/'

AUTH_USER_MODEL = 'user.User'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.office365.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = "notificaciones@unnoparts.com.ec"
EMAIL_HOST_PASSWORD = "Usuario2020"
EMAIL_USE_TLS = True

Q_CLUSTER = {
    'name': 'DjangORM',
    'retry': 600,
    'workers': 10,
    'save_limit': 0,
    'orm': 'sqlite',
    # 'sync':True,
    # 'catch_up': False,
}
