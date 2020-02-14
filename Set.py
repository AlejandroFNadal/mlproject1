import numpy as np
import pandas as pd
class Sets:
    #attributes=np.array([])
    #clas=np.array([])
    elements=[] #It contains instances of element, so it must be a list 

        
    def getClasses(self):
        temp_clas=np.array([],dtype=int)
        for elem in self.elements:
            temp_clas=np.append(temp_clas,[elem.clas])
            #print(temp_clas) #just for debbuging stuff
        return temp_clas
    
    def getAttColumn(self, num):
        temp_clas=np.array([],dtype=int)
        for elem in self.elements:
            temp_clas=np.append(temp_clas,[elem.attributes[num]])
        return temp_clas
    
    def addElement(self,elem):
        self.elements.append(elem)

        
        