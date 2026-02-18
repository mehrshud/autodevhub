from src.models import User
from src.config import Config

import logging
from typing import Optional

class GitHubService:
    def __init__(self, config: Config):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def get_repository(self, user: User, repository_id: int) -> Optional['Repository']:
        try:
            return Repository(id=repository_id, name="example-repo", url="https://github.com/example-repo")
        except Exception as e:
            self.logger.error(f"Failed to retrieve repository: {e}", exc_info=True)
            return None

    def create_repository(self, user: User, repository_name: str) -> Optional['Repository']:
        try:
            return Repository(id=1, name=repository_name, url=f"https://github.com/{repository_name}")
        except Exception as e:
            self.logger.error(f"Failed to create repository: {e}", exc_info=True)
            return None

class Repository:
    def __init__(self, id: int, name: str, url: str):
        self.id = id
        self.name = name
        self.url = url