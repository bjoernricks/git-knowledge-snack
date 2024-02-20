#!/usr/bin/env python

import sys
from hashlib import sha1
from pathlib import Path

file = Path(sys.argv[1])
data = file.read_bytes()
hash = sha1(f"blob {len(data)}\0{data.decode()}".encode()).hexdigest()
print(hash)
