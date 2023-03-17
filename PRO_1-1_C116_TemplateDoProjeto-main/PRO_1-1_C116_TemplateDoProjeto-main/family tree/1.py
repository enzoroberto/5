# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "enzo" # escreva seu nome
    idade = "14" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/2")
def A():
    nome = "pietro"
    idade = "6"

    return render_template('amigo.html', nome = nome, idade = idade)

# defina a rota para a página da mãe
@app.route("/3")
def B():
    nome = "débora"
    idade = "36"

    return render_template('mae.html', nome = nome, idade = idade)

# defina a rota para a página do amigo
@app.route("/4")
def C():
    nome = "Osvaldo"
    idade = "65"

    return render_template('pai.html', nome = nome, idade = idade)

# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
