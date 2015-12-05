#!/usr/bin/python3

# Programmer   :  Kyle Kloberdanz
# Date Created :  08 APR 2015
# Description  :  This program will create a wave form when run.
#                 To run on linux: open the terminal,
#                 then type 'python3 triangles.py'    

import time
import shutil


x = 1
DELAY = 0.005 # seconds
while x < 10000:
    width, height = shutil.get_terminal_size()
    SIZE = width # maximum length of stars

    j = 1
    i = 1
    time.sleep(DELAY)
    while i < SIZE:
        time.sleep(DELAY)
        while j < i:        
                time.sleep(DELAY)
                print(j * "*")
                j += 1

        while j > 0:
                time.sleep(DELAY)
                print(j * "*")
                j -= 1
        i += 1

    while i > 0:
        time.sleep(DELAY)
        while j < i:        
                time.sleep(DELAY)
                print(j * "*")
                j += 1

        while j > 0:
                time.sleep(DELAY)
                print(j * "*")
                j -= 1

        i -= 1
    
    x += 1 
