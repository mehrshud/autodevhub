from typing import Optional
import logging
import os
from src.models import User
from src.types import Repository

class Config:
    """
    Configuration settings for the application.

    Attributes:
        debug (bool): Debug mode flag.
        db_url (str): Database URL.
    """
    def __init__(self, debug: bool = False, db_url: str = "") -> None:
        """
        Initializes the Config instance.

        Args:
            debug (bool): Debug mode flag. Defaults to False.
            db_url (str): Database URL. Defaults to an empty string.
        """
        self.debug: bool = debug
        self.db_url: str = db_url

    def get_config(self) -> dict:
        """
        Returns the configuration settings as a dictionary.

        Returns:
            dict: Configuration settings.
        """
        return {
            "debug": self.debug,
            "db_url": self.db_url
        }

    @staticmethod
    def load_config(config_file: str = "config.json") -> Optional['Config']:
        """
        Loads the configuration settings from a file.

        Args:
            config_file (str): Path to the configuration file. Defaults to "config.json".

        Returns:
            Optional[Config]: The loaded Config instance, or None if failed.
        """
        try:
            # Assuming the configuration file is in JSON format
            import json
            if os.path.isfile(config_file):
                with open(config_file, 'r') as file:
                    config_data: dict = json.load(file)
                    return Config(debug=config_data.get("debug", False), db_url=config_data.get("db_url", ""))
            else:
                logging.error(f"Configuration file '{config_file}' not found.")
                return None
        except Exception as e:
            logging.error(f"Failed to load configuration: {e}")
            return None

def get_config() -> Config:
    """
    Returns the default Config instance.

    Returns:
        Config: The default Config instance.
    """
    return Config(debug=True, db_url=os.getenv("DATABASE_URL", "localhost:5432"))