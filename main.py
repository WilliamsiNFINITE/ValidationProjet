from collections import deque


dict = {'1': ['2a','3a'], '2': ['1b','2b'], '3': ['1c','2c','3c'], '4': ['1e','2e','3e','4e'], '2a': ['1']}
dictExemple = { '1' : ['2','3'], '2' : ['5','6'], '3' : [], '4' : ['4','6'], '5' : ['4'], '6' : ['6', 'a'], 'a' : ['b'], 'b' : ['1']}

class Graphe:
    def __init__(self, dict):
        self.dict = dict
        # Le graphe est initialisé avec les noeuds supérieurs du dictionnaire
        # self.Nodes = [Node(key) for key in dict.keys()]

    def getValues(self, key):
        return self.dict[key]

    def initial(self):
        return list(self.dict.keys())[0]

    def __str__(self):
        return str([str(node) for node in self.Nodes])

class Node:
    def __init__(self, nom):
        self.nom = nom
        self.parent = []
        self.enfant = []

    def add_parent(self, parent):
        self.parent.append(parent)

    def add_enfant(self, enfant):
        self.enfant.append(enfant)

    def __str__(self):
        return 'Node : '+self.nom + ' Parent : ' + self.enfant.__str__() + ' Enfant :' + self.parent.__str__()

#methode pour effectuer le parcours en largeur d'un dictionnaire donné en paramètre
# def bfs(graphe):
#     known = set()# set est utilisé pour ne pas avoir de duplication
#     frontier = deque() #dequeu est utilisé pour avoir une file, on peut aussi utiliser une liste circulaire
#     at_start = True
#
#     while((len(frontier) != 0) or at_start):
#         source = None
#         if at_start:
#             neighbors = graphe.initial()
#             at_start = False
#         else:
#             source = frontier.popleft()
#             # print('source : ', source)
#             neighbors = graphe.getValues(source)
#             # print('neighbors : ', neighbors)
#         for neighbor in neighbors:
#             # print('neighbor : ', neighbor)
#             if neighbor not in known:
#                 known.add(neighbor)
#                 frontier.append(neighbor)
#     return known


#Utilisé pour parcourir le graphe depuis un noeud donné
# def bfs(graphe, noeud, param):
#     known = set()# set est utilisé pour ne pas avoir de duplication
#     frontier = deque() #dequeu est utilisé pour avoir une file, on peut aussi utiliser une liste circulaire
#     at_start = True
#
#     while((len(frontier) != 0) or at_start):
#         source = None
#         if at_start:
#             neighbors = graphe.getValues(noeud)
#             at_start = False
#         else:
#             source = frontier.popleft()
#             # print('source : ', source)
#             neighbors = graphe.getValues(source)
#             # print('neighbors : ', neighbors)
#         for neighbor in neighbors:
#             # print('neighbor : ', neighbor)
#             if neighbor not in known:
#                 known.add(neighbor)
#                 frontier.append(neighbor)
#     return known

#
# def bfs(graphe, target):
#     known = set()# set est utilisé pour ne pas avoir de duplication
#     frontier = deque() #dequeu est utilisé pour avoir une file, on peut aussi utiliser une liste circulaire
#     at_start = True
#
#     while((len(frontier) != 0) or at_start):
#         source = None
#         if at_start:
#             neighbors = graphe.initial()
#             at_start = False
#         else:
#             source = frontier.popleft()
#             # print('source : ', source)
#             neighbors = graphe.getValues(source)
#             # print('neighbors : ', neighbors)
#         for neighbor in neighbors:
#             # print('neighbor : ', neighbor)
#             if neighbor not in known:
#                 known.add(neighbor)
#                 frontier.append(neighbor)
#     print('know',known)
#     return target in known


def valeurPaire(neighbor):
    #check parity of neighbor
    x = 0
    try:
        x = int(neighbor)
    except ValueError:
        return False

    if x%2==0:
        return True

    return False

def defaultFunction():
    return False

def on_entry(source, neighbor, acc):

    return False


def on_known(source, neighbor, acc):

    return False

def on_exit(neighbor, acc):

    return False


def bfs(graphe, pred, f1, f2, f3):
    #on a trois différents états booleen: on_entry(source,neihbor,accumulateur) (je viens d'entrer dans l'état), on_exit(n,a) (je viens de sortir de l'état) et on_known(s,n,a) (je suis dans l'état)
    known = set()# set est utilisé pour ne pas avoir de duplication
    frontier = deque() #dequeu est utilisé pour avoir une file, on peut aussi utiliser une liste circulaire
    at_start = True

    while((len(frontier) != 0) or at_start):
        acc = None
        source = None
        if at_start:
            neighbors = graphe.initial()
            at_start = False
        else:
            source = frontier.popleft()
            neighbors = graphe.getValues(source)
        for neighbor in neighbors:
            if neighbor not in known:
                known.add(neighbor)
                f2(source, neighbor, acc)# on_known
                frontier.append(neighbor)
                f1(source, neighbor, acc)# on_entry

        f3(neighbor, acc)# on_exit


    print('known',known)
    print('pred',[element for element in known if pred(element)])
    return True

# def bfsOld(dict, noeud):
#     graphe = Graphe(dict)
#
#     listeNoeudConnu = []
#     listeNoeudConnu.append(noeud)
#
#     for key, value in dict.items():
#         if key not in listeNoeudConnu:
#             listeNoeudConnu.append(key)
#             for i in value:
#                 if i not in listeNoeudConnu:
#                     listeNoeudConnu.append(i)
#
#
#
#     print('listeNoeudConnu : ', listeNoeudConnu)
#
#     # print('graphe',graphe)

def bfsOldOld(dict, noeud):

    visited = []
    queue = deque()
    queue.append(noeud)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            unvisited = [n for n in dict[node] if n not in visited]
            queue.extend(unvisited)

    return visited

if __name__ == '__main__':
    bfs(Graphe(dictExemple), valeurPaire, on_entry, on_known, on_exit)
