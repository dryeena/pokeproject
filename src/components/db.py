from sqlalchemy import Integer, String, Text, Date, Column, func, create_engine, ForeignKey
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base
import os

dbname='pokedb'
connection=os.environ.get('POSTGRES_CONNECTION','localhost:5555')
username=os.environ.get('POSTGRES_USER','pokedb_user')
dbname=os.environ.get('POSTGRES_DB','pokedb')
password=os.environ.get('POSTGRES_PASSWORD','pokedb_user_password')

class DBConnection():
    def __init__(self, dbname=dbname):
        self.dbName=dbname
        self.configure()

    def pullNames(self):
        results=self.session.query(Names).all()
        return results
    
    def insertOneAtDate(self, id, date: Date):
        hits=self.session.query(Counts)\
            .where(Counts.pokemon_id==id, Counts.date==date)
        if(hits.count() > 0):
            count = hits.first()
            self.session.query(Counts) \
                .filter(Counts.id==count.id)\
                .update({Counts.hits: Counts.hits + 1})
        else:
            count=Counts(pokemon_id=id, date=date, hits=1)
            self.session.add(count)
        self.session.commit()
        return count
    
    def getById(self, id):
        poke=self.session.query(Pokemon).get(id)            
        return poke
    def findAll(self, search):
        pokelist=self.session.query(Pokemon) \
            .join(Names) \
            .where(Names.name.ilike("%"+search+"%")) \
            .add_columns(Names.name, Names.lang) \
            .all()
        print(pokelist)
        return pokelist
    def getRandom(self):
        poke=self.session.query(Pokemon) \
            .order_by(func.random()).first()    
        return poke
    
    def getDateChamps(self, date: Date):
        champs=self.session.query(Pokemon) \
            .join(Counts) \
            .add_columns(
                Counts.hits
                ) \
            .where(Counts.date==date) \
            .order_by(Counts.hits.desc()).limit(7).all()
        return champs
            

 
    def findByName(self, search):
        name=self.session.query(Names) \
            .where(Names.name.ilike(search)) \
            .join(Pokemon).add_columns(
                Names.name,
                Names.id,
                Names.pokemon_id,
                Pokemon.image).first()
        return name        
    def getConn(self):
        return self.session
    
    def configure(self):
        engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{connection}/{self.dbName}')
        self.session = Session(engine)
        self.session.connection()


Base = declarative_base()

class Pokemon(Base):
    __tablename__ = 'pokemon'
    id = Column(Integer, primary_key=True)
    image = Column(String(255))
    description = Column(Text)

    names = relationship("Names")
    counts = relationship("Counts")
    

class Names(Base):
    __tablename__ = 'pokename'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    lang = Column(String(25))


    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))

class Counts(Base):
    __tablename__ = 'pokeapp'
    id = Column(Integer, primary_key=True)
    hits = Column(Integer)
    date = Column(Date)

    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))