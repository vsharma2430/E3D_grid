from .point import *
    
class grid_data:
    grid_label:str
    grid_delta:point

    def __init__(self,label:str='LBL',delta:point=point(0,0,0)):
        self.grid_label = label
        self.grid_delta = delta
    
    def getString(self):
        return self.grid_label + ' ' + self.grid_delta.getString()
    
def getGridList(grid_names:str,grid_values:str,dir:int):
    grid_list = []
    grid_val_split = grid_values.split(' ')
    grid_name_split = grid_names.split(' ')
    grid_vals = []
    for valX in grid_val_split:
        if(str(valX).find('*')>0):
            grid_valX_split = str(valX).split('*')
            rep = int(grid_valX_split[0].strip())
            valX = float(grid_valX_split[1].strip())
            for i in range(rep):
                grid_vals.append(float(valX))
        else:
            grid_vals.append(valX)

    if(len(grid_name_split)==len(grid_vals)):
        sum :float= 0
        for i in range(len(grid_vals)):
            grid_delta:point=point(0,0,0)
            if(dir==1):
                grid_delta = point(sum+float(grid_vals[i]),0,0)
            elif(dir==2):
                grid_delta = point(0,sum+float(grid_vals[i]),0)
            else:
                grid_delta = point(0,0,sum+float(grid_vals[i]))
            grid_data_X = grid_data(label=grid_name_split[i],delta=grid_delta)
            sum += float(grid_vals[i])
            print(grid_data_X.getString())
            grid_list.append(grid_data_X)

    return grid_list
