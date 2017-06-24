import random

import snap


def PrintGStats(s, Graph):
    print "graph %s, nodes %d, edges %d, empty %s" % (
        s, Graph.GetNodes(), Graph.GetEdges(),
        "yes" if Graph.Empty() else "no")

class MultiGraph:
    def __init__(self):
        self.G=self.getEmptyGraph()

    def getEmptyGraph(self):
        return snap.TNEANet();

    def loadGraph(self, graph_type, fileName, src_column, dst_column):
        return snap.LoadEdgeList(graph_type, fileName, src_column, dst_column)

    def getGraph(self):
        return self.G

    def setGraph(self, graph):
        self.G = graph

    # def getEdgeId(self, srcId, dstId, sequenceTag):
    #     return int(str(snap.TIntPr(srcId,dstId).GetPrimHashCd())+str(sequenceTag))

    def genGraph(self, nodes, edges):
        # create the nodes
        for i in range(0, nodes):
            self.addNode(i)
        # create random edges
        NCount = edges
        while NCount > 0:
            x = int(random.random() * nodes)
            y = int(random.random() * nodes)
            # x = int(0.5 * nodes)
            # y = int(0.6 * nodes)
            sequenceTag = NCount  # e.g. Timestamp

            # # skip the loops, one edge between node pair
            # if x != y and not self.G.IsEdge(x, y):
            #     n = self.G.AddEdge(x, y, EId)
            #     NCount -= 1
            # skip the loops, multiple edges between node pair
            if x != y:
                n = self.G.AddEdge(x, y, sequenceTag)
                NCount -= 1

    def addNode(self, nId):
        if (not self.G.IsNode(nId)):
            self.G.AddNode(nId)

    def addEdge(self, srcId, dstId, sequenceTag):
        self.G.AddEdge(srcId, dstId, sequenceTag)

    def delEdge(self, srcId, dstId):
        self.G.DelEdge(srcId, dstId)

    def saveGraph(self, fileName):
        FOut = snap.TFOut(fileName)
        self.G.Save(FOut)
        FOut.Flush()

    def loadBinaryGraph(self, fileName):
        FIn = snap.TFIn(fileName)
        self.G = snap.TNEANet(FIn)

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


