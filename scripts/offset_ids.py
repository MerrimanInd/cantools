# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:53:44 2020

@author: xcesari
"""
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, 'D:\\GitHub\\cantools\\')
import cantools

import os
import tkinter as tk
from tkinter import filedialog

def scanForBusFolders(dirPath,searchSubDirectory=True):
    
    for file in os.listdir(dirPath):
        #filename = os.fsdecode(file)
        filename = str(file)
        
        
        if os.path.isfile(os.path.join(dirPath,file)):
            if filename.endswith('.dbc') and not filename.endswith('offset0x01.dbc'):
                print('Found a DBC file: ' + filename)
                
                # Do the thing to the DBC file
                DBCpath = os.path.join(dirPath,filename)
                db = cantools.database.can.Database()
                db = cantools.database.load_file(DBCpath)
                
                for message in db.messages:
                    message.frame_id += 0x01
                
                newFileName = str.split(file,'.')[0] + '_offset0x01.' + str.split(file,'.')[1]
                print(dirPath + '\\' + newFileName)
                cantools.database.dump_file(db,dirPath + '\\' + newFileName)
                """
                # write file
                offsetDB = dirPath + '\\' + os.path.split(dirPath)[1] + '\\' + filename + '_offset0x01.dbc'
                # Check if a previous version of the merged file exists and delete it
                if os.path.exists(offsetDB):
                    print('Removing an earlier version of '+ os.path.split(dirPath)[1] + '_offset0x01.dbc')
                    os.remove(offsetDB)
                # Write db object
                cantools.database.dump_file(db,offsetDB)
                db = None
                """
                
        elif os.path.isdir(os.path.join(dirPath,file)):
            print('Found a folder: ' + dirPath + '/' + file)

            if searchSubDirectory:
                scanForBusFolders(dirPath + '/' + file)
            else:
                print('Found neither :/')

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