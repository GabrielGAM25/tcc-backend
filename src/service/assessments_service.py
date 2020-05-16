from repository.assessments_repository import AssessmentsRepository


class AssessmentsService:
    @classmethod
    def get_user_assessments(cls, user_id):
        return AssessmentsRepository.get_user_assessments(user_id)
