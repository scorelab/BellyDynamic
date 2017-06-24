import sys
import snap
import random


def PrintGStats(s, Graph):
    print "graph %s, nodes %d, edges %d, empty %s" % (
        s, Graph.GetNodes(), Graph.GetEdges(),
        "yes" if Graph.Empty() else "no")

class MultiGraph:
    def __init__(self):
        self.G=self.getEmptyGraph()
        PrintGStats("TestG",self.G)

        self.setGraph(nodes=101,edges=500)
        PrintGStats("TestG", self.G)

    def getEmptyGraph(self):
        return snap.TNEANet();

    def getGraph(self):
        return self.G

    def getEdgeId(self, srcId, dstId, sequenceTag):
        return int(str(snap.TIntPr(srcId,dstId).GetPrimHashCd())+str(sequenceTag))

    def setGraph(self,nodes,edges):
        # create the nodes
        for i in range(0, nodes):
            self.G.AddNode(i)
        # create random edges
        NCount = edges
        while NCount > 0:
            x = int(random.random() * nodes)
            y = int(random.random() * nodes)
            sequenceTag = int(random.random() * edges) # e.g. Timestamp
            EId = self.getEdgeId(x,y,sequenceTag)
            # skip the loops, one edge between node pair
            if x != y and not self.G.IsEdge(x, y):
                n = self.G.AddEdge(x, y, EId)
                NCount -= 1

    def walkNodes(self):
        print "Nodes: "
        NCount = 0
        NI = self.G.BegNI()
        while NI < self.G.EndNI():
            print NI.GetId()
            NCount += 1
            NI.Next()

    def walkEdges(self):
        print "Edges: "
        ECount = 0
        EI = self.G.BegEI()
        while EI < self.G.EndEI():
            print EI.GetId()
            ECount += 1
            EI.Next()


