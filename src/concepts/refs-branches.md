# Branches

Git branches are very similar to tags except they are dynamic instead of static.
Specific git operations like `git pull` change a branch reference automatically.
A branch reference points to the head commit of a graph of commits.

```{mermaid}
---
caption: Example Git branches
---
gitGraph
    commit
    commit
    commit
    branch feature-a
    checkout feature-a
    commit
    commit
```

The full branch reference is `refs/heads/<branch>` but can be abbreviated to
just `<branch>`.

For example:

```
git show --stat refs/heads/main
# is the same as
git show --stat main
```
