from src.models import User
from src.database import db
import logging

class CoreService:
    """
    Core service layer for AutoDevHub.
    
    Provides methods for interacting with the database and performing core operations.
    """

    def __init__(self, db: db):
        """
        Initializes the CoreService with a database connection.
        
        Args:
        db (db): The database connection.
        """
        self.db = db
        self.logger = logging.getLogger(__name__)

    def get_user(self, user_id: int) -> User:
        """
        Retrieves a user from the database by ID.
        
        Args:
        user_id (int): The ID of the user to retrieve.
        
        Returns:
        User: The retrieved user, or None if not found.
        """
        try:
            return self.db.query(User).filter(User.id == user_id).one_or_none()
        except Exception as e:
            self.logger.error(f"Error retrieving user: {e}", exc_info=True)
            return None

    def save_user(self, user: User) -> bool:
        """
        Saves a user to the database.
        
        Args:
        user (User): The user to save.
        
        Returns:
        bool: True if the user was saved successfully, False otherwise.
        """
        try:
            self.db.add(user)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            self.logger.error(f"Error saving user: {e}", exc_info=True)
            return False

    def delete_user(self, user_id: int) -> bool:
        """
        Deletes a user from the database by ID.
        
        Args:
        user_id (int): The ID of the user to delete.
        
        Returns:
        bool: True if the user was deleted successfully, False otherwise.
        """
        try:
            user = self.get_user(user_id)
            if user:
                self.db.delete(user)
                self.db.commit()
                return True
            return False
        except Exception as e:
            self.db.rollback()
            self.logger.error(f"Error deleting user: {e}", exc_info=True)
            return False