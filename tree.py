class tree:
    root=None
    class_list=[]#list of classes

class node:
    attr=0 #atribute that is represented by the node
    value=0 #value of the attribute
    elements=[] #list of elements that have the value of the attr

    def addChildren(self):
        x= node()
        self.elements.append(x)

    