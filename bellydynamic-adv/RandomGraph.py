import sys

sys.path.append("../bellydynamic-util/")

import MultiGraph as MG
import NodeAttribute as NodeA
import EdgeAttribute as EdgeA

filename = "../bellydynamic-data/random.graph"

if __name__ == '__main__':
    graph = MG.MultiGraph()

    graph.genGraph(nodes=101, edges=500)

    graph.saveGraph(filename)

    graph.loadBinaryGraph(filename)

    G = graph.getGraph()

    graph.walkNodes()
    graph.walkEdges()

    ## Node level attributes
    NodeA = NodeA.NodeAttribute(G)

    NId = G.GetRndNId()
    ##### init node attributes
    attribute_type = 1
    attribute_name = "Age"
    NodeA.initNodeAttribute(attribute_type, attribute_name, 0)

    # set node attribute
    NodeA.setNodeAttribute(NId, attribute_type, attribute_name, 34)

    NodeA.walkGraphNodeAttributes(attribute_type, attribute_name)

    ##### init node attributes
    attribute_type = 2
    attribute_name = "Price"
    NodeA.initNodeAttribute(attribute_type, attribute_name, 0.0)

    # set node attribute
    NodeA.setNodeAttribute(NId, attribute_type, attribute_name, 45.7862)

    NodeA.walkGraphNodeAttributes(attribute_type, attribute_name)

    ##### init node attributes
    attribute_type = 3
    attribute_name = "Name"
    NodeA.initNodeAttribute(attribute_type, attribute_name, "NA")

    # set node attribute
    NodeA.setNodeAttribute(NId, attribute_type, attribute_name, "Jale")

    NodeA.walkGraphNodeAttributes(attribute_type, attribute_name)

    ##### walk specific node attributes
    NodeA.walkNodeAttributes(NId)

    ## ----------------------------------------------------------------------- ##
    ## Edge level attributes
    EdgeA = EdgeA.EdgeAttribute(G)

    EId = G.GetRndEId()
    ##### init node attributes
    attribute_type = 1
    attribute_name = "Timestamp"
    EdgeA.initEdgeAttribute(attribute_type, attribute_name, 0)

    # set node attribute
    EdgeA.setEdgeAttribute(EId, attribute_type, attribute_name, 87508)

    EdgeA.walkGraphEdgeAttributes(attribute_type, attribute_name)

    ##### init node attributes
    attribute_type = 2
    attribute_name = "Duration"
    EdgeA.initEdgeAttribute(attribute_type, attribute_name, 0.0)

    # set node attribute
    EdgeA.setEdgeAttribute(EId, attribute_type, attribute_name, 72.45)

    EdgeA.walkGraphEdgeAttributes(attribute_type, attribute_name)

    ##### walk specific edge attributes
    EdgeA.walkEdgeAttributes(EId)
