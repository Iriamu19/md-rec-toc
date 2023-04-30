import sys
import pathlib

# main recursive function
def listing(folder):
    for item in folder.iterdir():

        indent_nb = len(item.parts) - 2

        if item.is_dir():
            print(indent_nb * "    " + "- " + item.stem)
            listing(item)
        else:
            print(indent_nb * "    " + "- [" + item.stem + "](" + str(item) + ")" )

# manage command line argument

if len(sys.argv) == 0:
    print("directory missing")
    quit()

if len(sys.argv) > 2:
    print("accept only one directory ")

input_dir = pathlib.Path(sys.argv[1])

if not input_dir.exists():
    print("this directory doesn't exist")
    quit()

# execute the main function                         
listing(input_dir)