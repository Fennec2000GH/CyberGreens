
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import create_engine, relationship, sessionmaker

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

url = 'postgresql://root@localhost:26257?sslmode=disable'
engine = create_engine(url=url)
Session = sessionmake(bind=engine)
session = Session()

class Specimen(Base):
"""[summary]
"""__tablename__ = 'specimen'
	id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
	species = Column(String, unique=True, nullable=False)
	variant = Column(String, nullable=True)
	days_to_maturity = Column(Integer, nullable=False)
	sunlight = Column(String, nullable=False)
	water = Column(String, nullable=False)
	resistance = Column(String, nullable=True)
	toxicity = Column(String, nullable=True)

	def __repr__(self):
		return f'<Specimen(id = {self.id}, species = {self.species})>'

Base.metadata.create_all(engine)

specimen1 = Specimen(species=)

session.add(species1)
session.commit()
session.flush()
session.close()