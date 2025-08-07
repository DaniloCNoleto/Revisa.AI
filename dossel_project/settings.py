import os
from pathlib import Path
from dotenv import load_dotenv

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Carrega variáveis de ambiente do arquivo .env localizado na raiz do projeto
load_dotenv(dotenv_path=BASE_DIR / '.env')

# -----------------------------------------------------------------------------
# Configurações básicas
# -----------------------------------------------------------------------------
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'changeme')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

# -----------------------------------------------------------------------------
# Aplicativos instalados
# -----------------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'revisor',
    'django.contrib.sites',
]

# -----------------------------------------------------------------------------
# Middleware
# -----------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# -----------------------------------------------------------------------------
# URL / WSGI
# -----------------------------------------------------------------------------
ROOT_URLCONF = 'dossel_project.urls'
WSGI_APPLICATION = 'dossel_project.wsgi.application'

# -----------------------------------------------------------------------------
# Templates
# -----------------------------------------------------------------------------
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'],
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

# -----------------------------------------------------------------------------
# Banco de dados
# -----------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -----------------------------------------------------------------------------
# Arquivos estáticos
# -----------------------------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# -----------------------------------------------------------------------------
# Arquivos de mídia e pastas de entrada/saída centralizadas
# -----------------------------------------------------------------------------
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

PASTA_ENTRADA       = MEDIA_ROOT / 'entrada'
PASTA_SAIDA         = MEDIA_ROOT / 'saida'
PASTA_TEMP          = MEDIA_ROOT / 'temp_files'
PASTA_CANCELAMENTO  = MEDIA_ROOT / 'cancel_signals'

# -----------------------------------------------------------------------------
# Configurações adicionais
# -----------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_URL  = 'login'
LOGOUT_URL = 'logout'

# -----------------------------------------------------------------------------
# Email
# -----------------------------------------------------------------------------
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True
EMAIL_HOST_USER     = 'dossel2008@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('SENHA_APP')
DEFAULT_FROM_EMAIL  = 'Dossel Ambiental <dossel2008@gmail.com>'
SERVER_EMAIL        = EMAIL_HOST_USER

# -----------------------------------------------------------------------------
# Sites Framework
# -----------------------------------------------------------------------------
SITE_ID = 2
