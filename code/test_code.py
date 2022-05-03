import networkx as nx
from gcp_ga import *


def parse_line(line): 
    if line.startswith(TYPE_COMMENT):
        return TYPE_COMMENT, None
    elif line.startswith(TYPE_PROBLEM_LINE):
        _, _, num_nodes, num_edges = line.split(' ')
        return TYPE_PROBLEM_LINE, (int(num_nodes), int(num_edges))
    elif line.startswith(TYPE_EDGE_DESCRIPTOR):
        _, node1, node2 = line.split(' ')
        return TYPE_EDGE_DESCRIPTOR, (int(node1), int(node2))
    else:
        raise ValueError(f"Unable to parse '{line}'")


def from_file(filename): #Contruit la matrice d'adjacence à partir des fichiers fournis
        matrice = None
        with open(filename) as f:
            problem_set = False
            for line in f.readlines():
                line_type, val = parse_line(line.strip())
                if line_type == TYPE_COMMENT:
                    continue
                elif line_type == TYPE_PROBLEM_LINE and not problem_set:
                    num_nodes, num_edges = val
                    matrice = [ [0 for _ in range(num_nodes)] for _ in range(num_nodes) ]
                    problem_set = True
                elif line_type == TYPE_EDGE_DESCRIPTOR:
                    if not problem_set:
                        raise RuntimeError("Edge descriptor found before problem line")
                    node1, node2 = val
                    matrice[node1-1][node2-1] = 1
                    matrice[node2-1][node1-1] = 1
        return matrice

def defineGraph(filename):

    """
    graph = nx.Graph()
    add_nodes_from([1, 2, 3, 4])
    add_edges_from([
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 1),
        (2, 3),
        (2, 4),
        (3, 1),
        (3, 2),
        (3, 4),
        (4, 1),
        (4, 2),
        (4, 3)
    ])
    """
    graph = nx.from_numpy_matrix(np.array(from_file(filename)))
    return graph

matrice = [] #Contient la matrice d'adjacence

SUBPLOT_NUM = 211
TYPE_COMMENT = "c"
TYPE_PROBLEM_LINE = "p"
TYPE_EDGE_DESCRIPTOR = "e"


dataset = input("Entrer le nom du dataset: ")
graph = defineGraph(dataset)
print(graph)


lenchromo=len(graph)
popsize=50
generations=100
colors=[0,1,2,3,4,5,6,7]


#L'action principale du programme
i = 0
optimal=[]
bestfit=0
generationslist=[]
bestgeneration=1
while(i != generations):
    i += 1
    x=run()
    generationslist.append(x)
    run_fit=fitness(x)
    if (run_fit>bestfit):
        bestfit=run_fit
        bestgeneration=i
    print(f"generation {i} : {x} -----> fitness is : {fitness(x)}")

print(f"optimal generation is : {bestgeneration} fitness rate is : {bestfit} best chromosome is : {generationslist[bestgeneration-1]}" )


optimalchromo=generationslist[bestgeneration-1]

colors= {
        0:"red",
        1:"blue",
        2:"yellow",
        3:"green",
        4:"orange",
        5:"black",
        6:"magenta",
        7:"white"
    }
color_map=[colors[x] for x in optimalchromo]
print(color_map)
#ploting

g = nx.Graph()
g.add_nodes_from(graph.keys())
for k, v in graph.items():
    g.add_edges_from(([(k, t) for t in v]))

print (nx.info(g))
nx.draw(g,node_color = color_map,with_labels = True)
plt.show()



'''
start = time.time()
coloring, nb_colors = GraphColoring(graph)
end = time.time()
print("Temps d'execution = ", (end-start)*1000," milliseconds")
print(coloring)
print("Le nombre de couleurs utilisé est = ", nb_colors)
#nx.draw_networkx(graph,node_color=coloring, with_labels=True)
nx.draw_circular(graph, font_weight="bold", node_color = coloring, with_labels=True, vmin=0, vmax=max(coloring))
plt.show()
'''