from .point import *
    
def getFloat(data:str)->float:
    return 0 if data=='' or data==None else float(data)

class grid_data:
    grid_label:str
    grid_delta:point

    def __init__(self,label:str='LBL',delta:point=point(0,0,0)):
        self.grid_label = label
        self.grid_delta = delta
    
    def getString(self)->str:
        return self.grid_label + ' ' + self.grid_delta.getString()
    
def getGridList(grid_names:str,grid_values:str,dir:int)->list[grid_data]:
    grid_list = []
    grid_val_split = grid_values.split(' ')
    grid_name_split = grid_names.split(' ')
    grid_vals = []
    for valX in grid_val_split:
        if(str(valX).find('*')>0):
            grid_valX_split = str(valX).split('*')
            rep = int(grid_valX_split[0].strip())
            valX = getFloat(grid_valX_split[1].strip())
            for i in range(rep):
                grid_vals.append(getFloat(valX))
        else:
            grid_vals.append(valX)

    if(len(grid_name_split)==len(grid_vals)):
        sum :float= 0
        for i in range(len(grid_vals)):
            grid_delta:point=point(0,0,0)
            current_dim = sum+getFloat(grid_vals[i])
            if(dir==1):
                grid_delta = point(current_dim,0,0)
            elif(dir==2):
                grid_delta = point(0,current_dim,0)
            else:
                grid_delta = point(0,0,current_dim)
            grid_data_X = grid_data(label=grid_name_split[i],delta=grid_delta)
            sum += getFloat(grid_vals[i])
            print(grid_data_X.getString())
            grid_list.append(grid_data_X)

    return grid_list
