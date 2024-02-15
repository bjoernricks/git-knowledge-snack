 # Directed Acyclic Graph

 A directed acyclic graph in the sense of git means

 * Commits reference their parents
 * Commits can either have zero, one or two parents
 * Only the first commit has no parent
 * A parent commit can not be a child of a commit (no cycles)

```{mermaid}
---
caption: Linear Graph
---
%%{init: { 'gitGraph': {'showBranches': false}} }%%
gitGraph
    commit id: "A"
    commit id: "B"
    commit id: "C"
```

```{mermaid}
---
caption: Forked Graph
---
%%{init: { 'gitGraph': {'showBranches': false}} }%%
gitGraph
    commit id: "A"
    commit id: "B"
    commit id: "C"
    branch dev
    commit id: "D"
    checkout main
    commit id: "E"
```

```{mermaid}
---
caption: Merged Graph
---
%%{init: { 'gitGraph': {'showBranches': false}} }%%
gitGraph
    commit id: "A"
    commit id: "B"
    commit id: "C"
    branch develop
    checkout develop
    commit id: "D"
    commit id: "E"
    checkout main
    merge develop id: "F"
    commit id: "G"
    commit id: "H"
```

```{mermaid}
---
caption: Merged Graph
---
%%{init: { 'gitGraph': {'showBranches': false}} }%%
gitGraph
    commit id: "A"
    commit id: "B"
    commit id: "C"
    branch develop
    checkout develop
    commit id: "D"
    commit id: "E"
    branch feature
    checkout feature
    commit id: "F"
    checkout main
    commit id: "G"
    merge develop id: "H"
    merge feature id: "I"
    commit id: "J"
```
