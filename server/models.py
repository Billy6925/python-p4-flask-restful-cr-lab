from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata= MetaData(naming_convention={
    "fk":"fk_%(table_name)s_%(column_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    image= db.Column(db.String)
    price= db.Column(db.Float)

    def to_dict(self):
        return {
            "id":self.id,
            "name": self.name,
            "image":self.image,
            "price":self.price
        }

    def __repr__(self):
        return f'<Plant {self.id},{self.name},{self.image},{self.price}>'

