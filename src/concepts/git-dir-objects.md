# The `.git` Directory - Objects

The git objects are stored within the `.git` directory too.

```sh
$ ls .git/
branches  COMMIT_EDITMSG  config  description  FETCH_HEAD  HEAD  hooks  index  info  logs  objects  refs

# Examine the objects directory
$ ls .git/objects
05  0c  0f  16  27  2f  31  36  3a  3e  47  4e  52  57  5b  60  64  71  7b  7d  83  89  91  9c  a5  aa  b4  b8  bf  c2  c8  d0  db  e2  e5  e8  f5  f9  info
06  0e  11  26  29  30  35  39  3b  3f  48  50  56  58  5e  62  6b  78  7c  81  86  8c  9b  a3  a9  b3  b6  be  c1  c5  ca  d6  e1  e3  e7  f2  f7  fc  pack

# Get a git object hash
$ cat .git/refs/heads/main
6227630dd590a9c3c6014eed15a18a639448f86d

# there is no file at .git/objects/6227630dd590a9c3c6014eed15a18a639448f86d
# but a directory starting named 62
$ ls .git/objects/62
27630dd590a9c3c6014eed15a18a639448f86d

# looks like we found our commit
$ file .git/objects/62/27630dd590a9c3c6014eed15a18a639448f86d
.git/objects/62/27630dd590a9c3c6014eed15a18a639448f86d: zlib compressed data

# show content of that zlib compressed file with a simple Python script
$ ./git-zlib.py .git/objects/62/27630dd590a9c3c6014eed15a18a639448f86d
commit 717tree 649cbf3d33418503dc23d2fbbe8a4ac9f35947d7
parent e70ee22490cb31fed27240ca35b7cfd6f44307b7
author Björn Ricks <bjoern.ricks@greenbone.net> 1708089746 +0100
committer Björn Ricks <bjoern.ricks@greenbone.net> 1708089746 +0100
gpgsig -----BEGIN SSH SIGNATURE-----
 U1NIU0lHAAAAAQAAAH8AAAAic2stZWNkc2Etc2hhMi1uaXN0cDI1NkBvcGVuc3NoLmNvbQ
 AAAAhuaXN0cDI1NgAAAEEEO8opWOj6rxRQHsh4QZuMmbiD1fZ5tYA02MIDNKAI7ctXTX3q
 3HqQPum2qDiWC0ZzuRipXvDKHGhqxJPlQKXWQwAAAARzc2g6AAAAA2dpdAAAAAAAAAAGc2
 hhNTEyAAAAdwAAACJzay1lY2RzYS1zaGEyLW5pc3RwMjU2QG9wZW5zc2guY29tAAAASAAA
 ACAK+pM4xSkdNfMW/WBrNbEx0e//TtwkbUodRg0mV4bAIgAAACA3Bw2tKqCsvh5WM2+6C3
 KzdOWtK/5HTQq1ORfglWCI8wEAAGPG
 -----END SSH SIGNATURE-----

Change: Improve git concepts
```

This looks familiar, right?

