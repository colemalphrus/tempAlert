from src import db


class Rules(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    context = db.Column(db.String(80), nullable=False)
    device_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.context}'
