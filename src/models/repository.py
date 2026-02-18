from src.config import Config
from src.models import User
from src.database import db
import logging

class Repository:
    def __init__(self, id: int, name: str, url: str):
        self.id = id
        self.name = name
        self.url = url

    def __str__(self):
        return f"Repository(id={self.id}, name='{self.name}', url='{self.url}')"

    @classmethod
    def from_db(cls, db_row: dict) -> 'Repository':
        try:
            return cls(id=db_row['id'], name=db_row['name'], url=db_row['url'])
        except KeyError as e:
            logging.error(f"Failed to create Repository instance from database row: {str(e)}")
            raise ValueError("Invalid database row format") from e
        except Exception as e:
            logging.error(f"Failed to create Repository instance from database row: {str(e)}")
            raise

    @classmethod
    def get_all(cls) -> list['Repository']:
        try:
            db_rows = db.query("SELECT * FROM repositories")
            return [cls.from_db(db_row) for db_row in db_rows]
        except Exception as e:
            logging.error(f"Failed to retrieve all repositories: {str(e)}")
            raise RuntimeError("Failed to retrieve repositories from the database") from e

    def save(self) -> None:
        try:
            db.query("INSERT INTO repositories (id, name, url) VALUES (%s, %s, %s)", (self.id, self.name, self.url))
        except Exception as e:
            logging.error(f"Failed to save repository: {str(e)}")
            raise RuntimeError("Failed to save repository to the database") from e