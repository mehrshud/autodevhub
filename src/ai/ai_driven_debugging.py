from src.utils.helpers import helpers
from src.types import User
import logging

class AiDrivenDebugging:
    def __init__(self, user: User, repository: 'Repository') -> None:
        self.user = user
        self.repository = repository

    def detect_issues(self) -> list:
        try:
            issues = helpers.detect_issues(self.repository.url)
            logging.info(f"Detected {len(issues)} issues in the repository.")
            return issues
        except Exception as e:
            logging.error(f"Error detecting issues: {e}")
            return []

    def suggest_fixes(self, issues: list) -> list:
        try:
            fixes = helpers.suggest_fixes(issues)
            logging.info(f"Suggested {len(fixes)} fixes for the issues.")
            return fixes
        except Exception as e:
            logging.error(f"Error suggesting fixes: {e}")
            return []