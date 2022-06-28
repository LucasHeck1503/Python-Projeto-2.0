from flask import Flask, render_template
app = Flask(__name__) #instanciando classe flask 

#endereço do site
@app.route('/') #rota principal
@app.route('/index') #rota alternativa
def index():
    #return"Hello World"
    nome = 'Lucas Heck'
    dados = {"profissão":"SRE","cidade":"Santa Rosa"} #variavel lista
    return render_template('index.html',nome = nome, dados = dados)