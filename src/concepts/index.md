# Git Concepts

* Git is a [**Distributed Version Control System**](https://en.wikipedia.org/wiki/Distributed_version_control).
* A **version control system** saves the state of current source files.
* Every state is stored in a snapshot, the so called **commit**.
* The commits form a [**directed acyclic graph**](https://en.wikipedia.org/wiki/Directed_acyclic_graph).
* Git uses different **objects** to store information
* Every git object is identified by a **hashsum**, a SHA-1 hash.
* To not having to remember hashes when referring to commits, git provides **references**.
* All git information about a repository is contained in a **single `.git` directory**


```{toctree}
:hidden:

distributed
graph
objects
objects-example
objects-summary
references
references-summary
git-dir-references
git-dir-objects
```

