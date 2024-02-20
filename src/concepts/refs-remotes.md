# Remotes

A git remote reference points to a branch of a remote repository.

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
    branch BranchA
    checkout BranchA
    commit
    commit
    checkout main
    merge BranchA
```
