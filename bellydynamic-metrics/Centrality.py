import time

import snap


# import matplotlib.pyplot
# import pylab

## Get graph centrality measurements
## Author: samtube405
class Centrality:
    # init snappy graph
    def __init__(self, graph, graphName):
        self.G = graph
        self.graphName = graphName
        self.namesDict = {}

    def getGraph(self):
        return snap.LoadEdgeList(snap.PUNGraph, self.elistFileName)

    # abstract method to calculate centrality values from given method
    def getCentr(self, centrMethod):
        nodesKeysCentrVals = snap.TIntFltH()
        for node in self.G.Nodes():
            centrValue = centrMethod(self.G, node.GetId())
            nodesKeysCentrVals[node.GetId()] = centrValue

        return nodesKeysCentrVals

    # get the centrality values
    def genCentrValues(self, nodesKeysCentrVals):
        nodesCentrVals = []
        for nodeKey in nodesKeysCentrVals:
            nodesCentrVals.append(nodesKeysCentrVals[nodeKey])

        return nodesCentrVals

    # sort the centrality values
    def getHashmapText(self, map):
        map.SortByDat(False);
        output = "";
        topNodes = ""
        index = 0
        for key in map:
            output += "nodeID: %d centrality: %f\n" % (key, map[key])
            index += 1
            if (index <= 10):
                label = self.namesDict.setdefault(str(key), str(key))
                topNodes += "\tnodeID: %d label: %s\n" % (key, label)
        return output, topNodes

    # get the betweenness centrality values
    def getBetweennessCentr(self):
        nodesKeyCentrVals = snap.TIntFltH()
        edgesKeyCentrVals = snap.TIntPrFltH()
        snap.GetBetweennessCentr(self.G, nodesKeyCentrVals, edgesKeyCentrVals, 1.0)

        return nodesKeyCentrVals

    # get harmonic closeness centrality values
    def getHarmonicClosenessCentr(self, G, nodeId):
        n = G.GetNodes()
        nodeDistances = snap.TIntH()
        snap.GetShortPath(G, nodeId, nodeDistances)
        centrValue = 0.0
        for nodeKey in nodeDistances:
            if (nodeKey != nodeId):
                centrValue += (1 / float(nodeDistances[nodeKey]))

        centrValue /= (n - 1)
        # print nodeId, centrValue

        return centrValue

    def writeOutput(self, fileName, output):
        file = open(fileName, "w")
        file.write(output)
        file.close()

    def getOutputFileName(self, suffix):
        return self.graphName + suffix + ".txt"

    def genGraphInfoBetweeness(self, centrality):
        print "\n+++++++++++ %s ++++++++++++" % (centrality)
        print "Calculating centrality values..."
        start_time = time.clock()
        nodesKeyCentrVals = snap.TIntFltH()
        edgesKeyCentrVals = snap.TIntPrFltH()
        snap.GetBetweennessCentr(self.G, nodesKeyCentrVals, edgesKeyCentrVals, 1.0)
        print "Computation time: %f secs." % (time.clock() - start_time)
        outputFileName = self.getOutputFileName(centrality)
        print "Generating the output -> %s" % (outputFileName)
        output, topNodes = self.getHashmapText(nodesKeyCentrVals)
        self.writeOutput(outputFileName, output)
        print "Top node labels: \n %s" % (topNodes)

        return nodesKeyCentrVals

    def genGraphInfo(self, centrality, func):
        print "\n+++++++++++ %s ++++++++++++" % (centrality)
        print "Calculating centrality values..."
        start_time = time.clock()
        nodesKeysCentrVals = self.getCentr(func)
        print "Computation time: %f secs." % (time.clock() - start_time)
        outputFileName = self.getOutputFileName(centrality)
        print "Generating the output -> %s" % (outputFileName)
        output, topNodes = self.getHashmapText(nodesKeysCentrVals)
        self.writeOutput(outputFileName, output)
        print "Top node labels: \n %s" % (topNodes)

        return nodesKeysCentrVals
