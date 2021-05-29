from models import Exercise
from factories import ExerciseFactory


class SearchExercisesRepository:
    def __init__(self, factory=ExerciseFactory):
        self.factory = factory or ExerciseFactory

    def get_exercises(self):
        exercises = Exercise.query.all()
        return self.factory.from_models(exercises)
