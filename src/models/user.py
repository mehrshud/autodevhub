from src.api.github import GitHubClient
from src.config import Config
from typing import Optional
import logging

class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    @classmethod
    def get_user(cls, user_id: int) -> Optional['User']:
        try:
            users = [
                User(1, "John Doe", "john@example.com"),
                User(2, "Jane Doe", "jane@example.com")
            ]
            user = next((u for u in users if u.id == user_id), None)
            if user:
                logging.info(f"Retrieved user {user_id}")
            return user
        except Exception as e:
            logging.error(f"Error retrieving user {user_id}: {str(e)}")
            return None

    def __str__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"