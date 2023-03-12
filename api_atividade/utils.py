from models import Pessoas



# consultar as tabelas
def insere_pessoas():
    pessoa = Pessoas(nome='Rafale', idade=25)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome="Nicholas").first()
    print(pessoa.nome)
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafale').first()
    pessoa.idade = 28
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafale').first()
    pessoa.delete()


if __name__ ==  '__main__':
    # insere_pessoas()
    # consulta_pessoas()
    # altera_pessoa()
    # consulta_pessoas()
    # exclui_pessoa()
    consulta_pessoas()



