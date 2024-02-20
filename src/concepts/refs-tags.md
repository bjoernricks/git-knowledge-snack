# Tags

Git tags are the simplest reference. It's a static reference to a specific
commit.

```{mermaid}
---
caption: Example Git tag
---
%%{init: { 'gitGraph': {'showBranches': false}} }%%
gitGraph
    commit
    commit
    commit tag: "SomeTag"
    commit
```

The full tag reference is `refs/tags/<tag>` but can be abbreviated to just
`<tag>`.

For example:

```
git show --stat refs/tags/v0.1
# is the same as
git show --stat v0.1
```
