#!/usr/bin/env python3

import os
import sys
from typing import Dict, List

def find_potential_duplicates(directory: str) -> Dict[int, List[str]]:
    """Find potential duplicate files by size."""
    size_to_files: Dict[int, List[str]] = {}


    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
            except OSError:
                continue
            
            if file_size not in size_to_files:
                size_to_files[file_size] = []
            
            size_to_files[file_size].append(file_path)
    
    return size_to_files
    

if __name__ == "__main__":
   
    if len(sys.argv) != 2:
        print("Usage: ./duplicate_finder.py <directory>")
        sys.exit(1)

    directory: str = sys.argv[1]

    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory")
        sys.exit(1)
    
    potential_duplicates = find_potential_duplicates(directory)

    for file_size, files in potential_duplicates.items():
        if len(files) > 1:
            print(f"Potential duplicates (size: {file_size} bytes): {' '.join(files)}")
