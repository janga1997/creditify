import sys

directory = sys.argv[1]
author = sys.argv[2]

import os

for dname, dirs,files in os.walk(directory):
    for file in files:
        if file.endswith('.py'):
            print '\n'
            f = open(os.path.join(dname, file),'r+')
            lines = f.readlines() # read old content
            f.seek(0) # go back to the beginning of the file
            f.write("__author__ = '"+ author +"'\n\n") # write new content at the beginning
            for line in lines: # write old content after new
                f.write(line)
            f.close()
