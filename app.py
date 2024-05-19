from  flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas

app = Flask(__name__)
api = Api(app)


class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
            'nome':pessoa.nome
            'idade':pessoa.idade,
            'id':pessoa.idade
        }
        except AttributeError:
            response ={
                'status':'error'
                'menssagem':'pessoa não escontrada'
            }

        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return{'nome':'rafael'}

    def delete(self, nome):
        pessoa = Pessoa.query.filter_by(nome=nome).first()
        mensagem = 'Pessoa {} excluida com sucesso'.format(pessoa.nome)
        pessoa.delete()
        return{'status':'sucesso', 'mensagem':mensagem}

class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.id
        }
        return response
api.add_resource(Pessoa, '/pessoa/<string:nome>/')

if __name__ == '__main__'
    app.run(debug=True)