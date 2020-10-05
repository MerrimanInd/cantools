# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
sys.path.insert(0, 'D:\\GitHub\\cantools\\')
import cantools

import os

folder_path = r'D:\vcu-controls\Core\CAN\Powertrain Bus'
db_powertrain = cantools.database.load_file(folder_path + r'\Powertrain.dbc')
db_inverters = cantools.database.load_file(folder_path + r'\20200701_RMS PM_CAN_DB.dbc')

db_powertrain.merge_db(db_inverters)
# db_inverters.merge_db(db_powertrain)