from models.abstract_model import Model, db, ma
class MenuModel(Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return '<Menu %s>' % self.name

class MenuSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")