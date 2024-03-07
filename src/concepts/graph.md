 # Directed Acyclic Graph

 Git stores it's snapshots, the commits, in a directed acyclic graph. In the
 sense of git this means:

 * Commits are linked to their parent commits (directed)
 * A commit can not be a child of itself, directly or indirectly (acyclic)

 Additionally:
 * A single commits can either have zero, one or two parents
 * But different commits can have the same parent
 * Only the first commit has no parent

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
