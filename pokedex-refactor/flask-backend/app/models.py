from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()




class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    happiness = db.Column(db.Integer)
    image_url = db.Column(db.String(255), nullable=False) #0 is null! FIX IT!
    name = db.Column(db.String(255))
    price = db.Column(db.Integer, nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemon.id"))


class Pokemon(db.Model):
    __tablename__ = "pokemons"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=True) # min 1
    attack = db.Column(db.Integer, nullable=False) # min 0 max 100
    defense = db.Column(db.Integer, nullable=False) # 0 - 100
    image_url = db.Column(db.String, nullable=False) # custom
    name = db.Column(db.String(3,255),nullable=False, unique=True)
    type = db.Column(db.String, nullable=False) # must be from list of types

    @validates("type")
    def validate_name(self, type, pokemons):
        types = ["fire", "electric","normal","ghost", "psychic", "water", "bug", "dragon", "grass", "fighting", "ice", "flying", "poison", "ground", "rock", "steel"]
        if pokemons["type"] not in types:
            raise ValueError("Invalid pokemon type")
        return pokemons
        








# 1 - 1

# class Image(db.Model):
#     __tablename__ = 'image'
#     image_id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(8))
#     # the one-to-one relation
#     blindmap = relationship("Blindmap", uselist=False, backref="image")

# class Blindmap(db.Model):
#     __tablename__ = 'blindmap'
#     module_id = db.Column(db.Integer, primary_key = True)
#     image_id = db.Column(db.Integer, ForeignKey('image.image_id'))


# image1 = Image(name='image1.png')
# blindmap1 = Blindmap()
# blindmap1.image = image1







