# Git Objects

## What's a Git Commit?

A git commit is a snapshot of the change information, hierarchy (**Git tree**),
including the contents of the files (**Git blob**) in a Git repository.

Every object (Git commit, Git tree, Git blob) is identified by it's hashsum.
The hashsum is calculated with SHA-1 and includes the hashsums of all linked
objects.


```{toctree}
blob
tree
commit
```
