import PyInstaller.__main__
import os

config_images = []
config_images=os.listdir('images')
for fileX in config_images[:]: # filelist[:] makes a copy of filelist.
    if not(fileX.endswith(".png")):
        config_images.remove(fileX)
config_images = map(lambda fx : '--add-data=' + os.path.abspath('images') + "\\" + fx + ':img' , config_images )

config_data = []
config_data.append('--noconfirm')

generate_type = 4
#generate_type = int(input("Enter exe config type : "))

#doesn't work because of windows defender
if(generate_type==1):
    config_data.append('grid_ui_qt.py')
    config_data.append('--onefile')
    config_data.append('--windowed')

#not preferred because it is slow and console is not preferred
elif (generate_type == 2):
    config_data.append('grid_ui_qt.py')
    config_data.append('--onefile')

#doesn't work because of windows defender
elif (generate_type == 3):
    config_data.append('grid_ui_qt.py')
    config_data.append('--windowed')

elif (generate_type == 4):
    config_data.append('grid_ui_qt.py')

config_data.extend(config_images)
PyInstaller.__main__.run(config_data)

if(int(input('Publish to server?'))==1):
    os.system(r'C:\Users\D097\source\repos\E3D_Grid\E3D_grid\publish_server.bat')

current_version : int = 0
version_file = r'\\10.40.10.46\itstrl\RELEASE\TCCLIVE\TeklaModules\ver.dat'
with open(version_file ,'+r') as file:
    current_version = int(file.read())
with open(version_file ,'+w') as file:
    file.write(str(current_version+1))