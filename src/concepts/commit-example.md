# Git Commit - Example

```
> git cat-file commit 5b675b466c60ad3e7d0ce044445d7a300e404d2a
tree aabf9b570c38466c225f0e63de25f74b39391d40
parent b320f9bf554f56fd8dcad2db30bc02f23e2f90cd
author Björn Ricks <bjoern.ricks@greenbone.net> 1708008424 +0100
committer Björn Ricks <bjoern.ricks@greenbone.net> 1708008424 +0100
gpgsig -----BEGIN SSH SIGNATURE-----
 U1NIU0lHAAAAAQAAAH8AAAAic2stZWNkc2Etc2hhMi1uaXN0cDI1NkBvcGVuc3NoLmNvbQ
 AAAAhuaXN0cDI1NgAAAEEEO8opWOj6rxRQHsh4QZuMmbiD1fZ5tYA02MIDNKAI7ctXTX3q
 3HqQPum2qDiWC0ZzuRipXvDKHGhqxJPlQKXWQwAAAARzc2g6AAAAA2dpdAAAAAAAAAAGc2
 hhNTEyAAAAeAAAACJzay1lY2RzYS1zaGEyLW5pc3RwMjU2QG9wZW5zc2guY29tAAAASQAA
 ACEA4XJLN/nrl9hOp8zAMHocbr16l3pgBUjDP2PYerjmbHIAAAAgcg4jQy0WwwkUrk+bdz
 2thFSH+g+fTkxdwgkq6K3IJykBAABjpA==
 -----END SSH SIGNATURE-----

Change: Extend git commit chapter
```

```
> git ls-tree aabf9b570c38466c225f0e63de25f74b39391d40
100644 blob 8396654bc46dfc2e35b3e039895ef41017cd27ef    .gitignore
100644 blob f288702d2fa16d3cdf0035b15a9fcbc552cd88e7    LICENSE
100644 blob d67b8618f193c63b97b9a7a62e90157eeab2684b    Makefile
100644 blob fc06a0b33a8b78f94e76c869cbb1159838264458    README.md
100644 blob 0c426f5978f8df4de07b977038e41024c129f56b    poetry.lock
100644 blob c101f8a088333e882ee9c7bc1fb5fb75320f91e4    pyproject.toml
040000 tree a9793f86dcd6eedf8b5323b8f10d469415bbb43a    src
```

```
> git hash-object LICENSE
f288702d2fa16d3cdf0035b15a9fcbc552cd88e7
```

```
> git ls-tree a9793f86dcd6eedf8b5323b8f10d469415bbb43a
040000 tree 315da460c7ad9696f82ddb13bea6eca61aaa44bc    _static
040000 tree e3869c4f5ffd97645ece7b066358d1e052a37e4c    add
040000 tree ca2de8021adba336a944495cf3b04a30b44019f5    adjust
100644 blob 3f56108820ce214055858e11eef03c3a1768caa9    agenda.md
040000 tree 5e2862ac6ec083385377062de9ec2942eeac95e5    concepts
100644 blob 273138e091c41abef5f38337b04a20a024082b32    conf.py
040000 tree 36faf1153c12b0c339a04937533e9ab5eb518880    config
100644 blob 47f769ac172a5dc945cc3b0feee68bcccf3d4ddc    favicon.png
100644 blob b67e55de02f413804ec84e33905834124ac997a5    index.md
100644 blob 3a8533197b5fdc33a1b9c8fa41082ffa25314b54    introduction.md
100644 blob f24398e79be1d689ff741b45b91f2167911d7bdf    next.md
040000 tree 26be82717c6b3f7760e46fa4173c4adca7720f38    revert
```

```
> git cat-file commit b320f9bf554f56fd8dcad2db30bc02f23e2f90cd
tree be868bd5d2971e5c2e374bd79bfa678cce1b7673
author Björn Ricks <bjoern.ricks@greenbone.net> 1708007701 +0100
committer Björn Ricks <bjoern.ricks@greenbone.net> 1708007701 +0100
gpgsig -----BEGIN SSH SIGNATURE-----
 U1NIU0lHAAAAAQAAAH8AAAAic2stZWNkc2Etc2hhMi1uaXN0cDI1NkBvcGVuc3NoLmNvbQ
 AAAAhuaXN0cDI1NgAAAEEEO8opWOj6rxRQHsh4QZuMmbiD1fZ5tYA02MIDNKAI7ctXTX3q
 3HqQPum2qDiWC0ZzuRipXvDKHGhqxJPlQKXWQwAAAARzc2g6AAAAA2dpdAAAAAAAAAAGc2
 hhNTEyAAAAdwAAACJzay1lY2RzYS1zaGEyLW5pc3RwMjU2QG9wZW5zc2guY29tAAAASAAA
 ACBx5QfP3aO3zEaBvgtd7x6tpcmD4Tnq9QYsv5daTb2t1QAAACApdsBS9O0H6UTtl567HL
 8rjHy+0JxtQg6lMhh8XmqtMAEAAGOi
 -----END SSH SIGNATURE-----

Add: Initial commit
```
