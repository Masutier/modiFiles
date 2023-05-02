import os
import json

def localSett():
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'bootstrap5',
        'csv_all',
        'pdf_all',
        'xls_all',
        'modiFiles',

    ]

    return ALLOWED_HOSTS, INSTALLED_APPS


def prodSett():
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']

    RECAPTCHA_PUBLIC_KEY = config['RECAT_PUBLIC_KEY_DEBUG']
    RECAPTCHA_PRIVATE_KEY = config['RECAT_SECRET_KEY_DEBUG']

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'bootstrap5',
        'captcha',
        'csv_all',
        'pdf_all',
        'xls_all',
        'modiFiles',

    ]

    return ALLOWED_HOSTS, RECAPTCHA_PUBLIC_KEY, RECAPTCHA_PRIVATE_KEY, INSTALLED_APPS

def securityFileHome():
    with open("/home/gabriel/prog/json_config/modiFiles.json") as config_file:
        config = json.load(config_file)
    return config

def securityFileProduction():
    with open("C:\inetpub\wwwroot\modiFiles.json") as config_file:
        config = json.load(config_file)
    return config
