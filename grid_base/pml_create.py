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