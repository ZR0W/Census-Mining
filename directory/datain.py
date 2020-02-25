# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 21:24:30 2020

@author: Rowland Zhang
"""

def run():
    filename = "data/adult.data"
    file = open(filename, "r")
    if file.mode == "r":
        print("reading file: %s" % file.name)
        # contents = file.read()
        # print(contents)
        
        fileLines = file.readlines()
        
        for line in fileLines:
            line = line.strip()
            print(line)
            tuples = line.split(", ")
            create_obj(tuples)
        return
    else:
        print("Error in datain.run()")

def create_obj(tuples):
    for elem in tuples:
        pass
    pass
    