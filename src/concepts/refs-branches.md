# Branches

Git branches are very similar to tags except they are dynamic instead of static.
Specific git operations change a branch reference.

```{mermaid}
---
caption: Example Git branches
---
gitGraph
    commit
    commit
    commit
    branch BranchA
    checkout BranchA
    commit
    commit
```
