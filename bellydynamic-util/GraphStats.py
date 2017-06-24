import snap

statDir = "../bellydynamic-data/"


class GraphStats:
    def __init__(self, graph, graphName):
        self.G = graph
        self.graphName = graphName

    def printGStats(self):
        snap.PrintInfo(self.G, self.graphName, statDir + self.graphName + "-info.txt", False)

    def getGraphName(self, graphName):
        tags = graphName.split("/")
        return tags[len(tags) - 1].split(".")[0]

    def countNodes(self):
        return self.GetNodes()

    def countEdges(self):
        return self.GetEdges()
