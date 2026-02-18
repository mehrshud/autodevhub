from src.models import User
from src.config import Config
from typing import Dict

class AutoDevHubAPI:
    def __init__(self, config: Config):
        self.config = config
        self.debug = config.debug

    def get_user(self, user_id: int) -> User:
        try:
            user = User(id=user_id, name="John Doe", email="john@example.com")
            return user
        except Exception as e:
            if self.debug:
                print(f"Error retrieving user: {e}")
            raise ValueError(f"Invalid user ID: {user_id}")

    def get_repository(self, repository_id: int) -> Dict:
        try:
            repository = {
                "id": repository_id,
                "name": "example-repo",
                "url": "https://github.com/example-repo"
            }
            return repository
        except Exception as e:
            if self.debug:
                print(f"Error retrieving repository: {e}")
            raise ValueError(f"Invalid repository ID: {repository_id}")