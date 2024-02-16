# Git Commit

A git commit contains the hashsum of the tree, parent commit and the commit
information.

```{mermaid}
flowchart TD
    B([commit 2]) --> C([commit 1])
    B --> D[tree 2]
    C --> E[tree 1]
    D ---> |LICENSE| F(blob)
    E ---> |LICENSE| F(blob)
    E ---> |README| G(blob)
    D ---> |README| H(blob)
```

It's format is

```{code-block}
---
caption: Internal format of a git commit
---
commit {size}
tree {tree hashsum}
parent {parent commit hashsum}
author {author name} <{author email}> {date}
committer {committer name} <{committer email}> {date}
{additional commit information}

{commit message}
```

The hashsum is calculated as follows

```{code-block} python
---
caption: Incomplete Python pseudocode for calculating the git commit hash
---

commit_content = f"tree {tree.binary_sha1}\nparent {parent_commit.binary_sha1}\n{commit_information}"
commit_data = f"commit {len(commit_content.encode())} \0{commit_content}\n"
hashsum = sha1(commit_data.encode()).hexdigest()
```

Sources:

* [https://git-scm.com/book/en/v2/Git-Internals-Git-Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)
* [https://stackoverflow.com/questions/35430584/how-is-the-git-hash-calculated](https://stackoverflow.com/questions/35430584/how-is-the-git-hash-calculated)
