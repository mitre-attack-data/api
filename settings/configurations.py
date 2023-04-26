import os


class DefaultConfig:
    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = os.environ.get("SECRET_KEY")
    ALGORITHM = os.environ.get("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", "10"))

    # MongoDB Cluter
    CLUSTER_USERNAME = os.environ.get("CLUSTER_USERNAME")
    CLUSTER_PASSWORD = os.environ.get("CLUSTER_PASSWORD")
    DATABASE_NAME_USERS = os.environ.get("DATABASE_NAME_USERS")
    DATABASE_NAME_MITRE = os.environ.get("DATABASE_NAME_MITRE")

    # Email
    FROM_EMAIL = os.environ.get("FROM_EMAIL")
    FROM_PWD = os.environ.get("FROM_PWD")
    IMAP_SERVER = os.environ.get("IMAP_SERVER")

    # SMTP Server
    SMTP_PWD = os.environ.get("SMTP_PWD")
    SMTP_SERVER = os.environ.get("SMTP_SERVER")
    SMTP_PORT = os.environ.get("SMTP_PORT")
    STMP_API_KEY = os.environ.get("STMP_API_KEY")
