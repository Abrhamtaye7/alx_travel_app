"""
Django settings for alx_travel_app project.
"""

from pathlib import Path
import environ
import os

# --- BASE SETUP ---


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environment settings and read .env file
env = environ.Env(
    # Set default type/casting for environment variables if not present
    DEBUG=(bool, False) 
)
# Read .env file (assuming it's in the project root)
environ.Env.read_env(os.path.join(BASE_DIR, '.env')) 


# --- SECURITY & CORE SETTINGS ---

# SECURITY WARNING: The SECRET_KEY is read from the .env file.
# The hardcoded key below is for reference/fallback and should be removed 
# or commented out once env loading is confirmed.
# SECRET_KEY = 'django-insecure-v1hn91uwp!tu3^e&3(=$ax+=08pn2a=qf#4&@xhnzavv@n0oy0'

# Use the key from the environment (e.g., in .env)
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG') 

ALLOWED_HOSTS = []

# --- APPLICATION DEFINITION ---

# Merged INSTALLED_APPS
INSTALLED_APPS = [
    # Django built-ins
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    
    # Local apps
    'listings',
]

# Merged MIDDLEWARE
MIDDLEWARE = [
    # CORS middleware needs to be high up, often before CommonMiddleware
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'alx_travel_app.urls'

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

WSGI_APPLICATION = 'alx_travel_app.wsgi.application'


# --- DATABASE CONFIGURATION ---

# This uses the MySQL settings loaded from the .env file.
# It replaces the default sqlite3 settings.
DATABASES = {
    'default': env.db(),  # env.db() automatically reads DATABASES_URL or the individual DB_ variables
}

# Optional: If you want to manually specify the settings:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': env('DB_NAME'),
#         'USER': env('DB_USER'),
#         'PASSWORD': env('DB_PASSWORD'),
#         'HOST': env('DB_HOST'),
#         'PORT': env('DB_PORT'),
#     }
# }


# --- ADDITIONAL PACKAGE SETTINGS ---

# DRF Settings
REST_FRAMEWORK = {
    # Using openapi schema generator for drf-yasg
    'DEFAULT_SCHEMA_CLASS': 'drf_yasg.openapi.AutoSchema',
}

# CORS Settings
CORS_ALLOW_ALL_ORIGINS = True


# --- STANDARD DJANGO SETTINGS ---

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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'