class point:
    x:float
    y:float
    z:float

    def __init__(self,x:float=0,y:float=0,z:float=0):
        self.x = x
        self.y = y
        self.z = z

    def getString(self)-> str:
        return str(self.x) + ',' + str(self.y) + ',' +str(self.z)
    
    def getPMLString(self)-> str:
        return 'E '+str(self.x) + 'mm N ' + str(self.y) + 'mm U ' +str(self.z) + 'mm'