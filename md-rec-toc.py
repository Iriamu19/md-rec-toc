import pathlib

input_dir = pathlib.Path('test')

#les_md = test.rglob("*.md")
#print(list(les_md))


def listing(dossier):
    for item in dossier.iterdir():

        indent = len(item.parts) - 2

        if item.is_dir():
            print(indent * "    " + "- " + item.stem)
            listing(item)
        else:
            print(indent * "    " + "- [" + item.stem + "](" + str(item) + ")" )

listing(input_dir)