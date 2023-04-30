import pathlib

input_dir = pathlib.Path('test')

#les_md = test.rglob("*.md")
#print(list(les_md))

dossier =  input_dir
def listing(dossier):
    for item in dosser.iterdir()
        if item.is_dir():
            listing(item)
        else:
            full_path = item.relative_to('input_dir')
            indent = len(full_path.parts) - 1
            print(indent * "    " + "- [" + item.stem + "](" + full_path + ")" )

