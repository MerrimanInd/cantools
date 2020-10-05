# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:04:17 2020

@author: xcesari
"""
"""
import cantools
"""

import sys
sys.path.insert(0, 'D:\\GitHub\\cantools\\')
import cantools

import os
import tkinter as tk
from tkinter import filedialog

def scanForBusFolders(dirPath,searchSubDirectory=True):
    # Create a db object
    db = cantools.database.can.Database()
    foundDBC = False    # flag to skip write if no DBCs
    
    for file in os.listdir(dirPath):
        #filename = os.fsdecode(file)
        filename = str(file)
        
        
        if os.path.isfile(os.path.join(dirPath,file)):
            if filename.endswith('.dbc') and not filename.endswith('merged.dbc'):
                print('Found a DBC file: ' + filename)
                foundDBC = True
                
                # Do the thing to the DBC file
                DBCpath = os.path.join(dirPath,filename)
                db.merge_dbc_file(DBCpath)
                db.refresh()
                
        elif os.path.isdir(os.path.join(dirPath,file)):
            print('Found a folder: ' + dirPath + '/' + file)

            if searchSubDirectory:
                scanForBusFolders(dirPath + '/' + file)
            else:
                print('Found neither :/')
    
    if foundDBC:
        mergedDB = dirPath + '\\' + os.path.split(dirPath)[1] + '_merged.dbc'
        # Check if a previous version of the merged file exists and delete it
        if os.path.exists(mergedDB):
            print('Removing an earlier version of '+ os.path.split(dirPath)[1] + '_merged.dbc')
            os.remove(mergedDB)
        # Write db object
        cantools.database.dump_file(db,mergedDB)
        db = None


root = tk.Tk()
root.withdraw()

folder_path = filedialog.askdirectory()
scanForBusFolders(folder_path)
"""

folder_path = r'D:\vcu-controls\Core\CAN\Chassis Bus'
db_chassis = cantools.database.load_file(folder_path + r'\Chassis.dbc')
db_HProtocol = cantools.database.load_file(folder_path + r'\H-Protocol.dbc')

db_HProtocol.dbc.attribute_definitions
db_chassis.dbc.attribute_definitions
        
for key in db_HProtocol.dbc.attribute_definitions:
    if key in db_chassis.dbc.attribute_definitions:
        print(key)
"""