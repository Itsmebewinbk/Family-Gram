from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
print("Mode : Dev")
from decouple import config

STATIC_URL = "/api_familygram/api/static/"
MEDIA_URL = "/api_familygram/api/media/"
# Rest settings
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend"
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 20,
    "EXCEPTION_HANDLER": "familygram.config.exception_handler.CustomExceptionHandler",
    "DEFAULT_RENDERER_CLASSES": [
        "familygram.config.renderers.CustomJSONRenderer"
    ],
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
