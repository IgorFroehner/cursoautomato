from flask import Flask
from flask import render_template, redirect, send_from_directory
from automato.estudante import Estudante
import os

app = Flask(__name__)

estudantes = {}

@app.route('/')
def index(name=None):
    alunos = ['igor', 'mateus']
    for k in estudantes:
        estudantes[k].initializeWeb()
    return render_template('index.html', alunos=alunos)

@app.route('/aluno/<nome_aluno>')
def estado(nome_aluno, estado=None):
    if not nome_aluno in estudantes:
        est = Estudante(nome_aluno, 4)
        estudantes[nome_aluno] = est
        estudantes[nome_aluno].initializeWeb()
    
    estudantes[nome_aluno].renderizarAutomato()
    return render_template('aluno.html', estudante=estudantes[nome_aluno])

@app.route('/fazer_transicao/<nome_aluno>/<simbolo>')
def fazerTransicao(nome_aluno, simbolo):
    estudantes[nome_aluno].fazerTransicao(simbolo)
    return redirect(f'/aluno/{nome_aluno}')


@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory(os.getcwd()+'/images/', filename, as_attachment=True)


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