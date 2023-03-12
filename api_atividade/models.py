from sqlalchemy import (create_engine, Column,
                         Integer, String, ForeignKey)
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base


# Criar banco de dados
engine = create_engine('sqlite:///atividades.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                          bind=engine))

# fazer alterações no banco e fazer consultas
Base = declarative_base()
Base.query = db_session.query_property()

# Criar tabelas

class Pessoas(Base):
    __tablename__ = 'pessoas' # nome da tabela == nome da class
    id:int = Column(Integer, primary_key=True)
    nome:str = Column(String(40), index=True) # tamnho do nome e criar um index para consultas, more fast
    idade:int = Column(Integer)

    def __repr__(self) -> str:
        return f'< Pessoa {self.nome} >'
    
    def save(self):
        db_session.add(self) # add a propria instancia
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()



class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id')) # nome da tabela
    pessoa = relationship('Pessoas') # tem uma relação com a classe pessoa


    def __repr__(self) -> str:
        return f'< Pessoa {self.nome} >'
    
    def save(self):
        db_session.add(self) # add a propria instancia
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()



def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
