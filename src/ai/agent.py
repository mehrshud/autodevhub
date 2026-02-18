from src.utils.helpers import helpers
from src.types import User

import logging

class AIAgent:
    """
    AI agent for AutoDevHub.

    This class provides the core functionality of the AI-powered automated development environment.
    It utilizes the helpers module for utility functions and the User type for user data.
    """

    def __init__(self, user: User) -> None:
        """
        Initializes the AI agent.

        Args:
        user (User): The user instance.
        """
        self.user = user
        logging.info(f"AI agent initialized for user {user.id}")

    def analyze_code(self, code: str) -> str:
        """
        Analyzes the given code using AI-powered tools.

        Args:
        code (str): The code to analyze.

        Returns:
        str: The analysis result.

        Raises:
            AICodeAnalysisError: If an error occurs during analysis.
        """
        try:
            # Utilize the helpers module for code analysis
            analysis_result = helpers.analyze_code(code)
            logging.info(f"Code analysis completed for user {self.user.id}")
            return analysis_result
        except Exception as e:
            logging.error(f"Error occurred during code analysis: {str(e)}")
            raise AICodeAnalysisError("Code analysis failed")

    def provide_recommendations(self, repository: object) -> list:
        """
        Provides AI-driven recommendations for the given repository.

        Args:
        repository (object): The repository instance.

        Returns:
        list: A list of recommendations.

        Raises:
            AIRecommendationGenerationError: If an error occurs during recommendation generation.
        """
        try:
            # Utilize the helpers module for recommendation generation
            recommendations = helpers.generate_recommendations(repository)
            logging.info(f"Recommendations generated for user {self.user.id}")
            return recommendations
        except Exception as e:
            logging.error(f"Error occurred during recommendation generation: {str(e)}")
            raise AIRecommendationGenerationError("Recommendation generation failed")

class AICodeAnalysisError(Exception):
    """Raised when an error occurs during code analysis."""
    pass

class AIRecommendationGenerationError(Exception):
    """Raised when an error occurs during recommendation generation."""
    pass