# The Past

Version control systems predating git are based on a client/server model. Clients
are publishing changes on a central server and also downloading them from this
central server.

* If the client can't establish a connection to the server no code snapshot
  can be created
* Before creating a snapshot the local state has to be updated to include the
  latest changes from the server
* Only the server has all (meta) information about the code and it's changes

```{mermaid}
flowchart LR
    A(Client A) <--> S[(Server)]
    B(Client B) <--> S
```

This architecture has serious consequences:
* Not possible to create snapshots when being offline
* Developers tend to publish their changes at the end of the work day
* Incomplete or even broken features are published and downloaded
* Code changes in single snapshots are rather big
* Big snapshots are error prone to conflicts
* If the server crashes and no backup of the server is available the whole
  history of snapshots is lost
