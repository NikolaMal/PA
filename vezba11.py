import math

class Vertex:
    def __init__(self, data = None,data2 = None, ins=None,outs = None, parent = None):
        self.data2 = data2
        self.data = data
        self.ins = ins
        self.outs = outs
        self.parent = parent



class Edge:
    def __init__(self, source = None, destination = None, weight = None):
        self.source = source
        self.destination = destination
        self.weight = weight

def initialize_single_source(G, s):
    for vertex in G:
        vertex.data2 = math.inf
        vertex.parent = Vertex(data = 'Nothing')
    s.data2 = 0


def relax(u, v, w):
    if v.data2 > (u.data2 + w(u, v)):
        v.data2 = u.data2 + w(u, v)
        v.parent = u


def w(u, v):
    for i in u.outs:
        if i.destination == v:
            temp = i
    return temp.weight

def Bellman_Ford(G, w, s):
    initialize_single_source(G, s)
    for i in range(0, len(G)):
        for vertex in G:
            for edge in vertex.outs:
                relax(edge.source, edge.destination, w)
    for vertex in G:
        for edge in vertex.outs:
            if edge.destination.data2 > edge.source.data2 + w(edge.source, edge.destination):
                return 0
        return 1

def UpdateEdge(G, A, B, wei):
    exists = 0
    existing_edge = None
    for item in A.outs:
        if item.destination == B:
            exists = 1
            existing_edge = item
            break

    if exists == 0:
        temp = Edge(source=A, destination=B, weight=wei)
        A.outs.append(temp)
        B.ins.append(temp)
    else:
        existing_edge.weight = wei


def ShortestPath(G, A, B ):
    Bellman_Ford(G, w, A)
    list = []
    weight = B.data2
    par = B.parent
    list.append(B)
    while par != A:
        list.append(par)
        par = par.parent

    list.append(A)
    list = list[::-1]
    return list, weight

def NewShortestPath():
    global graf
    list, weight=ShortestPath(graf, graf[0], graf[6])
    return list, weight


def MakeGraph():
    a = Vertex(data = 'a', ins=[], outs=[])
    b = Vertex(data='b',ins=[], outs=[])
    c = Vertex(data='c', ins=[], outs=[])
    d = Vertex(data='d',ins=[], outs=[])
    e = Vertex(data='e', ins=[], outs=[])
    f = Vertex(data='f', ins=[], outs=[])
    g = Vertex(data='g', ins=[], outs=[])

    ab = Edge(source=a, destination=b, weight=8)
    a.outs.append(ab)
    b.ins.append(ab)
    ac = Edge(source=a, destination=c, weight=6)
    a.outs.append(ac)
    c.ins.append(ac)
    bd = Edge(source=b, destination=d, weight=10)
    b.outs.append(bd)
    d.ins.append(bd)
    cd = Edge(source=c, destination=d, weight=15)
    c.outs.append(cd)
    d.ins.append(cd)
    ce = Edge(source=c, destination=e, weight=9)
    c.outs.append(ce)
    e.ins.append(ce)
    de = Edge(source=d, destination=e, weight=14)
    d.outs.append(de)
    e.ins.append(de)
    df = Edge(source=d, destination=f, weight=4)
    d.outs.append(df)
    f.ins.append(df)
    ef = Edge(source=e, destination=f, weight=13)
    e.outs.append(ef)
    f.ins.append(ef)
    eg = Edge(source=e, destination=g, weight=17)
    e.outs.append(eg)
    g.ins.append(eg)
    fg = Edge(source=f, destination=g, weight=7)
    f.outs.append(fg)
    g.ins.append(fg)

    list = [a,b,c,d,e,f,g]
    return list

def GetInDegrees(G):
    list = []
    for item in G:
        list.append(len(item.ins))

    return list

def GetOutDegrees(G):
    list = []
    for item in G:
        list.append(len(item.outs))

    return list


graf = MakeGraph()
for item in graf:
    print(item.data)
inDegrees = GetInDegrees(graf)
outDegrees = GetOutDegrees(graf)
print()
print(inDegrees)
print(outDegrees)
print()
someList, someWeight = ShortestPath(graf, graf[0], graf[6])
for vertex in someList:
    print(vertex.data)

print(someWeight)
print()
UpdateEdge(graf, graf[1], graf[2], -6)


someList, someWeight = NewShortestPath()

for vertex in someList:
    print(vertex.data)

print(someWeight)