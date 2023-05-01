#!/usr/bin/env python

import sys
import pathlib
import re

mode = 'obsidian'

# main recursive function
def toc(folder):
    
    list = folder.iterdir()
    sorted_list = sorted(list) # sort by alphabetic order

    for item in sorted_list:
        indent_nb = len(item.parts) - 1

        if item.is_dir():
            print(indent_nb * "    " + "- " + item.stem)
            toc(item)
        else:
            if mode == 'obsidian':
                print(indent_nb * "    " + "- [" + item.stem + "](" + str(item).replace(' ', '%20') + ")" )
            elif mode == 'wiki_gitlab':
                path_with_no_ext = re.sub('\.[a-z]{2,3}$', '', str(item)) 
                print(indent_nb * "    " + "- [" + item.stem + "](" + path_with_no_ext + ")" )
            else:
                print(indent_nb * "    " + "- [" + item.stem + "](" + str(item) + ")" )

# manage command line argument

if len(sys.argv) == 0:
    print("directory missing")
    quit()

if len(sys.argv) > 2:
    print("accept only one directory ")
    quit()

input_dir = pathlib.Path(sys.argv[1])

if not input_dir.exists():
    print("this directory doesn't exist")
    quit()

# print the root folder if it is not the current directory
if input_dir != pathlib.PurePath("."):
    print(" - " + input_dir.stem)

# execute the main function                         
toc(input_dir)