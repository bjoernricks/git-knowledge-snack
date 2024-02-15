# Git Commit

A git commit is a snapshot of the change information, hierarchy (Git tree),
including the contents of the files (Git blob) in a Git repository.

```
> git ls-tree b320f9bf554f56fd8dcad2db30bc02f23e2f90cd
100644 blob 8396654bc46dfc2e35b3e039895ef41017cd27ef    .gitignore
100644 blob f288702d2fa16d3cdf0035b15a9fcbc552cd88e7    LICENSE
100644 blob d67b8618f193c63b97b9a7a62e90157eeab2684b    Makefile
100644 blob fc06a0b33a8b78f94e76c869cbb1159838264458    README.md
100644 blob 0c426f5978f8df4de07b977038e41024c129f56b    poetry.lock
100644 blob c101f8a088333e882ee9c7bc1fb5fb75320f91e4    pyproject.toml
040000 tree 91cb9aba1a3b41f362a225f2e5b6433316bed0e7    src
```

```
> git ls-tree 91cb9aba1a3b41f362a225f2e5b6433316bed0e7
040000 tree 315da460c7ad9696f82ddb13bea6eca61aaa44bc    _static
040000 tree e3869c4f5ffd97645ece7b066358d1e052a37e4c    add
040000 tree ca2de8021adba336a944495cf3b04a30b44019f5    adjust
100644 blob 3f56108820ce214055858e11eef03c3a1768caa9    agenda.md
040000 tree db2e22d577a3dfa56203877cad1ddb32328b3d0a    concepts
100644 blob 273138e091c41abef5f38337b04a20a024082b32    conf.py
040000 tree 36faf1153c12b0c339a04937533e9ab5eb518880    config
100644 blob 47f769ac172a5dc945cc3b0feee68bcccf3d4ddc    favicon.png
100644 blob b67e55de02f413804ec84e33905834124ac997a5    index.md
100644 blob 3a8533197b5fdc33a1b9c8fa41082ffa25314b54    introduction.md
100644 blob f24398e79be1d689ff741b45b91f2167911d7bdf    next.md
040000 tree 26be82717c6b3f7760e46fa4173c4adca7720f38    revert
```
