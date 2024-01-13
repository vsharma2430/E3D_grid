This application is created for generating PML command to model grids in E3D.


STEPS TO CREATE VIRTUAL ENV
1. Create env
    <python_location> -m venv env
    C:\Users\D097\AppData\Local\Programs\Python\Python39\python.exe -m venv env
2. Install requirements to venv
    pip install -r requirements.txt
3. Create Executable
    generate_exec.py
    OR
    pyinstaller grid_ui.py --onefile --windowed

MISC STEPS
* Freeze requirements (for developer)
    pip freeze > requirements.txt
* PyQt Designer
    pyqt5-tools designer
* Convert ui file to py file 
    python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py
    python -m PyQt5.uic.pyuic -x ui/mainWin.ui -o ui/mainWin.py

GIT Steps
1. Clone Repository
    git clone https://gitlab.eil.co.in/structural/e3d_grids.git
2. Commit 
    git add .
    git commit -m "<message>"
3. Push
    git push origin main
4. Get remotes
    git remote -v