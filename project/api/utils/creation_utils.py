from database_singleton import Singleton

db = Singleton().database_connection()


class Utils:
    def commit_to_database(self, type, model):
        if type == "A":
            db.session.add(model)
        elif type == "M":
            db.session.merge(model)

        db.session.flush()
        db.session.commit()
