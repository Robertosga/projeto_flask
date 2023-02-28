from flask import Flask,render_template,request
import pyodbc
from banco import*

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compra')
def compra():
    return render_template('compra.html')

@app.route('/aula')
def aula():
    return render_template('aula.html')

@app.route('/login', methods=['GET','POST'])
def login():
    variavel='COLABORADORES'

    if request.method == 'GET':
      return render_template('login.html',variavel1=variavel)
    else:
     username = request.form.get('username')
     password = request.form.get('password')

        # Adicione sua lógica de autenticação aqui
    
    if username == usuario and password == senha or username == usuario1 and password == senha1 :
      return render_template('usuario.html')
    else:
      return render_template('negado.html')

@app.route('/<string:nome>')
def error(nome):
    variavel= f'Página ({nome}) Não Existe'
    return render_template("error.html",variavel2=variavel)


app.run(debug=True)