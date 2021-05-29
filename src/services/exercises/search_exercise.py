from repositories.exercises import SearchExercisesRepository


class SearchExercise:
    def __init__(self, repository=SearchExercisesRepository()):
        self.repository = repository

    def get_exercises(self):
        return self.repository.get_exercises()
