import sys

sys.path.append("../bellydynamic-util/")

import pandas as pd

import MultiGraph as MG
import NodeAttribute as NodeA
import EdgeAttribute as EdgeA

# filename= "../bellydynamic-data/random.graph"
# filename = "../bellydynamic-data/CollegeMsg.txt"
filename = "../bellydynamic-data/email-Eu-core-temporal-Dept1.txt"

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

    for row in df.itertuples():
        index, src, dst, timestamp = row
        EId = index
        srcId = int(src)
        dstId = int(dst)
        tt = int(timestamp)
        graph.addNode(srcId)
        graph.addNode(dstId)
        graph.addEdge(srcId, dstId, EId)
        EdgeA.setEdgeAttribute(EId, attribute_type, attribute_name, tt)

    graph.walkNodes()
    graph.walkEdges()

    EdgeA.walkGraphEdgeAttributes(attribute_type, attribute_name)
