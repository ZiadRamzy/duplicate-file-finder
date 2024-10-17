#!/usr/bin/env python3

import os
import sys
import hashlib
from typing import Dict, List

def calculate_md5(file_path:str) -> str:
    """Calculate the MD5 hash of a file."""
    hash_md5 = hashlib.md5()

    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
    except OSError:
        return ""
    
    return hash_md5.hexdigest()

def files_are_identical(file1: str, file2: str) -> bool:
    """Perform a byte-by-byte comparison of two files."""
    try:
        with open(file1, "rb") as f1, open(file2, "rb") as f2:
            while True:
                b1 = f1.read(4096)
                b2 = f2.read(4096)
                if b1 != b2:
                    return False
                if not b1:
                    break
    except OSError:
        return False
    
    return True


def find_duplicates_by_hash(directory: str) -> Dict[str, List[str]]:
    """Find potential duplicate files by size."""
    hash_to_files: Dict[str, List[str]] = {}


    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_md5(file_path)

            if not file_hash:
                continue
                        
            if file_hash not in hash_to_files:
                hash_to_files[file_hash] = []
            
            hash_to_files[file_hash].append(file_path)
    
    return hash_to_files
    

if __name__ == "__main__":
   
    if len(sys.argv) != 2:
        print("Usage: ./duplicate_finder.py <directory>")
        sys.exit(1)

    directory: str = sys.argv[1]

    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory")
        sys.exit(1)
    
    duplicates = find_duplicates_by_hash(directory)

    for file_hash, files in duplicates.items():
        if len(files) > 1:
            checked_duplicates = []
            for i in range(len(files)):
                for j in range(i + 1, len(files)):
                    if files_are_identical(files[i], files[j]):
                        checked_duplicates.append((files[i], files[j]))
            
            for f1, f2 in checked_duplicates:
                print(f"Duplicates: {f1}, {f2}")

                
