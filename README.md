# md-rec-toc

Recusersively make a markdown table of content of a folder.

## Example :

From this folder :

```
.
├── coucou.md
├── folder_1
│   ├── monday.md
│   ├── sub_folder_1
│   │   └── july.md
│   └── tuesday.md
└── hello.md
```

We get this :

```markdown
- folder_1
    - [monday](test/folder_1/monday.md)
    - [tuesday](test/folder_1/tuesday.md)
    - sub_folder_1
        - [july](test/folder_1/sub_folder_1/july.md)
- [hello](test/hello.md)
- [coucou](test/coucou.md)
```

## Modes

In the example you can see the normal mode.

There are two other modes :
- one without file extension (nice for gitlab wiki)
- one with "%20" instead of spaces in file path (nice for Obsidian)

Both modes can be combined.