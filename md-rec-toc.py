#!/usr/bin/env python

import sys
import pathlib
import re
import argparse

######## main recursive function #######
def toc(folder):
    
    list = folder.iterdir()
    sorted_list = sorted(list) # sort by alphabetic order

    for item in sorted_list:
        indent_nb = len(item.parts) - 1

        if item.is_dir():
            print(indent_nb * "    " + "- " + item.stem)
            toc(item)
        else:
            if no_space:
                path = str(item).replace(' ', '%20')
            else:
                path = str(item)
            
            if no_file_ext:
                path = re.sub('\.[a-z]{2,3}$', '', path) 
            
            print(indent_nb * "    " + "- [" + item.stem + "](" + path + ")" )

######## manage command line argument ########

parser = argparse.ArgumentParser(description="Recursively generate a table of content of a folder containing markdown files",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-s", "--no-space", action="store_true", help="print %%20 instead of spaces in filepath")
parser.add_argument("-e", "--no-file-ext", action="store_true", help="remove file extension in path")
parser.add_argument("dir", help="directory from wich generating the toc")

args = vars(parser.parse_args())

no_space = args["no_space"]
no_file_ext = args["no_file_ext"]
input_dir = pathlib.Path(args["dir"])

######## main part ########
# print the root folder if it is not the current directory
if input_dir != pathlib.Path("."):
    print(" - " + input_dir.stem)

# execute the main function                         
toc(input_dir)