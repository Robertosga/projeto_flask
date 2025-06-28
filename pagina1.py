from flask import Flask,render_template,request,redirect, url_for
#from banco import*
import conexao_bd
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compra')
def compra():
    return render_template('compra.html')


@app.route('/webs')
def webs():
    return render_template('webs.html')

@app.route('/ia')
def ia():
    return 'ia.py'


@app.route('/aula')
def aula():
    return render_template('aula.html')


@app.route('/texto1.html')
def texto1():
    return render_template('texto1.html')


@app.route('/login', methods=['GET','POST'])

def login():
 
    conexao_bd.ConexaoBanco()

    variavel='COLABORADORES'

    if request.method == 'GET':
      return render_template('login.html',variavel1=variavel)
    else:
     username = request.form.get('username')
     password = request.form.get('password')

    # Adicione sua lógica de autenticação aqui

    banco = sqlite3.connect('elabore.db')

    cursor = banco.cursor()
 
    consulta = "SELECT * FROM user WHERE usuario = ? AND senha = ?"
    cursor.execute(consulta, (username, password))

    # Use fetchone() para pegar o primeiro resultado da consulta.
    registro = cursor.fetchone()

    
    if registro:
      return render_template('usuario.html')
    else:
      return render_template('negado.html')

@app.route('/<string:nome>')
def error(nome):
    variavel= f'Página ({nome}) Não Existe'
    return render_template("error.html",variavel2=variavel)


@app.route('/cadastro', methods=['GET','POST'])

def cadastro():
 
    conexao_bd.ConexaoBanco()

    variavel='CADASTRO'

    if request.method == 'GET':
      return render_template('cadastro.html',variavel1=variavel)
    else:
     usuario = request.form.get('username')
     senha = request.form.get('password')


    # Adicione sua lógica de autenticação aqui

    banco = sqlite3.connect('elabore.db')

    cursor = banco.cursor()
 
    consulta = "SELECT * FROM user WHERE usuario = ?"
    cursor.execute(consulta, (usuario,))

    # Use fetchone() para pegar o primeiro resultado da consulta.
    registro = cursor.fetchone()

    
    if registro:
      return '<script>alert("Usuário não disponível"); window.location.href="/cadastro";</script>'
    else:
                 
      cursor.execute("INSERT INTO user (usuario, senha) VALUES (?, ?)", (usuario, senha))

      banco.commit()
      
      return '<script>alert("Cadastro realizado com sucesso"); window.location.href="/login";</script>'

app.run(debug=True)
