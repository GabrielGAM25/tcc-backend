class ExerciseEntity():
    def __init__(self, name, description, id_=None):
        self.id = id_
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<Exercise id:{self.id} name:{self.name}>'

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }

    def to_dictionary(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }
