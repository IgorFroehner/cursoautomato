from flask import Flask
from flask import render_template, redirect
from automato.estudante import Estudante

app = Flask(__name__)

estudantes = {}

@app.route('/')
def index(name=None):
    alunos = ['igor', 'mateus']
    return render_template('index.html', alunos=alunos)

@app.route('/aluno/<nome_aluno>')
@app.route('/aluno/<nome_aluno>/<estado>')
def estado(nome_aluno, estado=None):
    if not nome_aluno in estudantes:
        est = Estudante(nome_aluno, 4)
        estudantes[nome_aluno] = est
    if estado==None or estado=='':
        estudantes[nome_aluno].initializeWeb()
        estado = estudantes[nome_aluno].getEstadoAtual()
    
    # estudantes[nome_aluno].renderizarAutomato()
    return render_template('aluno.html', estudante=estudantes[nome_aluno], estado=estado)

@app.route('/fazer_transicao/<nome_aluno>/<simbolo>')
def fazerTransicao(nome_aluno, simbolo):
    estudantes[nome_aluno].fazerTransicao(simbolo)
    return redirect(f'/aluno/{nome_aluno}/{estudantes[nome_aluno].getEstadoAtual()}')


