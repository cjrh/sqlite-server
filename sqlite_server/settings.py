from biodome import environ

# We'll make an outgoing connection to another server
TARGET_SERVER_URL: str = environ.get('TARGET_SERVER_URL', '')
TARGET_SERVER_PORT: int = environ.get('TARGET_SERVER_PORT', 8300)
IDENTITY: bytes = environ.get('IDENTITY', 'NO_IDENTITY', cast=str.encode)
