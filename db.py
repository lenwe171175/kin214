from os import environ, getenv

from kin214.settings import BASE_DIR

DB_TYPE = getenv("DB_TYPE", "sqlite").lower()

if DB_TYPE == "postgres":
    DB_ENGINE = "django.db.backends.postgresql_psycopg2"
    DB_NAME = environ["DB_NAME"]
else:
    DB_ENGINE = "django.db.backends.sqlite3"
    DB_NAME = str(BASE_DIR / "db.sqlite3")

DB_SETTINGS = {
    "NAME": DB_NAME,
    "ENGINE": DB_ENGINE,
    "USER": getenv("DB_USERNAME", ""),
    "PASSWORD": getenv("DB_PASSWORD", ""),
    "HOST": getenv("DB_ADDR", ""),
}