from flask import Flask
from flask import render_template, redirect, send_from_directory, request
from automato.estudante import Estudante
import os

app = Flask(__name__)

estudantes = {}
alunos = ['igor', 'matheus']

@app.route('/')
def index(name=None):
    return render_template('index.html', alunos=alunos)


@app.route('/aluno/<nome_aluno>')
def estado(nome_aluno):
    if not nome_aluno in estudantes:
        est = Estudante(nome_aluno, 4)
        estudantes[nome_aluno] = est
        estudantes[nome_aluno].initializeWeb()
    if not nome_aluno in alunos:
        alunos.append(nome_aluno)
    
    estudantes[nome_aluno].renderizarAutomato()
    return render_template('aluno.html', estudante=estudantes[nome_aluno])


@app.route('/fazer_transicao/<nome_aluno>/<simbolo>')
def fazer_transicao(nome_aluno, simbolo):
    estudantes[nome_aluno].fazerTransicao(simbolo)
    return redirect(f'/aluno/{nome_aluno}')


@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory(os.getcwd()+'/images/', filename, as_attachment=True)


@app.route('/adicionar_conteudo/<nome_aluno>', methods=['GET', 'POST'])
def adicionar_conteudo(nome_aluno):
    if request.method == 'POST':
        req = request.form
        links = req['links'].replace('\n', '').split('\r')
        estudantes[nome_aluno].add_conteudo_customizado(links)
        return redirect(f'/aluno/{nome_aluno}')
    return render_template('conteudo_adicional.html', nome_aluno=nome_aluno)

@app.route('/finalizar/<nome_aluno>')
def finalizar(nome_aluno):
    if nome_aluno in estudantes:
        estudantes.pop(nome_aluno)
    return redirect(f'/')

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r