from model.assessment import Assessment

class AssessmentsRepository:
    @classmethod
    def get_user_assessments(cls, user_id):
        return Assessment.query.filter_by(user_id=user_id).all()
