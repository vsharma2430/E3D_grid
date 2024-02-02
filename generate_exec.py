import PyInstaller.__main__
import os
from misc.increment_version import increment_tcc_ver

def generate_exec():
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

if(input('Generate new executable [Y/n] ? [n] ')=='Y'):
    generate_exec()
    print('Exectutable generated')

if(input('Publish to server [Y/n] ? [n] ')=='Y'):
    os.system(r'C:\Users\D097\source\repos\E3D_Grid\E3D_grid\publish_server.bat')
    increment_tcc_ver()
    print('Exectutable published')