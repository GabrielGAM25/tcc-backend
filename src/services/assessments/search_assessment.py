from repositories.assessments import SearchAssessmentsRepository


class SearchAssessment:
    def __init__(self, repository=SearchAssessmentsRepository()):
        self.repository = repository

    def get_user_assessments(self, user_id):
        return self.repository.get_user_assessments(user_id)
