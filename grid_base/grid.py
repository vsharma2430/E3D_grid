from .point import *
    
class grid_data:
    grid_label:str
    grid_delta:point

    def __init__(self,label:str='LBL',delta:point=point(0,0,0)):
        self.grid_label = label
        self.grid_delta = delta
    
    def getString(self):
        return self.grid_label + ' ' + self.grid_delta.getString()