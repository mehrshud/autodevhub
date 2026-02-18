from src.utils.helpers import helpers
from src.types import User, Repository

class RealTimeCodeAnalysis:
    def __init__(self, user: User):
        self.user = user

    def analyze_code(self, repository: Repository) -> dict:
        try:
            analysis_results = helpers.analyze_code(repository.url)
            return analysis_results
        except Exception as e:
            print(f"Error analyzing code: {e}")
            return {"error": str(e)}

    def get_analysis_results(self, repository: Repository) -> dict:
        return self.analyze_code(repository)

def main(user: User, repository: Repository) -> dict:
    analyzer = RealTimeCodeAnalysis(user)
    analysis_results = analyzer.get_analysis_results(repository)
    return analysis_results