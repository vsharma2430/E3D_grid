import PyInstaller.__main__
import os

config_images = []
config_images=os.listdir('images')
for fileX in config_images[:]: # filelist[:] makes a copy of filelist.
    if not(fileX.endswith(".png")):
        config_images.remove(fileX)
config_images = map(lambda fx : '--add-data=' + os.path.abspath('images') + "\\" + fx + ':img' , config_images )

config_data = []

generate_type = 3
#generate_type = int(input("Enter exe config type : "))

#Type 1 is not working some problem with pyinstaller
if(generate_type==1):
    config_data.append('grid_ui_qt.py')
    config_data.append('--onefile')
    config_data.append('--windowed')

#not preferred because it is slow and console is not preferred
elif (generate_type == 2):
    config_data.append('grid_ui_qt.py')
    config_data.append('--onefile')

#outgoing config generator
elif (generate_type == 3):
    config_data.append('grid_ui_qt.py')
    config_data.append('--windowed')

config_data.extend(config_images)
PyInstaller.__main__.run(config_data)
