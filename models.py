from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividade.bd', convert_unicode=True)
Base.metadata.create_all(engine)

# Criação da fábrica de sessão
session_factory = sessionmaker(bind=engine)
db_session = scoped_session(session_factory)

# Associar a propriedade query ao Base
Base =declarative_base()
Base.query = db_session.query_property()

# Exemplo de como usar a sessão
session = db_session()

# Fechar a sessão após o uso
session.close()

class Pessoas(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
