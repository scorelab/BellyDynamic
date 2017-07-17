import snap

class NodeAttribute:
    def __init__(self,G):
        self.G=G

    def initNodeAttribute(self,attribute_type, attribute_name, attribute_default_value):
        if attribute_type == 1:
            self.G.AddIntAttrN(attribute_name, attribute_default_value)
        elif attribute_type == 2:
            self.G.AddFltAttrN(attribute_name, attribute_default_value)
        elif attribute_type == 3:
            self.G.AddStrAttrN(attribute_name, attribute_default_value)

    def setNodeAttribute(self,nodeId, attribute_type, attribute_name, attribute_value):
        if attribute_type == 1:
            self.G.AddIntAttrDatN(nodeId, attribute_value, attribute_name)
        elif attribute_type == 2:
            self.G.AddFltAttrDatN(nodeId, attribute_value, attribute_name)
        elif attribute_type == 3:
            self.G.AddStrAttrDatN(nodeId, attribute_value, attribute_name)

    def walkGraphNodeAttributes(self, attribute_type, attribute_name):
        NodeId = 0
        if attribute_type == 1:
            NI = self.G.BegNAIntI(attribute_name)
            while NI < self.G.EndNAIntI(attribute_name):
                if NI.GetDat() != 0:
                    print "Attribute: %s, Node: %i, Val: %d" % (attribute_name, NodeId, NI.GetDat())
                NodeId += 1
                NI.Next()
        elif attribute_type == 2:
            NI = self.G.BegNAFltI(attribute_name)
            while NI < self.G.EndNAFltI(attribute_name):
                if NI.GetDat() != 0:
                    print "Attribute: %s, Node: %i, Val: %f" % (attribute_name, NodeId, NI.GetDat())
                NodeId += 1
                NI.Next()
        elif attribute_type == 3:
            NI = self.G.BegNAStrI(attribute_name)
            while NI < self.G.EndNAStrI(attribute_name):
                if NI.GetDat() != "NA":
                    print "Attribute: %s, Node: %i, Val: %s" % (attribute_name, NodeId, NI.GetDat())
                NodeId += 1
                NI.Next()

    def walkNodeAttributes(self, NId):
        NIdAttrName = snap.TStrV()
        self.G.AttrNameNI(NId, NIdAttrName)
        AttrLen = NIdAttrName.Len()

        NIdAttrValue = snap.TStrV()
        self.G.AttrValueNI(NId, NIdAttrValue)
        AttrLen = NIdAttrValue.Len()

        for i in range(AttrLen):
            print "Vertical Node: %i, Attr: %s, Val: %s" % (NId, NIdAttrName.GetI(i)(),NIdAttrValue.GetI(i)())