from project.api.models import db


class Database:
    def add_to_database(self, type: str, model) -> None:
        if type == "A":
            db.session.add(model)
        elif type == "M":
            db.session.merge(model)
        elif type == "D":
            db.session.delete(model)

    def commit_to_database(self) -> None:
        db.session.flush()
        db.session.commit()

    def rollback_database(self) -> None:
        db.session.rollback()
