from flask import Flask

app = Flask(__name__)

app.config['TESTING'] = True

@app.route("/",methods=['GET'])
def name():
    return 'Listado com sucesso'

@app.route("/post",methods=['POST'])
def postNome():
    return('postado com sucesso')


@app.route("/put",methods=['PUT'])
def putNome():
    return str(84/2)


@app.route("/delete",methods=['DELETE'])
def deleteNome():
    return('Este item foi deletado')

@app.route('/ <Id>', methods=['GET'])
def identificador(id):
    return {'id'}

