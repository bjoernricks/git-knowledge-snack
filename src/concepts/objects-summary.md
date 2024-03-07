# Git Objects - Summary

* Every object in git is identified by its SHA-1 sum.
* A git tree includes the hashes of all blobs and sub trees in its hash calculation.
* A git commit includes the hashes of the saved tree and the parent commit.

In conclusion if a single bit of a file or even in a commit gets manipulated the
whole graph of commits will be invalid because all hashes will change.

Git ensures the integrity of your repository and change history.
