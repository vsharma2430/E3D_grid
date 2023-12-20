import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

lic_file = r'\\e3d-ggn\AVEVA\AVEVA LICENSING SYSTEM\RMS\lsreserv_AVEVA'

f = open(lic_file, "r")

lic_user_map = {}

for line in f.read().splitlines():
    if('STRLDA' in line or 'STRLAS' in line):
        line_split = line.split(':')
        lic_type = line_split[0]
        users_list = line_split[len(line_split)-1]
        lic_user_map[lic_type] = users_list

print(lic_user_map)
