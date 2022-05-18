
# lê arquivo 'edges' e popula grafo implementado com lista de adj


# classe grafo abstrai funcionalidades do grafo e deixa os algoritmos mais legíveis
class Grafo():


    def __init__(self):
        self.grafo_interno = {}
        self.vertices = None
    
    def adiciona_vertice(self , a,b):
        if not (a in self.grafo_interno):
            self.grafo_interno[a] = {'adj' : []}
        if not (b in self.grafo_interno):
            self.grafo_interno[b] = {'adj' : []}
        self.grafo_interno[a]['adj'].append(b)
        self.grafo_interno[b]['adj'].append(a)
    
    def get_vizinhos(self , a):
        return self.grafo_interno[a]['adj']
    
    def get_todos_vertices(self):
        if not self.vertices:
            self.vertices =  list([ x for x in self.grafo_interno ])
        return self.vertices

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

# busca em largura clássica para saber a distância de tds os vértices do grafo até o vértice escolhido
# retorna dicionário com a relação v -> distancia até inicio
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

# calcula farness em O(E^2 + VE), ao executar busca em largura para cada vértice
# e somar, para cada v, a distancia de v aos outros vértices.
# Como a distancia a->b == b->a, é possível diminuir o tempo do algoritmo ao pular do
#  segundo 'for loop' vértices já visitados no primeiro
def calcula_farness(grafo: Grafo):
    farness = { x: 0 for x in grafo.get_todos_vertices() }
    for v_i , v in enumerate(grafo.get_todos_vertices()):
        distancia = busca_largura(grafo , v)
        for u in grafo.get_todos_vertices()[v_i + 1:]:
            farness[v] += distancia[u]
            farness[u] += distancia[u]
    return farness

# ordena vértices com base no oposto de farness
# essa parte pode ser trocada para escrever resultado num .txt ou mandar pela web
for x , d in sorted(calcula_farness(grafo).items() , key=lambda items: -items[1]  ):
    print(x , d)