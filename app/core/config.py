import os

from databases import DatabaseURL

# ## DB config
DATABASE_URL_STR = os.getenv("DATABASE_URL", "").replace("postgres://", "postgresql://")
if not DATABASE_URL_STR:
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))
    POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASS = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_NAME = os.getenv("POSTGRES_DB", "postgres")

    DATABASE_URL = DatabaseURL(
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}"
    )
else:
    DATABASE_URL = DatabaseURL(DATABASE_URL_STR)

MAX_CONNECTIONS_COUNT = int(os.getenv("MAX_CONNECTIONS_COUNT", 15))
MIN_CONNECTIONS_COUNT = int(os.getenv("MIN_CONNECTIONS_COUNT", 10))

# ## Project config
PROJECT_NAME = os.getenv("PROJECT_NAME", "dsds_service")
API_V1_STR = "/ga4gh/drs/v1"

# ## Application config
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 5000))


ELIXIR_METADATA_URL= os.getenv("ELIXIR_METADATA_URL", "https://login.elixir-czech.org/oidc/.well-known/openid-configuration")
GLOBUS_CLIENT_ID = os.getenv("GLOBUS_CLIENT_ID", "")
GLOBUS_CLIENT_SECRET = os.getenv("GLOBUS_CLIENT_SECRET", "")
SESSION_SECRET_KEY = os.getenv("SESSION_SECRET_KEY", "763384$%^21&*#4567")
ELIXIR_CLIENT_ID = os.getenv("ELIXIR_CLIENT_ID", "")
ELIXIR_CLIENT_SECRET = os.getenv("ELIXIR_CLIENT_SECRET", "")

