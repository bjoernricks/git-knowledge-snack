# Distributed Version Control System

What's the difference between a distributed and non-distributed version control
system?

## The Past

Version control systems before git based on a client/server model
* If the client couldn't establish a connection to the server no code snapshot could be created
* Before creating a snapshot the local state had to be updated to the latest state
  from the server
* Only the server had all meta information about the code and it's changes

```{mermaid}
flowchart LR
    A(Client A) <--> S[(Server)]
    B(Client B) <--> S
```

This had serious consequences:
* Not possible to create snapshots when being offline
* Error prone to conflicts
* If the server crashed and no backup of the server was available the whole
  history of snapshots was lost

## Git to Rule the World

To mitigate these consequences distributed version control systems like git were
created.

* Snapshots of the code can be created locally without a network connection
* A single git repository contains all meta information about the code changes
* There is no single *source of truth* for a repository anymore
* Every repository can be the *master*
* Information is distributed between different clones of the repository
    * Doesn't mean all repositories share all information
    * Repositories may hold only parts of the code changes

```{mermaid}
flowchart LR
    A[(Repo A)] --> C[(Repo C)]
    B[(Repo B)] --> C
    B <--> A
    C --> A
```
