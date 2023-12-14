import os

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
        #EXAMPLE - E 3687250mm N 3640000mm U 102400mm
        return 'E '+str(self.x) + 'mm N ' + str(self.y) + ' mm U ' +str(self.z) + 'mm'
    
class grid_data:
    grid_label:str
    grid_delta:point

    def __init__(self,label:str='LBL',delta:point=point(0,0,0)):
        self.grid_label = label
        self.grid_delta = delta

def add_str(*argv)-> str:
    res:str=''
    for arg in argv:
        res += str(arg)
    return res

def add_list(list_str:[str])-> str:
    res:str=''
    for dataX in list_str:
        res += str(dataX) + '\n'
    return res

def enclose_quotes(data:str)-> str:
    return '\''+data+'\''

def enclose_notation(data:str)-> str:
    return '@'+data+'@'

def add_data(*argv,**kwargs) -> str:
    res_str : str = ''
    
    for key, value in kwargs.items():
        key = str(key)
        value = str(value)
        if(value.startswith('@') and value.endswith('@')):
            res_str = res_str + key + ' ' + enclose_quotes(value.strip('@')) + '\n'
        elif(value=='' or key==''):
            continue
        else:
            res_str = res_str + key + ' ' + value + '\n'
    res_str+='\n'
    res_str += add_str(*argv)
    return res_str

def enclose_start_end_function(enclosure:str='')-> str:
    return lambda data='',name='': 'NEW '+ enclosure + ' '+ name + (('\n' + data) if len(str(data))>0 else '') + '\nEND' 

grid_world_enclose = enclose_start_end_function('GRIDWLD')
idinfo_enclose = enclose_start_end_function('IDINFO')
facelb_enclose = enclose_start_end_function('FACELB')
refgrd_enclose = enclose_start_end_function('REFGRD')
gridfaces_enclose = enclose_start_end_function('GRIDFACES')
gridpl_enclose = enclose_start_end_function('GRIDPL')
gridelevation_enclose = enclose_start_end_function('GRIDELEVATION')
refgln_enclose = enclose_start_end_function('REFGLN')

def form_facelb(grllbl:str,starti:str,gridaxe:str)-> str:
    return facelb_enclose(data=add_data(**{'GRDLBL':enclose_notation(grllbl),'STARTI':enclose_notation(starti),'STEPID':'1','GRDAXE':enclose_notation(gridaxe)}))

def form_refgrd(ref_name:str,origin:point,gridfaces:str,UUID:str='unset')-> str:
    res:str = ''
    res += add_data(**{'POS':origin.getPMLString(),'UUID':UUID})
    res += gridfaces
    return refgrd_enclose(data=res,name=ref_name)

def form_gridface(grllbl:str,starti:str,gridaxe:str,grid_planes:str)-> str:
    return gridfaces_enclose(data=add_data(grid_planes,**{'GRDLBL':enclose_notation(grllbl),'STARTI':enclose_notation(starti),'STEPID':'1','GRDAXE':enclose_notation(gridaxe),'UUID':'unset'}))

def form_gridelevation(grllbl:str,starti:str,gridaxe:str,grid_planes:str)-> str:
    return gridelevation_enclose(data=add_data(grid_planes,**{'GRDLBL':enclose_notation(grllbl),'STARTI':enclose_notation(starti),'STEPID':'1','GRDAXE':enclose_notation(gridaxe),'UUID':'unset'}))

def form_gridplanes(posn:point,ori:str,idplan:str,no_refgln:int)-> str:
    refgln:str=''
    for i in range(no_refgln):
        refgln += refgln_enclose() + '\n'
    return gridpl_enclose(data=add_data(refgln,**{'POS':posn.getPMLString(),'ORI':ori,'IDPLAN':enclose_notation(idplan),'PPLIM':'false','UUID':'unset'}))

def relation_grid(gridFace:int,ref_grid:str,ref_gln_no:str,grid_faces1_no:str,grid_pl1_no:str,grid_faces2_no:str,grid_pl2_no:str)->str:
    res:str=''
    res += f'OLD REFGLN {ref_gln_no} of GRIDPL {grid_pl1_no} of GRIDFACES {grid_faces1_no} of REFGRD {ref_grid}\n'
    res += f'GRDREF GRIDPL {grid_pl2_no} of {'GRIDFACES' if gridFace==1 else 'GRIDELEVATION'} {grid_faces2_no} of REFGRD {ref_grid}\n'
    return res

origin = point(0,0,0)
ref_grid = grid_data('/SS_04',point(1000,2000,3000))
x_grid = [grid_data('1/B11',point(0,0,0)),grid_data('2/B11',point(2000,0,0)),grid_data('3/B11',point(3000,0,0))]
y_grid = [grid_data('X7',point(0,0,0)),grid_data('X8',point(0,5000,0))]
z_grid = [grid_data('1',point(0,0,0))]

# FINAL DB FORMATION
pml_db:str=''
pml_db = add_str(pml_db,form_facelb(grllbl='Axis',starti='1',gridaxe='X'))
pml_db = add_str(pml_db,form_facelb(grllbl='Row',starti='A',gridaxe='Y'))
pml_db = add_str(pml_db,form_facelb(grllbl='Elev',starti='1',gridaxe='Z'))
pml_db = idinfo_enclose(pml_db)

x_grid_planes:str=''
y_grid_planes:str=''
z_grid_planes:str=''
for xgrd in x_grid:
    x_grid_planes = add_str(x_grid_planes,form_gridplanes(xgrd.grid_delta,'Y is U and Z is W',xgrd.grid_label,len(y_grid))) + '\n'
for ygrd in y_grid:
    y_grid_planes = add_str(y_grid_planes,form_gridplanes(ygrd.grid_delta,'Y is U and Z is S',ygrd.grid_label,len(x_grid))) + '\n'
for zgrd in z_grid:
    z_grid_planes = add_str(z_grid_planes,form_gridplanes(zgrd.grid_delta,'',zgrd.grid_label,len(x_grid)+len(y_grid))) + '\n'

grid_faces=list()
grid_faces.append(form_gridface(grllbl='Axis',starti='1',gridaxe='X',grid_planes=x_grid_planes))
grid_faces.append(form_gridface(grllbl='Row',starti='A',gridaxe='Y',grid_planes=y_grid_planes))
grid_faces.append(form_gridface(grllbl='Elev',starti='1',gridaxe='Z',grid_planes=z_grid_planes))

grid_faces_final = add_list(grid_faces)
pml_db = grid_world_enclose(pml_db + '\n' + form_refgrd(ref_name=ref_grid.grid_label,origin=ref_grid.grid_delta,gridfaces=grid_faces_final))

#GRID RELATIONS CODE REMAINING
#pml_db = add_str(pml_db,'\n'+relation_grid(1,0,0,0,0,0,0))

out_file = (os.getcwd()+r'\E3D_grid\Result\Grid_Macro.mac')
f = open(out_file, "w")
f.write(pml_db)
f.close()
