import sys

sys.path.append("../bellydynamic-util/")
sys.path.append("../bellydynamic-metrics/")

import snap

import MultiGraph as MG
import NodeAttribute as NodeA
import EdgeAttribute as EdgeA

import Structure as structure
import Centrality as centrality

# A file containing the graph, where each row contains an edge
# and each edge is represented with the source and dest node ids,
# the edge attributes, and the source and destination node attributes
# separated by a tab.
edgefilename = "../bellydynamic-data/CollegeMsg.txt"
graphName = "CollegeMsg"

if __name__ == '__main__':
    context = snap.TTableContext()  # When loading strings from different files, it is important to use the same context
    # so that SNAP knows that the same string has been seen before in another table.

    schema = snap.Schema()
    schema.Add(snap.TStrTAttrPr("srcID", snap.atStr))
    schema.Add(snap.TStrTAttrPr("dstID", snap.atStr))
    schema.Add(snap.TStrTAttrPr("timestamp", snap.atInt))
    # schema.Add(snap.TStrTAttrPr("edgeattr2", snap.atStr))
    # schema.Add(snap.TStrTAttrPr("srcnodeattr1", snap.atStr))
    # schema.Add(snap.TStrTAttrPr("srcnodeattr2", snap.atStr))
    # schema.Add(snap.TStrTAttrPr("dstnodeattr1", snap.atStr))
    # schema.Add(snap.TStrTAttrPr("dstnodeattr2", snap.atStr))

    table = snap.TTable.LoadSS(schema, edgefilename, context, " ", snap.TBool(False))

    # In this example, we add both edge attributes to the network,
    # but only one src node attribute, and no dst node attributes.
    edgeattrv = snap.TStrV()
    edgeattrv.Add("timestamp")
    # edgeattrv.Add("edgeattr2")

    srcnodeattrv = snap.TStrV()
    # srcnodeattrv.Add("srcnodeattr1")

    dstnodeattrv = snap.TStrV()

    # net will be an object of type snap.PNEANet
    G = snap.ToNetwork(snap.PNEANet, table, "srcID", "dstID", srcnodeattrv, dstnodeattrv, edgeattrv, snap.aaFirst)

    graph = MG.MultiGraph()
    graph.setGraph(G)

    ## Node level attributes
    NodeA = NodeA.NodeAttribute(G)

    ## Edge level attributes
    EdgeA = EdgeA.EdgeAttribute(G)

    graph.walkNodes()
    graph.walkEdges()

    ##### init edge attributes
    attribute_type = 1
    attribute_name = "timestamp"

    EdgeA.walkGraphEdgeAttributes(attribute_type, attribute_name)

    structure = structure.Structure(G, "CollegeMsg")
    structure.genGraphInfo()

    centrality = centrality.Centrality(G, "CollegeMsg")

    # degCentrVals = centrality.genCentrValues(centrality.genGraphInfo("_degree-centrality", snap.GetDegreeCentr))

    # closenessCentrVals = centrality.genCentrValues(
    #     centrality.genGraphInfo("_closeness-centrality", snap.GetClosenessCentr))
    #
    # harmonicClosenessCentrVals = centrality.genCentrValues(
    #     centrality.genGraphInfo("_harmonic-closeness-centrality", centrality.getHarmonicClosenessCentr))
    #
    # localccCentrVals = centrality.genCentrValues(
    #     centrality.genGraphInfo("_local-clustering-coefficient", snap.GetNodeClustCf))

    betweenessCentrVals = centrality.genCentrValues(centrality.genGraphInfoBetweeness("_betweeness-centrality"))

    # print "Calculating correlation coefficient.. Rows vs Cols. [_degree-centrality,_closeness-centrality, _harmonic-closeness-centrality,_local-clustering-coefficient,_betweeness-centrality]"
    # print numpy.corrcoef(
    #     [degCentrVals, closenessCentrVals, harmonicClosenessCentrVals, localccCentrVals, betweenessCentrVals])
