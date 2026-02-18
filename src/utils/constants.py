Here's the improved code:

from typing import Dict
from .models import User
from .config import Config
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MAX_REPOSITORIES: int = 100
MAX_USERS: int = 1000
DEFAULT_CONFIG: Config = Config(debug=False, db_url='sqlite:///default.db')

def get_default_config() -> Config:
    """
    Returns the default configuration.
    """
    return DEFAULT_CONFIG

def get_max_repositories() -> int:
    """
    Returns the maximum number of repositories allowed.
    """
    return MAX_REPOSITORIES

def get_max_users() -> int:
    """
    Returns the maximum number of users allowed.
    """
    return MAX_USERS

USER_ROLES: Dict[str, Dict[str, bool]] = {
    'admin': {'read': True, 'write': True, 'delete': True},
    'user': {'read': True, 'write': False, 'delete': False}
}

def get_user_role_permissions(role: str) -> Dict[str, bool]:
    """
    Returns the permissions for a given user role.
    """
    return USER_ROLES.get(role, {})