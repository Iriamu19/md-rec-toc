#!/usr/bin/env python

import sys
import pathlib

# main recursive function
def toc(folder):
    for item in folder.iterdir():
        indent_nb = len(item.parts) - 1

        if item.is_dir():
            print(indent_nb * "    " + "- " + item.stem)
            toc(item)
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