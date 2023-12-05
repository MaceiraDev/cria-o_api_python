from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'A Arte da Guerra',
        'autor': 'Sun Tzu'
    },
    {
        'id': 2,
        'titulo': 'Diário de um banana 1',
        'autor': 'Jeff Kinney'
    },
    {
        'id': 3,
        'titulo': 'BLEACH Cap.2',
        'autor': 'Tite Kubo'
    },
]

@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for index,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[index].update(livro_alterado)
            return jsonify(livros[index])

@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for index, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[index]
            return jsonify(livros)
            

app.run(port=5000,host='localhost',debug=True)