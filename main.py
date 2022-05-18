
# lê arquivo 'edges' e popula grafo implementado com lista de adj

from copyreg import constructor

class Grafo():

    def __init__(self):
        self.grafo_interno = {}
        self.vertices = None
    
    def adiciona_vertice(self , a,b):
        if not (a in self.grafo_interno):
            self.grafo_interno[a] = {'adj' : []}
        self.grafo_interno[a]['adj'].append(b)
    
    def get_vizinhos(self , a):
        return self.grafo_interno[a]['adj']
    
    def get_todos_vertices(self):
        if not self.vertices:
            self.vertices =  list([ x for x in self.grafo_interno ])
        return self.vertices

    # def set_cor_vertice(self , vertice , cor):
    #     self.grafo_interno[vertice]['cor'] = cor
    
    # def get_cor_vertice(self, vertice ):
    #     return self.grafo_interno[vertice]['cor']
    
    # def reset_grafo(self):
    #     for vertice in self.grafo_interno:
    #         self.set_cor_vertice(vertice, None)
    
    def add_distancia(self, vertice, distancia):
        self.grafo_interno[vertice]['dist'] = distancia
    
    def __str__(self):
        result = ''
        for vertice in self.grafo_interno:
            result += vertice + ":" + ",".join(self.grafo_interno[vertice]['adj']) + '\n'
        return result

grafo = Grafo()

with open('edges') as f:
    for line in f:
        a,b = line.split()
        grafo.adiciona_vertice(a,b)

def busca_largura(grafo: Grafo, inicio):
    distancia = {}
    cor = {}
    for v in grafo.get_todos_vertices():
        cor[v] = 'branco'
    cor[inicio] = 'cinza'
    distancia[inicio] = 0
    fila = [inicio]
    while len(fila):
        u = fila.pop(0)
        for v in grafo.get_vizinhos(u):
            if cor[v] == 'branco':
                cor[v] = 'cinza'
                distancia[v] = distancia[u] + 1
                fila.append(v)
        cor[u] = 'preto'
    return distancia

def calcula_farness(grafo: Grafo):
    farness = { x: 0 for x in grafo.get_todos_vertices() }
    for v_i , v in enumerate(grafo.get_todos_vertices()):
        distancia = busca_largura(grafo , v)
        for u in grafo.get_todos_vertices()[v_i + 1:]:
            farness[v] += distancia[u]
            farness[u] += distancia[u]
    return farness

for x , d in sorted(calcula_farness(grafo).items() , key=lambda items: -items[1]  ):
    print(x , 1/d)