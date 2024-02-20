# HEAD

The HEAD is a special dynamic reference pointing to the branch you’re currently
working on. It can be used when the latest checked out commit has to be
referenced.

```{mermaid}
---
caption: Example Git HEAD
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
    merge BranchA id: "HEAD"
```
