from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    email = Column(String, primary_key=True, nullable=False)
    hash = Column(String, unique=False, nullable=False)
    
    


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True, nullable=False)
    id_user =  Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User")
    id_planet = Column(Integer, ForeignKey("planets.id"))
    planets = relationship("Planets")
    id_characters = Column(Integer, ForeignKey("characters.id"))
    characters = relationship("Characters")
    name_planet = Column(String)
    name_characters = Column(String)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True, nullable=False)
    favorites= relationship("Favorites")
    name = Column(String, nullable=False)
    type = Column(String(250))
    description = Column(String(400))
    population = Column(String(250))
    diameter = Column(String(250))
    terrain = Column(String(250))
    url_plant = Column(String(250))


class Characters(Base):
    __tablename__ = 'characters'
    id =  Column(Integer, primary_key=True)
    favorites= relationship("Favorites")
    name = Column(String, nullable=False)
    type = Column(String(250))
    description = Column(String(400))
    species = Column(String(250))
    url_characters = Column(String(250))
    planet_name_origin = Column(String(20))
    


    
def to_dict(self):
    return {}

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
