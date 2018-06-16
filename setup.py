# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 23:47:39 2018

@author: guest11
"""

import cx_Freeze
import os
os.environ['TCL_LIBRARY'] = "C:\\ProgramData\\Anaconda3\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\ProgramData\\Anaconda3\\tcl\\tk8.6"

executables =[cx_Freeze.Executable("race-pygame.py")]

cx_Freeze.setup(
        name = "A bit Racey",
        options={"build_exe":{"packages":["pygame"],
                              "include_files":["race_car.png"]}},
        executables = executables,
        version='1.0.0'
        )

#python setup.py build
#python setup.py bdist_msi