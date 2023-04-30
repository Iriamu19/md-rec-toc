# md-rec-toc

Make a markdown table of content of a folder recusersively.

## Example :

From this :

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

## To-do

- List in alphabetic order