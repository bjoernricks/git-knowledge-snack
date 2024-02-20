# Git to Rule the World

To mitigate these consequences distributed version control systems like git were
created. Instead of relying on a client/server architecture, a peer-to-peer like
approach is used.

Changes and advantages:

* A single git repository includes all meta information about the contained code
  changes
* Snapshots of the code can be created locally without a network connection
* Code changes can be *pushed* to and *pulled* from everywhere
* Every code change can be inspected locally anytime without network connection
* Information is distributed between different *clones* of the repository
    * Doesn't mean all repositories share all information
    * Repositories may hold only parts of the code changes
* There is no single *source of truth* for a repository anymore
    * Every repository can be the *master*
    * There doesn't need to be a *master*

```{mermaid}
flowchart LR
    A[(Repo A)] --> C[(Repo C)]
    B[(Repo B)] --> C
    B <--> A
    C --> A
```

Because of these advantages git conquered the world of version control systems.
