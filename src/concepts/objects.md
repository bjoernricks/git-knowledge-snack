# Git Objects

Git has several different objects. Most important is the git commit. To
understand the objects we need to take a look at the git commit in detail.

## What's a Git Commit?

A git commit is a snapshot of the change information (Who, What, When, Why),
file and directory hierarchy (**Git tree**), including the contents of the files
(**Git blob**) in a Git repository.

So a commit actually consists of three git objects,

1. the git commit object itself,
2. the git tree,
3. and the git blob objects

Every object is identified by it's hashsum. The hashsum is calculated using
SHA-1 and includes the hashsums of all linked objects.


```{toctree}
blob
tree
commit
```
