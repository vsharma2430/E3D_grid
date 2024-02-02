import os

def increment_tcc_ver():
    version_file = r'\\10.40.10.46\itstrl\RELEASE\TCCLIVE\TeklaModules\ver.dat'
    increment_file(version_file)

def increment_file(file_location:str):
    if(os.path.exists(file_location)):
        current_version : int = 0
        with open(file_location ,'+r') as file:
            current_version = int(file.read())
        with open(file_location ,'+w') as file:
            file.write(str(current_version+1))