# The `.git` Directory - References

Git stores all information in a single `.git` directory at the root directory
of your local repository. If this directory gets deleted, all git information is
lost and it's no longer a git repository.

So lets take a look at how references are stored on disk.

```sh
$ ls .git/
branches  COMMIT_EDITMSG  config  description  FETCH_HEAD  HEAD  hooks  index  info  logs  objects  refs

# HEAD ref
$ cat .git/HEAD
ref: refs/heads/main

# branch ref
$ cat .git/refs/heads/main
6227630dd590a9c3c6014eed15a18a639448f86d

# remote ref
$ cat .git/refs/remotes/upstream/main
6227630dd590a9c3c6014eed15a18a639448f86d
```

Example usage of references:

```
git log --oneline HEAD
git log --oneline refs/heads/main
git log --oneline main
git log --oneline refs/remotes/upstream/main
git log --oneline upstream/main
```
