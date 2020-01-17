"""
Django settings for xyj project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
# Dev = 开发环境  Test = 测试环境  Pro = 生产
APP_ENV = 'Dev'
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=w%_(%#u$ff_f2hmrsb_1t7t=yz*dcr7skw2ocme%z5h-4-9yo'

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
    'adm',
    'api',
    'adm.templatetags.dealwithtime',
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

ROOT_URLCONF = 'xyj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'xyj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'py_xyj',
        'USER': 'xyopen',
        'PASSWORD': 'Jx4h3FFN4a!@#$%D3ytwr3DGh',
        'HOST': '58e33ba947df6.gz.cdb.myqcloud.com',
        'PORT': '10594',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# 发送邮箱验证码
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com' # 服务器
EMAIL_HOST_USER = 'zhoucg_8699' # 账号
EMAIL_HOST_PASSWORD = 'zhou1991' # 密码(这里是你的授权码)
EMAIL_FROM = "zhoucg_8699@163.com"      # 邮箱来自


# 环境判断设置常量
if APP_ENV == 'Pro':
    DEBUG = False
    ALLOWED_HOSTS = ['*']
    STATIC_ROOT = os.path.join(BASE_DIR, "static")

    # 发送邮箱验证码
    EMAIL_PORT = 465  # 一般情况下都为25 , 465, 587
    EMAIL_USE_SSL = True
    APP_HOST = 'https://pro.sc578.cn/media/'
else:
    DEBUG = True
    ALLOWED_HOSTS = []
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

    # 发送邮箱验证码
    EMAIL_PORT = 25  # 一般情况下都为25 , 465, 587
    EMAIL_USE_TLS = False       # 一般都为False
    APP_HOST = 'http://127.0.0.1:8000/media/'

# 小程序配置参数
APP_ID = 'wx8769019bd9853a3f'
APP_SECRET = '16d681224074510a7e095bfb3ae8b3d6'

# 公用URL，指向上传文件的基本路径
MEDIA_URL = '/media/'

# 上传文件在服务器中的基本路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
