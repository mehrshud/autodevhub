from typing import Any, Dict
from src.models import User
from src.config import Config
from src.types import Repository
import logging

def get_user_info(user: User) -> Dict[str, Any]:
    try:
        user_info = {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
        logging.info("Retrieved user info")
        return user_info
    except Exception as e:
        logging.error(f"Failed to retrieve user info: {e}", exc_info=True)
        return {}

def get_repository_info(repository: Repository) -> Dict[str, Any]:
    try:
        repository_info = {
            "id": repository.id,
            "name": repository.name,
            "url": repository.url
        }
        logging.info("Retrieved repository info")
        return repository_info
    except Exception as e:
        logging.error(f"Failed to retrieve repository info: {e}", exc_info=True)
        return {}

def get_config_info(config: Config) -> Dict[str, Any]:
    try:
        config_info = {
            "debug": config.debug,
            "db_url": config.db_url
        }
        logging.info("Retrieved config info")
        return config_info
    except Exception as e:
        logging.error(f"Failed to retrieve config info: {e}", exc_info=True)
        return {}