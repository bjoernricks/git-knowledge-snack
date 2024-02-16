# Git Tree

A git tree links to blobs and other trees. A blob in a tree represents a file
and a linked tree represents a directory with additional files and directories.

```{mermaid}
flowchart TD
    A[tree] -->|README.md| B(blob)
    A[tree] -->|LICENSE| C(blob)
    A[tree] -->|src| D[tree]
    D[tree] -->|conf.py| E(blob)
    D[tree] -->|index.md| F(blob)
```

It's format is

```{code-block}
---
caption: Internal format of a git tree
---

tree {size}
{file1 permissions} blob {file1 hashsum} {file1 name}
{tree2 permissions} tree {tree2 hashsum} {tree2 directory name}
{file2 permissions} blob {file2 hashsum} {file2 name}
...
```

It's hashsum is calculated from

```{code-block} python
---
caption: Incomplete Python pseudocode for calculating the git tree hash
---

tree_data = f"tree {len(tree.content)}\0\n"
linked_objects = [f"{obj.mode} {obj.file_or_folder_name}\0{obj.binary_sha1}" for obj in tree.objects]
data = tree_data + "\n".join(linked_objects) + "\n"
hashsum = sha1(data.encode()).hexdigest()
```

Sources:

* [https://git-scm.com/book/en/v2/Git-Internals-Git-Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)
* [https://stackoverflow.com/questions/14790681/what-is-the-internal-format-of-a-git-tree-object](https://stackoverflow.com/questions/14790681/what-is-the-internal-format-of-a-git-tree-object)
* [https://stackoverflow.com/questions/35430584/how-is-the-git-hash-calculated](https://stackoverflow.com/questions/35430584/how-is-the-git-hash-calculated)
