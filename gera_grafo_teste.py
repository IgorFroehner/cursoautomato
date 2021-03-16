from graphviz import Digraph

f = Digraph('finite_state_machine', filename='fsm.gv', format="png")
f.attr(rankdir='LR', size='8,5')

f.attr('node', shape='none')
f.node('qi')

f.attr('node', shape='doublecircle')
f.node('K')

f.attr('node', shape='circle')
f.edge('qi', 'N0')
f.edge('N0', 'N1', label='(a1, c11), (a1, c12)')
f.edge('N0', 'N2', label='(a2, c21), (a2, c22)')
f.edge('N1', 'N0', label='(ret, ε)')
f.edge('N1', 'N1', label='(a1, c11), (a1, c12)')
f.edge('N1', 'N2', label='(a2, c21), (a2, c22)')
f.edge('N2', 'N2', label='(a2, c21), (a2, c22)')
f.edge('N2', 'N1', label='(a1, c11), (a1, c12)')
f.edge('N2', 'N0', label='(ret, ε)')
f.edge('N1', 'K', label='(fim, ε)')
f.edge('N2', 'K', label='(fim, ε)')
f.edge('N0', 'K', label='(fim, ε)')

f.view()
