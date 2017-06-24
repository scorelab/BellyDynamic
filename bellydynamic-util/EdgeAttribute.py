import snap

class EdgeAttribute:
    def __init__(self,G):
        self.G=G

    def initEdgeAttribute(self,attribute_type, attribute_name, attribute_default_value):
        if attribute_type == 1:
            self.G.AddIntAttrE(attribute_name, attribute_default_value)
        elif attribute_type == 2:
            self.G.AddFltAttrE(attribute_name, attribute_default_value)
        elif attribute_type == 3:
            self.G.AddStrAttrE(attribute_name, attribute_default_value)

    def setEdgeAttribute(self,EdgeId, attribute_type, attribute_name, attribute_value):
        if attribute_type == 1:
            self.G.AddIntAttrDatE(EdgeId, attribute_value, attribute_name)
        elif attribute_type == 2:
            self.G.AddFltAttrDatE(EdgeId, attribute_value, attribute_name)
        elif attribute_type == 3:
            self.G.AddStrAttrDatE(EdgeId, attribute_value, attribute_name)

    def walkGraphEdgeAttributes(self, attribute_type, attribute_name):
        EdgeId = 0
        if attribute_type == 1:
            EI = self.G.BegEAIntI(attribute_name)
            while EI < self.G.EndEAIntI(attribute_name):
                if EI.GetDat() != 0:
                    print "Attribute: %s, Edge: %i, Val: %d" % (attribute_name, EdgeId, EI.GetDat())
                EdgeId += 1
                EI.Next()
        elif attribute_type == 2:
            EI = self.G.BegEAFltI(attribute_name)
            while EI < self.G.EndEAFltI(attribute_name):
                if EI.GetDat() != 0:
                    print "Attribute: %s, Edge: %i, Val: %f" % (attribute_name, EdgeId, EI.GetDat())
                EdgeId += 1
                EI.Next()
        elif attribute_type == 3:
            EI = self.G.BegEAStrI(attribute_name)
            while EI < self.G.EndEAStrI(attribute_name):
                if EI.GetDat() != "NA":
                    print "Attribute: %s, Edge: %i, Val: %s" % (attribute_name, EdgeId, EI.GetDat())
                EdgeId += 1
                EI.Next()

    def walkEdgeAttributes(self, EId):
        EIdAttrName = snap.TStrV()
        self.G.AttrNameEI(EId, EIdAttrName)
        AttrLen = EIdAttrName.Len()

        EIdAttrValue = snap.TStrV()
        self.G.AttrValueEI(EId, EIdAttrValue)
        AttrLen = EIdAttrValue.Len()

        for i in range(AttrLen):
            print "Vertical Edge: %i, Attr: %s, Val: %s" % (EId, EIdAttrName.GetI(i)(),EIdAttrValue.GetI(i)())