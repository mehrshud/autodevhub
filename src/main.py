from src.models import User
from src.config import Config
from src.services.core import init_services
from src.ai.agent import Agent
from src.database import db
from src.utils.helpers import helpers
from src.types import Repository

import logging

def main() -> None:
    try:
        # Initialize logging
        logging.basicConfig(level=logging.INFO)
        
        # Initialize configuration
        config: Config = Config(debug=True, db_url="sqlite:///example.db")
        
        # Initialize database
        db.init_app(config.db_url)
        
        # Initialize services
        init_services()
        
        # Create a new user
        user: User = User(id=1, name="John Doe", email="john@example.com")
        
        # Create a new repository
        repository: Repository = Repository(id=1, name="AutoDevHub", url="https://github.com/user/repo")
        
        # Initialize AI agent
        agent: Agent = Agent(user, repository)
        
        # Start the AI agent
        agent.start()
        
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()