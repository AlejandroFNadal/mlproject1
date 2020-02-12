import numpy as np
class Element:
    #default values
    id_e=0
    attributes=np.array([])
    clas=0
    
    #constructor
    def __init__(self, id_e,atts,c):
        self.id_e=id_e
        self.attributes=atts
        self.clas=c
    
    def printElement(self):
        print(self.id_e)
        #   print(self.attributes)
        #print(self.clas)
