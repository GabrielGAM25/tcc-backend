from entities import UserEntity


class UserFactory():
    @classmethod
    def from_dictionary(cls, dictionary):
        return UserEntity(
            id_=dictionary['id'],
            name=dictionary['name'],
            email=dictionary['email'],
            password=dictionary['password'],
            birth_date=dictionary['birth_date'],
        )

    @classmethod
    def from_model(cls, user_model):
        return UserEntity(
            id_=user_model.id,
            name=user_model.name,
            email=user_model.email,
            encrypted_password=user_model.password,
            birth_date=user_model.birth_date,
        )

    @classmethod
    def from_models(cls, user_models):
        return map(cls.from_model, user_models)
