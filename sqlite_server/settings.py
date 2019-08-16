from typing import Callable
from biodome import environ

# We'll make an outgoing connection to another server
TARGET_SERVER_URL: Callable[[], str] = environ.get_callable('TARGET_SERVER_URL', '')
TARGET_SERVER_PORT: Callable[[], int] = environ.get_callable('TARGET_SERVER_PORT', 8300)
IDENTITY: str = environ.get('IDENTITY', 'NO_IDENTITY')
