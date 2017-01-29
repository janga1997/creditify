#! /usr/bin/env python

import sys
import os

from bs4 import BeautifulSoup

filetype = sys.argv[1]
directory = sys.argv[2]
author = sys.argv[3]

for dname, dirs,files in os.walk(directory):
    for file in files:
        if file.endswith('.'+filetype):
            f = open(os.path.join(dname, file),'r+')
            if filetype == 'py':
                lines = f.readlines() # read old content
                f.seek(0) # go back to the beginning of the file
                f.write("__author__ = '"+ author +"'\n\n") # write new content at the beginning
                for line in lines: # write old content after new
                    f.write(line)

            elif filetype == 'html':
                soup = BeautifulSoup(f.read())
                title = soup.find('title')
                meta = soup.new_tag('meta')
                meta['author'] = author
                title.insert_after(meta)
                f.seek(0)
                f.write(soup.prettify())
            f.close()
