from collections import deque
from abc import ABC, abstractmethod

# dict = {'1': ['2a','3a'], '2': ['1b','2b'], '3': ['1c','2c','3c'], '4': ['1e','2e','3e','4e'], '2a': ['1']}
dictExemple = { '1' : ['2','3'], '2' : ['5','6'], '3' : [], '4' : ['4','6'], '5' : ['4'], '6' : ['6', 'a'], 'a' : ['b'], 'b' : ['1']}


class TransitionRelation:
    def __init__(self, dict):
        self.dict = dict

    @abstractmethod
    def initial(self): # Dans la présentation du prof, la méthode initial correspond à sa méthode 'roots'
        #retourne les racines du graphe
        return None

    @abstractmethod
    def getValues(self, source): # Dans la présentation du prof, la méthode getValues correspond à sa méthode 'next'
        return None


class NBits(TransitionRelation):
    def __init__(self, initial, longueur):
        self.initial = initial
        self.longueur = longueur
        self.dict = {initial: []}

    def initial(self):
        return list(self.dict.keys())[0]

    def getValues(self, source):
        res = []
        for i in range(self.longueur):
            res += [flipBit(source, i)]
        return res

    def __str__(self):
        return str(self.dict)

class DictGraphe(TransitionRelation):

    def __init__(self, dict):
        self.dict = dict
        # Le graphe est initialisé avec les noeuds supérieurs du dictionnaire
        self.Nodes = [Node(key) for key in dict.keys()]

    def getValues(self, source):
        return self.dict[source]

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

def flipBit(n, i):
    return n ^ (1 << i)

def bfs(graphe, pred, f_on_entry, f_on_known, f_on_exit):
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
                frontier.append(neighbor)
                if f_on_entry(source, neighbor, acc):# on_entry
                    print('on_entry')
                    return True
            else:
                if f_on_known(source, neighbor, acc):# on_known
                    print('on known')
                    return True
        f_on_exit(source, acc)# on_exit
        print('on exit')

    print('known',known)
    print('pred',[element for element in known if pred(element)])
    return True




if __name__ == '__main__':
    bfs(DictGraphe(dictExemple), valeurPaire, on_entry, on_known, on_exit)

    print('DictGraphe initial',DictGraphe(dictExemple).initial())

    a = NBits(1,3)
    print('a',a)
    print(a.getValues(2))

    bfs(NBits(1,3), valeurPaire, on_entry, on_known, on_exit)

    #fonction pour flip un bit d'un entier n

    print(flipBit(15, 2))







