from src.models import User
from src.config import Config
import logging
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

logger = logging.getLogger(__name__)

Base = declarative_base()

class Repository(Base):
    """Repository model."""
    __tablename__ = 'repositories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)

class Database:
    """Database interface."""
    def __init__(self, config: Config):
        """
        Initialize the database.

        Args:
        config (Config): The configuration.
        """
        self.engine = create_engine(config.db_url)
        Base.metadata.create_all(self.engine)
        self.session: Session = sessionmaker(bind=self.engine)()

    def get_user(self, user_id: int) -> Optional[User]:
        """
        Get a user by ID.

        Args:
        user_id (int): The user ID.

        Returns:
        Optional[User]: The user or None if not found.
        """
        try:
            return self.session.query(User).get(user_id)
        except Exception as e:
            logger.error(f"Error getting user: {e}", exc_info=True)
            return None

    def get_repositories(self) -> List[Repository]:
        """
        Get all repositories.

        Returns:
        List[Repository]: The repositories.
        """
        try:
            return self.session.query(Repository).all()
        except Exception as e:
            logger.error(f"Error getting repositories: {e}", exc_info=True)
            return []

    def add_repository(self, repository: Repository) -> None:
        """
        Add a repository.

        Args:
        repository (Repository): The repository.
        """
        try:
            self.session.add(repository)
            self.session.commit()
        except Exception as e:
            logger.error(f"Error adding repository: {e}", exc_info=True)