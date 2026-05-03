from pathlib import Path
import os

# ---------------- BASE ----------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------- SECURITY ----------------
SECRET_KEY = 'django-insecure--l@gh46d)gv*bkxc4v$cvtr*y&m9r7gu%@=r+76ugfmvi5c8)e'

DEBUG = False

ALLOWED_HOSTS = [
    "portfolio-backend-ww34.onrender.com",
    ".vercel.app",
]

# ---------------- APPS ----------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'api',
]

# ---------------- MIDDLEWARE ----------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # MUST be first
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ---------------- URL ----------------
ROOT_URLCONF = 'backend.urls'

# ---------------- TEMPLATES ----------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ---------------- WSGI ----------------
WSGI_APPLICATION = 'backend.wsgi.application'

# ---------------- DATABASE ----------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ---------------- PASSWORD ----------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

# ---------------- INTERNATIONAL ----------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ---------------- CORS ----------------
CORS_ALLOWED_ORIGINS = [
    "https://portfolio-frontend-ruddy-two.vercel.app",
]

CORS_ALLOW_CREDENTIALS = True

# ---------------- CSRF ----------------
CSRF_TRUSTED_ORIGINS = [
    "https://portfolio-frontend-ruddy-two.vercel.app",
    "https://portfolio-backend-ww34.onrender.com",
]

# ---------------- STATIC ----------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ---------------- MEDIA ----------------
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ---------------- EXTRA ----------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Fix HTTPS proxy issues on Render
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')