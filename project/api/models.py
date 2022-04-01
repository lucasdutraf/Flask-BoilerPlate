from database_singleton import Singleton

db = Singleton().database_connection()


class Example(db.Model):
    __tablename__ = "Example"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    example = db.Column(db.String(255), nullable=False)

    def __init__(self, example):
        self.example = example

    def to_json(self):
        return {
            "id": self.id,
            "example": self.example,
        }
