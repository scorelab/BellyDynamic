import snap


## Get graph structural properties
## Author: samtube405
## All rights reserved.
class Structure:
    def __init__(self, graph, graphName):
        self.G = graph
        self.graphName = graphName

    def initilize(self, fileName):
        self.fileName = fileName
        self.G = self.getGraph()

    def genGraph(self, nodes):
        print "Generating random graph..."
        genFileName = 'random5000by6.txt'
        nodesV = snap.TIntV()
        for i in range(nodes):
            if (i % 6 != 0):
                nodesV.Add(i)

        comG = snap.GenFull(snap.PUNGraph, nodes)
        snap.DelNodes(comG, nodesV)

        snap.SaveEdgeList(comG, genFileName)
        return genFileName

    def getGraph(self):
        return snap.LoadEdgeList(snap.PUNGraph, self.fileName)

    def getGraphName(self):
        tags = self.fileName.split("/")
        return tags[len(tags) - 1].split(".")[0]

    def genGraphInfo(self):
        graphName = self.graphName

        # get the number of nodes and edges in the graph
        print "Number of nodes in %s: %d" % (graphName, self.G.GetNodes())
        print "Number of edges in %s: %d" % (graphName, self.G.GetEdges())

        # get the node id(s) with highest degree

        nodeIdMaxDegree = snap.GetMxOutDegNId(self.G)

        maxDegree = -1
        for node in self.G.Nodes():
            if (node.GetId() == nodeIdMaxDegree):
                maxDegree = node.GetOutDeg()
                break;

        nodeIdsMaxDegreeT = ""
        for node in self.G.Nodes():
            if (maxDegree == node.GetOutDeg()):
                nodeIdsMaxDegreeT += str(node.GetId()) + ","

        print "Node id(s) with highest degree in %s: %s" % (graphName, nodeIdsMaxDegreeT)

        # plot degree distribution
        snap.PlotOutDegDistr(self.G, graphName, "Degree Distribution")
        degreeFileName = "outDeg." + graphName + ".png"
        print "Degree distribution of %s is in: %s" % (graphName, degreeFileName)

        # plot shortest path distribution
        snap.PlotShortPathDistr(self.G, graphName, "Shortest Path Distribution")
        shortestPathFileName = "diam." + graphName + ".png"
        print "Shortest path distribution of %s is in: %s" % (graphName, shortestPathFileName)

        # get the fraction of nodes in largest cc
        print "Fraction of nodes in largest connected component in %s: %f" % (graphName, snap.GetMxSccSz(self.G))

        # plot the component size distribution
        snap.PlotSccDistr(self.G, graphName, "Component size distribution")
        sccFileName = "scc." + graphName + ".png"
        print "Component size distribution of %s is in: %s" % (graphName, sccFileName)
