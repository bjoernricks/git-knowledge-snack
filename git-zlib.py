#!/usr/bin/env python3
import sys
import zlib
from pathlib import Path


def main() -> None:
    file = Path(sys.argv[1])
    data = file.read_bytes()
    print(zlib.decompress(data).decode(errors="replace").replace("\0", "\n"))


if __name__ == "__main__":
    main()
