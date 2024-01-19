# About
This application is created for generating PML command to model grids in E3D.

Python version used - 3.9.13  
Python version supported - (3.0 to 3.9)
Pyqt5 designer supports 3.9 only.

## Steps for virtual env

1. Create virtual env <br>
<python_location> -m venv env <br>
C:\Users\D097\AppData\Local\Programs\Python\Python39\python.exe -m venv env

2. Install requirements to venv <br>
pip install -r <requirements file location> <br>
pip install -r developer_requirements.txt   <br>
pip install -r publish_requirements.txt

3. Create Executable <br>
generate_exec.py <br>
OR <br>
pyinstaller grid_ui.py 

## PyQt Steps

* Freeze requirements (for developer) <br>
pip freeze > requirements.txt

* PyQt Designer <br>
pyqt5-tools designer <ui_file_location>     <br>
pyqt5-tools designer ui/mainWin.ui

* Convert ui file to py file <br>
python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py <br>
python -m PyQt5.uic.pyuic -x ui/mainWin.ui -o ui/mainWin.py

## Git Steps

1. Clone Repository <br>
git clone <remote_location>     <br>
git clone https://gitlab.eil.co.in/structural/e3d_grids.git

2. Commit <br>
git add . <br>
git commit -m "<message>" 

3. Push <br>
git push origin main

4. Get remotes <br>
git remote -v

