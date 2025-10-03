#Escreva o código Python usando SQLAlchemy para mapear uma tabela produtos. A tabela deve ter os seguintes campos:
#id: Inteiro, chave primária.
#nome: String de até 100 caracteres, não pode ser nulo.
#preco: Numérico com 10 dígitos no total e 2 casas decimais.
#em_estoque: Booleano, com valor padrão True.

from sqlalchemy import (
    create_engine, Column, Integer, String, Date, ForeignKey
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class curso
