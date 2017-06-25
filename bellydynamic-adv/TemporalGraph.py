import sys

sys.path.append("../bellydynamic-util/")

import pandas as pd

import MultiGraph as MG
import NodeAttribute as NodeA
import EdgeAttribute as EdgeA

# filename= "../bellydynamic-data/random.graph"
filename = "../bellydynamic-data/CollegeMsg.txt"

if __name__ == '__main__':
    graph = MG.MultiGraph()
    G = graph.getGraph()

    ## Node level attributes
    NodeA = NodeA.NodeAttribute(G)

    ## Edge level attributes
    EdgeA = EdgeA.EdgeAttribute(G)

    df = pd.read_csv(filename, sep=' ')

    ##### init edge attributes
    attribute_type = 1
    attribute_name = "timestamp"

    NCount = 1
    for row in df.itertuples():
        index, src, dst, timestamp = row
        srcId = int(src)
        dstId = int(dst)
        tt = int(timestamp)
        graph.addNode(srcId)
        graph.addNode(dstId)
        graph.addEdge(srcId, dstId, NCount)
        EdgeA.setEdgeAttribute(NCount, attribute_type, attribute_name, tt)
        NCount += 1

    # graph.walkNodes()
    # graph.walkEdges()

        # EdgeA.walkGraphEdgeAttributes(attribute_type, attribute_name)
