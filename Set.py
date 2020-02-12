import numpy as np
class Set:
    attributes=np.array([])
    clas=np.array([])
    elements=[] #It contains instances of element, so it must be a list 

    def getClasses(self):
        temp_clas=np.array([])
        for elem in self.elements:
            temp_clas=np.append(temp_clas,[elem.clas])
            print(temp_clas)
        return temp_clas
            
        
        