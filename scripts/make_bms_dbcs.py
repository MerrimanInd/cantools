# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 17:22:06 2020

@author: xcesari
"""

import sys
sys.path.insert(0, 'D:\\GitHub\\cantools\\')
import cantools

import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# base_dbc = filedialog.askopenfilename()
base_dbc = r'D:\stafl dbc\BMS1000M Internal CAN Protocol - A0.dbc'
folder = os.path.split(base_dbc)[0]
file = os.path.split(base_dbc)[1]
db = cantools.database.load_file(base_dbc)

for i in range(7):
    # iterate 7 times to create the sub BMS DBCs
    for message in db.messages:
        message.frame_id += 0x01
        
    newFileName = str.split(file,'.')[0] + '_offset0x0'+ str(i+1) + '.' + str.split(file,'.')[1]
    print(folder + '\\' + newFileName)
    cantools.database.dump_file(db,folder + '\\' + newFileName)
