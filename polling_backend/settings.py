# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = 'django-insecure-your-secret-key'
# DEBUG = True
# ALLOWED_HOSTS = []

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'polls',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'polling_backend.urls'

# TEMPLATES = [{
#     'BACKEND': 'django.template.backends.django.DjangoTemplates',
#     'DIRS': [],
#     'APP_DIRS': True,
#     'OPTIONS': {
#         'context_processors': [
#             'django.template.context_processors.debug',
#             'django.template.context_processors.request',
#             'django.contrib.auth.context_processors.auth',
#             'django.contrib.messages.context_processors.messages',
#         ],
#     },
# }]

# WSGI_APPLICATION = 'polling_backend.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# AUTH_PASSWORD_VALIDATORS = []

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# STATIC_URL = '/static/'
# from pathlib import Path
# import os
# import dj_database_url  # This is required. Install with: pip install dj-database-url

# BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = os.environ.get("SECRET_KEY", 'django-insecure-your-secret-key')  # Use env var in prod
# DEBUG = os.environ.get("DEBUG", "False") == "True"  # Set DEBUG=False by default in production

# ALLOWED_HOSTS = ['*']  # Render will set this via env or you can specify actual domain

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'polls',
#     'whitenoise.runserver_nostatic',  # For static files
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',  # Serve static files efficiently
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'polling_backend.urls'

# TEMPLATES = [{
#     'BACKEND': 'django.template.backends.django.DjangoTemplates',
#     'DIRS': [],
#     'APP_DIRS': True,
#     'OPTIONS': {
#         'context_processors': [
#             'django.template.context_processors.debug',
#             'django.template.context_processors.request',
#             'django.contrib.auth.context_processors.auth',
#             'django.contrib.messages.context_processors.messages',
#         ],
#     },
# }]

# WSGI_APPLICATION = 'polling_backend.wsgi.application'

# # DATABASE CONFIGURATION FOR RENDER
# DATABASES = {
#     'default': dj_database_url.config(
#         default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}", conn_max_age=600
#     )
# }

# AUTH_PASSWORD_VALIDATORS = []  # You can add validators if needed

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# # STATIC FILES
# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'

# # Enable GZip and caching for static files
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# from pathlib import Path
# import os
# import dj_database_url  # make sure to install this: pip install dj-database-url

# BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = os.environ.get("SECRET_KEY", "your-local-secret-key")

# DEBUG = os.environ.get("DEBUG", "") != "False"

# ALLOWED_HOSTS = ['*']  # You can replace '*' with your Render domain for more security

# # Application definition
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'polls',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',  # Required for serving static files
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'polling_backend.urls'

# TEMPLATES = [{
#     'BACKEND': 'django.template.backends.django.DjangoTemplates',
#     'DIRS': [],
#     'APP_DIRS': True,
#     'OPTIONS': {
#         'context_processors': [
#             'django.template.context_processors.debug',
#             'django.template.context_processors.request',
#             'django.contrib.auth.context_processors.auth',
#             'django.contrib.messages.context_processors.messages',
#         ],
#     },
# }]

# WSGI_APPLICATION = 'polling_backend.wsgi.application'

# # Database: uses PostgreSQL on Render, SQLite locally
# DATABASES = {
#     'default': dj_database_url.config(
#         default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
#         conn_max_age=600,
#         ssl_require=True
#     )
# }

# AUTH_PASSWORD_VALIDATORS = []

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# # Static files settings
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# # Enable WhiteNoise to serve static files
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-your-secret-key")
DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = ["polling-django.onrender.com"]  # or use your custom domain

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # 🧊 Enables static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'polling_backend.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'],  # Optional: template folder if used
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}]

WSGI_APPLICATION = 'polling_backend.wsgi.application'

# DATABASE (default SQLite or Render-provided via DATABASE_URL)
DATABASES = {
    'default': dj_database_url.config(default=f'sqlite:///{BASE_DIR / "db.sqlite3"}', conn_max_age=600)
}

# Password validators (you can add more if needed)
AUTH_PASSWORD_VALIDATORS = []

# Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files config
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
