from entities import ExerciseEntity


class ExerciseFactory():
    @classmethod
    def from_dictionary(cls, dictionary):
        return ExerciseEntity(
            id_=dictionary['id'],
            name=dictionary['name'],
            description=dictionary['description'],
        )

    @classmethod
    def from_model(cls, exercise_model):
        return ExerciseEntity(
            id_=exercise_model.id,
            name=exercise_model.name,
            description=exercise_model.description,
        )

    @classmethod
    def from_models(cls, exercise_models):
        return map(cls.from_model, exercise_models)
