# Git Objects

Git has several different objects. Most important is the git commit. To
understand all objects we need to take a look at the git commit in detail.

## What's a Git Commit?

A git commit is a snapshot of the change information (who, what, when, why,
parent) and a file and directory hierarchy (**Git tree**). This hierarchy
includes the contents of the files (**Git blob**).

So a commit actually consists of three git objects,

1. the git commit object itself,
2. the git tree objects,
3. and the git blob objects

Every object is identified by its hash. The hash is calculated using SHA-1 and
includes the hashes of all linked objects.


```{toctree}
blob
tree
commit
```
