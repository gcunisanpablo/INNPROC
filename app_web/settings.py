"""
Django settings for app_web project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-z1f4v7g2e!a_#n0+)r(rfprzr0&1hpnm%ah363g%b$#kyve*wd"

TIME_ZONE = "America/Bogota"  # Zona horaria para Colombia
USE_TZ = (
    True  # Asegúrate de que esté activado para manejar la zona horaria correctamente
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Para servidor en la red: "10.1.4.96", "localhost"
# ALLOWED_HOSTS = ["*"]
ALLOWED_HOSTS = [
    "*",
    # (IPv4)
    "10.1.4.96",
    # localhost
    "127.0.0.1",
    # localhost
    "localhost",
    # ngrok
    "d3df-191-88-170-184.ngrok-free.app",
]
CSRF_TRUSTED_ORIGINS = [
    "https://d3df-191-88-170-184.ngrok-free.app",
    # Si tienes otras URL de ngrok, agrega también.
]
CORS_ALLOWED_ORIGINS = [
    "https://d3df-191-88-170-184.ngrok-free.app",
    "https://example.com",
]
# Asegúrate de que no está forzando HTTPS en desarrollo
SECURE_SSL_REDIRECT = False  # Desactiva la redirección forzada a HTTPS
SECURE_HSTS_SECONDS = 0  # Evita que Django use HSTS
CORS_ALLOW_ALL_ORIGINS = True


CORS_ALLOW_HEADERS = [
    "content-type",
    "authorization",
]
CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "DELETE",
]


# Establece el tiempo de inactividad de la sesión (en segundos)
# Si no quieres que la sesión se cierre por inactividad, usa un valor muy alto
SESSION_SAVE_EVERY_REQUEST = True  # Para que la sesión se guarde en cada solicitud


# Application definition

INSTALLED_APPS = [
    # panel
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    # My apps
    "usuarios",
    "gestor_archivos",
    "glosario",
    "documentacion",
    "mapa_procesos",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "app_web.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "app_web.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "dbrepsan",
        "USER": "postgres",
        "PASSWORD": "1234",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# SMTP CONFIG
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "proluxgamer456@gmail.com"
EMAIL_HOST_PASSWORD = "mphp feqd tnas vnwb"


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "es"
LANGUAGES = [
    ("es", "Español"),
    ("en", "Inglés"),
    # Otros idiomas que quieras agregar
]

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

FILE_UPLOAD_PERMISSIONS = (
    0o644  # Lectura/escritura para el propietario, solo lectura para otros
)

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",  # Carpeta global para archivos estáticos
]

STATIC_ROOT = (
    BASE_DIR / "staticfiles"
)  # Carpeta donde se recopilan los archivos estáticos al ejecutar collectstatic

LOGIN_URL = "login/"  # O cualquier otra ruta de inicio de sesión que tengas

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(
    BASE_DIR, "media"
)  # Ajusta la ruta según tu estructura de carpetas


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# settings.py

LOGIN_REDIRECT_URL = "login/"  # O cualquier otra URL donde debería ir el usuario

# settings.py
CSRF_COOKIE_NAME = "csrftoken"  # Nombre de la cookie de CSRF

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-danger",
    "accent": "accent-lightblue",
    "navbar": "navbar-danger navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-danger",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "pulse",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
    "actions_sticky_top": False,
}

JAZZMIN_SETTINGS = {
    # Título de la ventana (Por defecto, usa el título del sitio si no se especifica)
    "site_title": "Panel administrador",
    # Título en la pantalla de inicio de sesión (máximo 19 caracteres)
    # (Por defecto, usa el encabezado del sitio si no se especifica)
    "site_header": "Panel administrador",
    # Título que se muestra en la marca (máximo 19 caracteres)
    # (Por defecto, usa el encabezado del sitio si no se especifica)
    "site_brand": "Administracion",
    # Logo para usar en el sitio, debe estar presente en los archivos estáticos
    # Se usa como la marca en la parte superior izquierda
    "site_logo": "img/Logo_blanco.png",
    # Logo para la página de inicio de sesión, debe estar en los archivos estáticos
    # Si no se especifica, se utiliza el mismo logo que `site_logo`
    "login_logo": None,
    # Logo para la página de inicio de sesión en temas oscuros
    # (Si no se especifica, se utiliza el `login_logo`)
    "login_logo_dark": None,
    # Clases CSS aplicadas al logo del sitio
    "site_logo_classes": "logo-personalizado",
    # Ruta relativa al favicon para el sitio, se usará el `site_logo` por defecto si no se especifica
    # (Idealmente 32x32 px)
    "site_icon": "img/unisanp.ico",
    # Texto de bienvenida en la pantalla de inicio de sesión
    "welcome_sign": "bienvenido al sitio de administracion del repositorio",
    # Copyright en el pie de página
    "copyright": "Uniminuto",
    # Lista de modelos de administradores para buscar desde la barra de búsqueda
    # Si se omite, la barra de búsqueda no aparecerá
    # Si quieres usar un único campo de búsqueda, puedes usar solo una cadena
    "search_model": [
        "auth.User",
    ],
    # Nombre del campo del modelo de usuario que contiene la imagen de avatar
    # Puede ser un ImageField, URLField, CharField, o una función que reciba al usuario
    "user_avatar": None,
    ############
    # Menú superior #
    ############
    # Enlaces para mostrar en el menú superior
    "topmenu_links": [
        # URL que se invierte (se pueden añadir permisos)
        {"name": "Inicio", "url": "admin:index", "permissions": ["auth.view_user"]},
        # URL externa que se abre en una nueva ventana (se pueden añadir permisos)
        # Modelo de administrador al que se enlaza (los permisos se verifican contra el modelo)
        {"model": "auth.User"},
        # Aplicación con un menú desplegable a todas sus páginas de modelos (los permisos se verifican contra los modelos)
        {"app": "books"},
    ],
    #############
    # Menú de usuario #
    #############
    # Enlaces adicionales en el menú del usuario en la parte superior derecha
    # (Los enlaces de tipo "app" no se permiten aquí)
    "usermenu_links": [
        {
            "name": "Mapa Procesos",
            "url": "/mapa-procesos/",
            "new_window": False,
        },
    ],
    #############
    # Menú lateral #
    #############
    # Mostrar el menú lateral
    "show_sidebar": False,
    # Expandir automáticamente el menú lateral
    "navigation_expanded": False,
    # Ocultar estas aplicaciones al generar el menú lateral (por ejemplo, 'auth')
    "hide_apps": [],
    # Ocultar estos modelos al generar el menú lateral (por ejemplo, 'auth.user')
    "hide_models": [],
    # Lista de aplicaciones (y/o modelos) para ordenar el menú lateral
    # No es necesario que contenga todas las aplicaciones/modelos
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
    # Enlaces personalizados que se añaden a los grupos de aplicaciones, indexados por nombre de la aplicación
    "custom_links": {
        "books": [
            {
                "name": "Make Messages",
                "url": "make_messages",
                "icon": "fas fa-comments",
                "permissions": ["books.view_book"],
            }
        ]
    },
    # Iconos personalizados para aplicaciones/modelos en el menú lateral
    # Puedes ver los iconos disponibles en FontAwesome
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Iconos por defecto cuando no se especifica uno manualmente
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #################
    # Modal relacionado #
    #################
    # Usar modales en lugar de ventanas emergentes
    "related_modal_active": True,
    #############
    # Ajustes de la interfaz #
    #############
    # Rutas relativas a archivos CSS/JS personalizados (deben estar en los archivos estáticos)
    "custom_css": "css/custom_admin.css",
    "custom_js": None,
    # Si se usa la fuente de Google Fonts desde fonts.googleapis.com (de lo contrario, usa `custom_css` para suministrar la fuente)
    "use_google_fonts_cdn": True,
    # Si mostrar el personalizador de UI en la barra lateral
    "show_ui_builder": False,
    ###############
    # Vista de cambio #
    ###############
    # Cómo renderizar la vista de cambio, opciones actuales:
    # - single
    # - horizontal_tabs (por defecto)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # Sobrescribir el formato de cambio para un modelo específico
    "changeform_format_overrides": {
        "auth.user": "horizontal_tabs",
        "auth.group": "vertical_tabs",
    },
    # Añadir un selector de idioma en el panel de administración
    "language_chooser": False,
}
