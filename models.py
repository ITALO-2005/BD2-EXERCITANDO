from sqlalchemy import (
    create_engine, Column, Integer, String, Date, ForeignKey
)
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class Autor(Base):
    __tablename__ = 'autores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)

class Livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    autor_id = Column(Integer, ForeignKey('autores.id'), nullable=False)

