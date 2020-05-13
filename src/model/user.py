from config.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(30))
    password = db.Column(db.String())
    birth_date = db.Column(db.DateTime)

    def __init__(self, name, email, password, birth_date):
        self.name = name
        self.email = email
        self.password = password
        self.birth_date = birth_date

    def __repr__(self):
        return '<User id:{} email:{}>'.format(self.id, self.email)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birth_date': self.birth_date,
        }
