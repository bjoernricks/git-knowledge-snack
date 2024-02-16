# Git Blob

A git blob is the simplest object. It just contains binary data and doesn't link
any other objects.

It's format is

```{code-block}
---
caption: Internal format of a git blob
---

blob {size} {binary data}
```

Git calculates the hashsum as

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

Sources:

* [https://git-scm.com/book/en/v2/Git-Internals-Git-Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)
* [https://stackoverflow.com/questions/35430584/how-is-the-git-hash-calculated](https://stackoverflow.com/questions/35430584/how-is-the-git-hash-calculated)
