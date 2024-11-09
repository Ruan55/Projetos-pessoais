from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from config.connection import db

Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Tarefas(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(250))
    data = Column(String(250))

    def __init__(self, nome: str, data: str) -> None:
        self.nome = nome
        self.data = data

Base.metadata.create_all(bind=db)