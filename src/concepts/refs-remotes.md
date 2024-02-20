# Remotes

Another dynamic reference which gets changed automatically (`git fetch`). The
git remote reference points to the head commit of a branch in a remote
repository.

```{mermaid}
---
caption: Example Git branch from remote
---
gitGraph
    commit
    branch origin/feature-a
    commit
    commit
    commit
    branch feature-a
    checkout feature-a
    commit
    commit
    checkout main
    merge feature-a
```

The full remote reference is `refs/remotes/<remote>/<branch>` but can be
abbreviated to just `<remote>/<branch>`.

For example:

```
git show --stat refs/remotes/upstream/main
# is the same as
git show --stat upstream/main
```
