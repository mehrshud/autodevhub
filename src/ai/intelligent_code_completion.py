from src.utils.helpers import helpers
from src.types import User, Config, Repository
import logging

class IntelligentCodeCompletion:
    """
    Provides AI-powered intelligent code completion functionality.

    Attributes:
    ----------
    user : User
        The user requesting code completion.
    config : Config
        The application configuration.
    repository : Repository
        The GitHub repository being worked on.
    """

    def __init__(self, user: User, config: Config, repository: Repository):
        """
        Initializes the IntelligentCodeCompletion instance.

        Args:
        ----
        user (User): The user requesting code completion.
        config (Config): The application configuration.
        repository (Repository): The GitHub repository being worked on.
        """
        self.user = user
        self.config = config
        self.repository = repository
        self.logger = logging.getLogger(__name__)

    def complete_code(self, code_snippet: str) -> str:
        """
        Completes the given code snippet using AI-powered suggestions.

        Args:
        ----
        code_snippet (str): The code snippet to complete.

        Returns:
        -------
        str: The completed code snippet.
        """
        try:
            # Use AI model to generate completion suggestions
            suggestions = helpers.generate_suggestions(code_snippet, self.repository.url)
            # Select the most suitable suggestion
            completion = self._select_suggestion(suggestions, code_snippet)
            self.logger.info(f"Completed code snippet for user {self.user.id}")
            return completion
        except Exception as e:
            self.logger.error(f"Error completing code snippet: {e}", exc_info=True)
            return ""

    def _select_suggestion(self, suggestions: list[str], code_snippet: str) -> str:
        """
        Selects the most suitable completion suggestion based on the code snippet.

        Args:
        ----
        suggestions (list[str]): The list of completion suggestions.
        code_snippet (str): The original code snippet.

        Returns:
        -------
        str: The selected completion suggestion.
        """
        # Implement suggestion selection logic here
        # For demonstration purposes, return the first suggestion
        return suggestions[0] if suggestions else ""