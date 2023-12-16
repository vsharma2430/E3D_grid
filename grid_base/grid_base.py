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
        return 'E '+str(self.x) + 'mm N ' + str(self.y) + 'mm U ' +str(self.z) + 'mm'
    
class grid_data:
    grid_label:str
    grid_delta:point

    def __init__(self,label:str='LBL',delta:point=point(0,0,0)):
        self.grid_label = label
        self.grid_delta = delta
    
    def getString(self):
        return self.grid_label + ' ' + self.grid_delta.getString()

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
elevlb_enclose = enclose_start_end_function('ELEVLB')
refgrd_enclose = enclose_start_end_function('REFGRD')
gridfaces_enclose = enclose_start_end_function('GRIDFACES')
gridpl_enclose = enclose_start_end_function('GRIDPL')
gridelevation_enclose = enclose_start_end_function('GRIDELEVATION')
refgln_enclose = enclose_start_end_function('REFGLN')

def form_facelb(grllbl:str,starti:str,gridaxe:str)-> str:
    return facelb_enclose(data=add_data(**{'GRDLBL':enclose_notation(grllbl),'STARTI':enclose_notation(starti),'STEPID':'1','GRDAXE':enclose_notation(gridaxe)}))

def form_elevlb(grllbl:str,starti:str,gridaxe:str)-> str:
    return elevlb_enclose(data=add_data(**{'GRDLBL':enclose_notation(grllbl),'STARTI':enclose_notation(starti),'STEPID':'1','GRDAXE':enclose_notation(gridaxe)}))

def form_refgrd(ref_name:str,origin:point,gridfaces:str)-> str:
    res:str = ''
    res += add_data(**{'POS':origin.getPMLString()})
    res += gridfaces
    return refgrd_enclose(data=res,name=ref_name)

def form_gridface(grllbl:str,starti:str,gridaxe:str,grid_planes:str)-> str:
    return gridfaces_enclose(data=add_data(grid_planes,**{'GRDLBL':enclose_notation(grllbl),'STARTI':enclose_notation(starti),'STEPID':'1','GRDAXE':enclose_notation(gridaxe)}))

def form_gridelevation(grllbl:str,starti:str,gridaxe:str,grid_planes:str)-> str:
    return gridelevation_enclose(data=add_data(grid_planes,**{'GRDLBL':enclose_notation(grllbl),'STARTI':enclose_notation(starti),'STEPID':'1','GRDAXE':enclose_notation(gridaxe)}))

def form_gridplanes(posn:point,ori:str,idplan:str,no_refgln:int)-> str:
    refgln:str=''
    for i in range(no_refgln):
        refgln += refgln_enclose() + '\n'
    return gridpl_enclose(data=add_data(refgln,**{'POS':posn.getPMLString(),'ORI':ori,'IDPLAN':enclose_notation(idplan)}))


def relation_grid(gridFace1:int,gridFace2:int,ref_grid:str,ref_gln_no:str,grid_faces1_no:str,grid_pl1_no:str,grid_faces2_no:str,grid_pl2_no:str)->str:
    res:str=''
    if(gridFace1==1):
        res += f'OLD REFGLN {ref_gln_no} of GRIDPL {grid_pl1_no} of GRIDFACES {grid_faces1_no} of REFGRD {ref_grid}\n'
    else:
        res += f'OLD REFGLN {ref_gln_no} of GRIDPL {grid_pl1_no} of GRIDELEVATION {grid_faces1_no} of REFGRD {ref_grid}\n'
    if(gridFace2==1):
        res += f'GRDREF GRIDPL {grid_pl2_no} of GRIDFACES {grid_faces2_no} of REFGRD {ref_grid}\n'
    else:
        res += f'GRDREF GRIDPL {grid_pl2_no} of GRIDELEVATION {grid_faces2_no} of REFGRD {ref_grid}\n'
    return res

#ref_grid = grid_data('/TEST_GRID',point(3687250,3640000,99700))
#x_grid = [grid_data('1/B11',point(0,0,0)),grid_data('2/B11',point(19500,0,0)),grid_data('3/B11',point(26500,0,0)),grid_data('4/B11',point(32750,0,0)),grid_data('5/B11',point(40500,0,0)),grid_data('6/B11',point(48750,0,0))]
#y_grid = [grid_data('X7',point(0,0,0)),grid_data('X8',point(0,10000,0)),grid_data('X9',point(0,15000,0))]
#z_grid = [grid_data('1',point(0,0,0))]
#new_old : bool = True
#out_file_location:str=''
#os.getcwd()+r'\E3D_grid\Result\Grid_Macro.mac'

# FINAL DB FORMATION
def build_macro(ref_grid:grid_data,x_grid,y_grid,z_grid,new_old,out_file_location):
    pml_db:str=''
    #pml_db = add_str(pml_db,'INPUT BEGIN' + '\n')

    print('Creating grid ' + ref_grid.grid_label)

    if(new_old):
        pml_db = add_str(pml_db,form_facelb(grllbl='Axis',starti='1',gridaxe='X')+ '\n')
        pml_db = add_str(pml_db,form_facelb(grllbl='Row' ,starti='A',gridaxe='Y')+ '\n')
        pml_db = add_str(pml_db,form_elevlb(grllbl='Elev',starti='1',gridaxe='Z')+ '\n')
        pml_db = idinfo_enclose(pml_db)

    x_grid_planes:str=''
    y_grid_planes:str=''
    z_grid_planes:str=''
    for xgrd in x_grid:
        x_grid_planes = add_str(x_grid_planes,form_gridplanes(xgrd.grid_delta,'Y is U and Z is W',xgrd.grid_label,len(y_grid)+len(z_grid))) + '\n'
    for ygrd in y_grid:
        y_grid_planes = add_str(y_grid_planes,form_gridplanes(ygrd.grid_delta,'Y is U and Z is S',ygrd.grid_label,len(x_grid)+len(z_grid))) + '\n'
    for zgrd in z_grid:
        z_grid_planes = add_str(z_grid_planes,form_gridplanes(zgrd.grid_delta,'',zgrd.grid_label,len(x_grid)+len(y_grid))) + '\n'

    grid_faces=list()
    grid_faces.append(form_gridface(grllbl='Axis',starti='1',gridaxe='X',grid_planes=x_grid_planes))
    grid_faces.append(form_gridface(grllbl='Row',starti='A',gridaxe='Y',grid_planes=y_grid_planes))
    grid_faces.append(form_gridelevation(grllbl='Elev',starti='1',gridaxe='Z',grid_planes=z_grid_planes))

    grid_faces_final = add_list(grid_faces)
    ref_grid_final = form_refgrd(ref_name=ref_grid.grid_label,origin=ref_grid.grid_delta,gridfaces=grid_faces_final)

    if(new_old):
        pml_db = grid_world_enclose(pml_db + '\n' + ref_grid_final)
    else:
        pml_db = ref_grid_final

    #pml_db = add_str(pml_db,'INPUT FINISH' + '\n')

    print(('New' if new_old else 'Old') + ' grid system')
    print('Opening file ' + out_file_location)
    f = open(out_file_location, "w")
    f.write(pml_db)
    f.close()
    print('File closed')


#GRID RELATIONS CODE - NOT REQUIRED
"""
for i in range(len(x_grid)):
    for j in range(len(y_grid)):
        pml_db = add_str(pml_db,'\n'+\
                relation_grid(gridFace1=1,gridFace2=1,ref_grid=ref_grid.grid_label,
                              ref_gln_no=j+1,grid_pl1_no=i+1,grid_faces1_no=1,grid_pl2_no=j+1,grid_faces2_no=2))
    for k in range(len(z_grid)):
        pml_db = add_str(pml_db,'\n'+\
                relation_grid(gridFace1=1,gridFace2=2,ref_grid=ref_grid.grid_label,
                              ref_gln_no=len(y_grid)+k+1,grid_pl1_no=i+1,grid_faces1_no=1,grid_pl2_no=k+1,grid_faces2_no=1))
        
for i in range(len(y_grid)):
    for j in range(len(x_grid)):
        pml_db = add_str(pml_db,'\n'+\
                relation_grid(gridFace1=1,gridFace2=1,ref_grid=ref_grid.grid_label,
                              ref_gln_no=j+1,grid_pl1_no=i+1,grid_faces1_no=1,grid_pl2_no=j+1,grid_faces2_no=2))
    for k in range(len(z_grid)):
        pml_db = add_str(pml_db,'\n'+\
                relation_grid(gridFace1=1,gridFace2=2,ref_grid=ref_grid.grid_label,
                              ref_gln_no=len(x_grid)+k+1,grid_pl1_no=i+1,grid_faces1_no=1,grid_pl2_no=k+1,grid_faces2_no=1))
        
for i in range(len(z_grid)):
    for j in range(len(x_grid)):
        pml_db = add_str(pml_db,'\n'+\
                relation_grid(gridFace1=2,gridFace2=1,ref_grid=ref_grid.grid_label,
                              ref_gln_no=j+1,grid_pl1_no=i+1,grid_faces1_no=1,grid_pl2_no=j+1,grid_faces2_no=2))
    for k in range(len(y_grid)):
        pml_db = add_str(pml_db,'\n'+\
                relation_grid(gridFace1=2,gridFace2=1,ref_grid=ref_grid.grid_label,
                              ref_gln_no=len(x_grid)+k+1,grid_pl1_no=i+1,grid_faces1_no=1,grid_pl2_no=k+1,grid_faces2_no=1))
"""
