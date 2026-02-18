from src.models import User, Repository
from src.config import Config
from src.database import db
from src.api.github import GitHubAPI
from src.types import User as UserType
from src.utils.helpers import helpers
import logging

class AutoDevHubService:
    def __init__(self, config: Config):
        self.config = config
        self.github_api = GitHubAPI()
        self.logger = logging.getLogger(__name__)

    def get_repositories(self, user: User) -> List[Repository]:
        try:
            repositories = self.github_api.get_repositories(user)
            return repositories
        except Exception as e:
            self.logger.error(f"Failed to retrieve repositories: {str(e)}")
            return []

    def analyze_repository(self, repository: Repository) -> dict:
        try:
            analysis_results = helpers.analyze_repository(repository)
            return analysis_results
        except Exception as e:
            self.logger.error(f"Failed to analyze repository: {str(e)}")
            return {}

    def debug_repository(self, repository: Repository) -> dict:
        try:
            debugging_results = helpers.debug_repository(repository)
            return debugging_results
        except Exception as e:
            self.logger.error(f"Failed to debug repository: {str(e)}")
            return {}

def main():
    config = Config(debug=True, db_url="localhost")
    service = AutoDevHubService(config)
    user = User(id=1, name="John Doe", email="john@example.com")
    repositories = service.get_repositories(user)
    for repository in repositories:
        analysis_results = service.analyze_repository(repository)
        debugging_results = service.debug_repository(repository)
        print(f"Repository: {repository.name}, Analysis Results: {analysis_results}, Debugging Results: {debugging_results}")

if __name__ == "__main__":
    main()