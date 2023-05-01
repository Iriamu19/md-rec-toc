# md-rec-toc

Recusersively make a markdown table of content of a folder.

## Example :

From this folder :


```
.
├── coucou.md
├── folder_1
│   ├── monday.md
│   ├── sub_folder_1
│   │   └── july.md
│   ├── sub folder 2
│   │   └── be happy.md
│   └── tuesday.md
├── hello.md
└── life is good.md
```

We get this :

```markdown
- [coucou](coucou.md)
- folder_1
    - [monday](folder_1/monday.md)
    - sub folder 2
        - [be happy](folder_1/sub folder 2/be happy.md)
    - sub_folder_1
        - [july](folder_1/sub_folder_1/july.md)
    - [tuesday](folder_1/tuesday.md)
- [hello](hello.md)
- [life is good](life is good.md)
```
This was the normal mode.

## Modes

There are two other modes :
- one without file extension (nice for gitlab wiki)

```
- [coucou](coucou)
- folder_1
    - [monday](folder_1/monday)
    - sub folder 2
        - [be happy](folder_1/sub folder 2/be happy)
    - sub_folder_1
        - [july](folder_1/sub_folder_1/july)
    - [tuesday](folder_1/tuesday)
- [hello](hello)
- [life is good](life is good)
```

- one with "%20" instead of spaces in file path (nice for Obsidian)

```
    - sub folder 2
        - [be happy](folder_1/sub%20folder%202/be%20happy.md)
- [life is good](life%20is%20good.md)
```

Both modes can be combined.