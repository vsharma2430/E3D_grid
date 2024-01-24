#STEPS TO GENERATE EXECUTABLE
"""
1.
INSTALL PYTHON

2.
USE PIP TO INSTALL VIRTUAL ENV - pip install virtualenv

3.
MAKE VIRTUAL ENV -  python<version> -m venv env 
                or
MAKE VIRTUAL ENV -  py -m venv env 
ACTIVATE VIRTUAL ENV - env/Scripts/activate.bat 

4.
{
INSTALL REQUIREMENTS IN VIRTUAL ENV - pip install -r requirements.txt
GENERATE EXE FILE - pyinstaller grid_ui.py
}
or
{
RUN generate_exec.bat
}
Executable is generated in dist folder

//EXTRAS
* On adding new dependencies/external libraries
    Generate requirements.txt
    pip freeze > requirements.txt
"""
import os
import tkinter as tk 
from tkinter import messagebox
from grid_base.grid import grid_data,getGridList
from grid_base.point import point
from grid_base.grid_base import build_macro
from misc.calc_time import calculate_time
from misc.clipboard import copy2clip
from misc.file_UI import readLineByLine
from misc.tkinter_dialog import saveFile_win_mac

saveLoc = os.getenv('LOCALAPPDATA') + r"\GridPy"
saveFile = saveLoc+ r"\db.dat"

#Create local app data folder for UI data save
if(not os.path.isdir(saveLoc)):
    os.mkdir(saveLoc)

def createUI():

    #WINDOW EVENT FUNCTIONS : 

    def selectOutputFile():
        output_file = saveFile_win_mac()
        input_file.delete(1.0,"end")
        input_file.insert(tk.END,output_file)

    def sel():
        if(str(var.get())=="1"):
            print("You selected the option - New")
        else:
            print("You selected the option - Old")

    # Top level window 
    frame = tk.Tk() 
    frame.title("Grid E3D 1.1") 
    frame.geometry('800x350') 

    label_width = 10
    input_width = 80

    framereference = tk.Frame(frame)
    label_reference = tk.Label(framereference, text = "Reference ",width=label_width,justify="left",anchor="w") 
    label_reference.pack(side="left")
    framereferenceInput=tk.Frame(framereference)
    input_reference_name = tk.Text(framereferenceInput, height = 1, width=int(input_width*0.2374))
    input_reference_X = tk.Text(framereferenceInput, height = 1, width=int(input_width*0.25))
    input_reference_Y = tk.Text(framereferenceInput, height = 1, width=int(input_width*0.25))
    input_reference_Z = tk.Text(framereferenceInput, height = 1, width=int(input_width*0.25))
    input_reference_name.pack(side="left",padx=0,pady=0)
    input_reference_X.pack(side="left",padx=0,pady=0)
    input_reference_Y.pack(side="left",padx=0,pady=0)
    input_reference_Z.pack(side="left",padx=0,pady=0)
    framereferenceInput.pack(side="left",padx=0,pady=0)
    framereference.pack(padx=0,pady=0)

    frameGridX = tk.Frame(frame)
    label_gridX = tk.Label(frameGridX, text = "X Axis",width=label_width,justify="left",anchor="w") 
    label_gridX.pack(side="left")
    frameGridXInput=tk.Frame(frameGridX)
    input_gridX_name = tk.Text(frameGridXInput, height = 1, width=input_width)
    input_gridX_value = tk.Text(frameGridXInput, height = 1, width=input_width)
    input_gridX_value.pack(side="top")
    input_gridX_name.pack(side="top")
    frameGridXInput.pack(side="left")
    frameGridX.pack(padx=5,pady=5)

    frameGridY = tk.Frame(frame)
    label_gridY = tk.Label(frameGridY, text = "Y Axis",width=label_width,justify="left",anchor="w") 
    label_gridY.pack(side="left")
    frameGridYInput=tk.Frame(frameGridY)
    input_gridY_name = tk.Text(frameGridYInput, height = 1, width=input_width)
    input_gridY_value = tk.Text(frameGridYInput, height = 1, width=input_width)
    input_gridY_value.pack(side="top")
    input_gridY_name.pack(side="top")
    frameGridYInput.pack(side="left")
    frameGridY.pack(padx=5,pady=5)

    frameGridZ = tk.Frame(frame)
    label_gridZ = tk.Label(frameGridZ, text = "Z Axis",width=label_width,justify="left",anchor="w") 
    label_gridZ.pack(side="left")
    frameGridZInput=tk.Frame(frameGridZ)
    input_gridZ_name = tk.Text(frameGridZInput, height = 1, width=input_width)
    input_gridZ_value = tk.Text(frameGridZInput, height = 1, width=input_width)
    input_gridZ_value.pack(side="top")
    input_gridZ_name.pack(side="top")
    frameGridZInput.pack(side="left")
    frameGridZ.pack(padx=5,pady=5)

    var = tk.IntVar()
    frameGridType = tk.Frame(frame)
    label_GridType = tk.Label(frameGridType, text = "Grid Type",width=label_width,justify="left",anchor="w") 
    label_GridType.pack(side="left")
    frameGridTypeInput=tk.Frame(frameGridType)
    input_GridType_New = tk.Radiobutton(frameGridTypeInput, text="New", variable=var, value=1, command=sel,width=int(input_width*0.53),anchor=tk.W)
    input_GridType_New.select()
    input_GridType_Old = tk.Radiobutton(frameGridTypeInput, text="Old", variable=var, value=2, command=sel,width=int(input_width*0.53),anchor=tk.W)
    input_GridType_New.pack(side="left",anchor=tk.W)
    input_GridType_Old.pack(side="left",anchor=tk.W)
    frameGridTypeInput.pack(side="left",anchor=tk.W)
    frameGridType.pack(padx=5,pady=5)

    frameOutput = tk.Frame(frame)
    labelFile = tk.Label(frameOutput, text = "Output",width=label_width,justify="left",anchor="w")  
    input_file = tk.Text(frameOutput, height = 1, width = int(input_width*0.8)) 
    input_button = tk.Button(frameOutput, text = "Select", command = lambda:selectOutputFile(),width=int(input_width*0.2),height=1) 
    labelFile.pack(side="left",padx=0,pady=0)
    input_file.pack(side="left",padx=0,pady=0)
    input_button.pack(side="left",padx=0,pady=0)
    frameOutput.pack(padx=5,pady=5)

    frameEIL = tk.Frame(frame)
    lblName1 = tk.Label(frameEIL, text = "Developed with ❤ by Vaibhav Sharma",font=("Monospace MS",10) ,anchor="w",width=50)  
    lblName2 = tk.Label(frameEIL, text = "© Engineers India Limited",font=("Monospace MS", 10) ,anchor="e",width=50) 
    lblName1.pack(side="left")
    lblName2.pack(side="right")

    def defaultData (): 
        print('Loading default input')
        input_reference_name.insert(1.0,'MYGRID')
        input_reference_X.insert(1.0,'1000')
        input_reference_Y.insert(1.0,'2000')
        input_reference_Z.insert(1.0,'3000')
        input_gridX_name.insert(1.0,'A B C D')
        input_gridX_value.insert(1.0,'0 1000 2*2000')
        input_gridY_name.insert(1.0,'1 2 3')
        input_gridY_value.insert(1.0,'0 2*2500')
        input_gridZ_name.insert(1.0,'1')
        input_gridZ_value.insert(1.0,'0')
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
        input_file.insert(1.0,desktop+r'\macro.mac')

    @calculate_time
    def generate_macro(): 
        gridXName = input_gridX_name.get(1.0, tk.END).strip() 
        gridYName = input_gridY_name.get(1.0, tk.END).strip() 
        gridZName = input_gridZ_name.get(1.0, tk.END).strip()  
        gridXVal = input_gridX_value.get(1.0, tk.END).strip()  
        gridYVal = input_gridY_value.get(1.0, tk.END).strip()  
        gridZVal = input_gridZ_value.get(1.0, tk.END).strip()  
        grid_refX = float(input_reference_X.get(1.0, tk.END).strip() )
        grid_refY = float(input_reference_Y.get(1.0, tk.END).strip() )
        grid_refZ = float(input_reference_Z.get(1.0, tk.END).strip() )
        grid_ref_name = input_reference_name.get(1.0, tk.END).strip()  
        out_file_location = input_file.get(1.0, tk.END).strip()  
        grid_ref = grid_data(label='/'+grid_ref_name,delta=point(grid_refX,grid_refY,grid_refZ))
        x_grid = getGridList(grid_names=gridXName,grid_values=gridXVal,dir=1)
        y_grid = getGridList(grid_names=gridYName,grid_values=gridYVal,dir=2)
        z_grid = getGridList(grid_names=gridZName,grid_values=gridZVal,dir=3)
        new_old = True if (str(var.get())=='1') else False

        pml_command :str = build_macro(grid_ref,x_grid,y_grid,z_grid,new_old,out_file_location)
        copy2clip(pml_command)

        print('PML command copied to clipboard.Paste in command window of E3D to create grids.')
        return

    # Button Creation 
    createButton = tk.Button(frame, text = "Create Macro",  command = generate_macro,width=25,height=2) 
    createButton.pack(padx=10,pady=10) 
    frameEIL.pack(padx=5,pady=5,anchor=tk.S)

    def loadUIData():
        if(os.path.exists(saveFile)):
            print('Loading last input')
            saveData = readLineByLine(saveFile)
            size = len(saveData)
            if(size>9):
                input_reference_name.insert(1.0,saveData[0])
                input_reference_X.insert(1.0,saveData[1])
                input_reference_Y.insert(1.0,saveData[2])
                input_reference_Z.insert(1.0,saveData[3])
                input_gridX_name.insert(1.0,saveData[4])
                input_gridX_value.insert(1.0,saveData[5])
                input_gridY_name.insert(1.0,saveData[6])
                input_gridY_value.insert(1.0,saveData[7])
                input_gridZ_name.insert(1.0,saveData[8])
                input_gridZ_value.insert(1.0,saveData[9])
                input_file.insert(1.0,saveData[10])
            else:
                defaultData()
        else:
            defaultData()

    def saveUIData():
        save_data = []
        grid_ref_name = input_reference_name.get(1.0, tk.END).strip()  
        grid_refX = input_reference_X.get(1.0, tk.END).strip()
        grid_refY = input_reference_Y.get(1.0, tk.END).strip()
        grid_refZ = input_reference_Z.get(1.0, tk.END).strip()
        gridXName = input_gridX_name.get(1.0, tk.END).strip() 
        gridXVal = input_gridX_value.get(1.0, tk.END).strip()  
        gridYName = input_gridY_name.get(1.0, tk.END).strip() 
        gridYVal = input_gridY_value.get(1.0, tk.END).strip()  
        gridZName = input_gridZ_name.get(1.0, tk.END).strip()  
        gridZVal = input_gridZ_value.get(1.0, tk.END).strip()  
        out_file_location = input_file.get(1.0, tk.END).strip()  
        save_data.append(grid_ref_name)
        save_data.append(grid_refX)
        save_data.append(grid_refY)
        save_data.append(grid_refZ)
        save_data.append(gridXName)
        save_data.append(gridXVal)
        save_data.append(gridYName)
        save_data.append(gridYVal)
        save_data.append(gridZName)
        save_data.append(gridZVal)
        save_data.append(out_file_location)

        print("Saving last input")
        f = open(saveFile,'w')
        f.write('\n'.join(save_data))
        f.close()
        return

    def on_closing():
        saveUIData()
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            frame.destroy()
            exit

    loadUIData()
    frame.protocol("WM_DELETE_WINDOW", on_closing)
    frame.mainloop() 

createUI()