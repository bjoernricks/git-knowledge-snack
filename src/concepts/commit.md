# Git Objects

## What's a Git Commit?

A git commit is a snapshot of the change information, hierarchy (**Git tree**),
including the contents of the files (**Git blob**) in a Git repository.

Every object (Git commit, Git tree, Git blob) is identified by it's hashsum.
The hashsum is calculated with SHA1 and includes the hashsums of all linked
objects.

## Git Blob

A git blob just contains binary data and doesn't link any other objects. Git
calculates the hashsum as

```{code-block} python
---
caption: Calculation of the git hash for a file in Python
---

import sys
from hashlib import sha1
from pathlib import Path

file = Path(sys.argv[1])
data = file.read_bytes()
hashsum = sha1(f"blob {len(data)}\0{data.decode()}".encode()).hexdigest()
print(hashsum)
```
## Git Tree

A git tree contains hashes to other tree and blobs. It's hashsum is calculated
from

```{code-block} python
---
caption: Incomplete Python pseudocode for calculating the git tree hash
---

tree_data = f"tree {len(tree.content)} \0\n"
linked_objects = [f"{obj.mode} {obj.file_or_folder_name}\0{obj.binary_sha1}" for obj in tree.objects]
data = tree_data + "\n".join(linked_objects) + "\n"
hashsum = sha1(data.encode()).hexdigest()
```

## Git Commit

A git commit contains the hashsum of the tree, parent commit and the commit
information. The hashsum is calculated as follows

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
* [https://stackoverflow.com/questions/14790681/what-is-the-internal-format-of-a-git-tree-object](https://stackoverflow.com/questions/14790681/what-is-the-internal-format-of-a-git-tree-object)
* [https://stackoverflow.com/questions/35430584/how-is-the-git-hash-calculated](https://stackoverflow.com/questions/35430584/how-is-the-git-hash-calculated)
