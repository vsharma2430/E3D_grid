import subprocess

def copy2clip(txt:str):
    print('Copying to clipboard')
    cmd='echo '+txt+'|clip'
    return subprocess.check_call(cmd, shell=True)