#!/usr/bin/env python3

import os
import sys
from typing import Generator

def list_files(directory: str) -> Generator[str, None, None] :
    """Recursively list all files in the given directory."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(os.path.join(root, file))
    

if __name__ == "__main__":
   
    if len(sys.argv) != 2:
        print("Usage: ./duplicate_finder.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory")
        sys.exit(1)
    
    list_files(directory=directory)

