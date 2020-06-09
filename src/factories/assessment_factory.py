from entities import AssessmentEntity


class AssessmentFactory():
    @classmethod
    def from_dictionary(cls, dictionary):
        return AssessmentEntity(
            id_=dictionary['id'],
            user_id=dictionary['user_id'],
            date=dictionary['date'],
            weight=dictionary['weight'],
            fat_percentage=dictionary['fat_percentage'],
            neck=dictionary['neck'],
            shoulder=dictionary['shoulder'],
            torax=dictionary['torax'],
            abdomen=dictionary['abdomen'],
            waist=dictionary['waist'],
            hip=dictionary['hip'],
            left_arm=dictionary['left_arm'],
            right_arm=dictionary['right_arm'],
            left_forearm=dictionary['left_forearm'],
            right_forearm=dictionary['right_forearm'],
            left_thigh=dictionary['left_thigh'],
            right_thigh=dictionary['right_thigh'],
            left_calf=dictionary['left_calf'],
            right_calf=dictionary['right_calf'],
        )

    @classmethod
    def from_model(cls, assessment_model):
        return AssessmentEntity(
            id_=assessment_model.id,
            user_id=assessment_model.user_id,
            date=assessment_model.date,
            weight=assessment_model.weight,
            fat_percentage=assessment_model.fat_percentage,
            neck=assessment_model.neck,
            shoulder=assessment_model.shoulder,
            torax=assessment_model.torax,
            abdomen=assessment_model.abdomen,
            waist=assessment_model.waist,
            hip=assessment_model.hip,
            left_arm=assessment_model.left_arm,
            right_arm=assessment_model.right_arm,
            left_forearm=assessment_model.left_forearm,
            right_forearm=assessment_model.right_forearm,
            left_thigh=assessment_model.left_thigh,
            right_thigh=assessment_model.right_thigh,
            left_calf=assessment_model.left_calf,
            right_calf=assessment_model.right_calf,
        )

    @classmethod
    def from_models(cls, assessment_models):
        return map(cls.from_model, assessment_models)
