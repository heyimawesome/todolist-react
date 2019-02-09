from project import db


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64), unique=True, nullable=False)

    def __init__(self, title):
        self.title = title


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item = db.Column(db.String(128), unique=True, nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), nullable=False)
    status = db.Column(db.Boolean(), default=False, nullable=False)
