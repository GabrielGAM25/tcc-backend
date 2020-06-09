from models import Assessment
from factories import AssessmentFactory


class SearchAssessmentsRepository:
    def __init__(self, factory=AssessmentFactory):
        self.factory = factory or AssessmentFactory

    def get_user_assessments(self, user_id):
        assessments = Assessment.query.filter_by(user_id=user_id).all()
        return self.factory.from_models(assessments)
