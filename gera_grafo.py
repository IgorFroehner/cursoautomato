
from graphviz import Digraph

gra = Digraph()

gra.node('a', 'Machine Learning Errors')
gra.node('b', 'RMSE')
gra.node('c', 'MAE')

gra.edges(['ab', 'ac'])

gra.render('a.png', view=True)
