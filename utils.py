from models import Pessoas

def insere_pessoas():
    pessoa =Pessoas(nome='Rafael', idade=29)
    print(pessoa)
    pessoa.save()

def consulta_pessoa():
    pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Galleani').first()
    print(pessoa.idade)

def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.idade = 21
    pessoa.save()

if __name__ == '__main__':
    #consulta_pessoas()
    #insere_pessoas()
    altera_pessoas()