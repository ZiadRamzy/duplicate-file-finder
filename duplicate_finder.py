#!/usr/bin/env python3

import os
import sys
import hashlib
from typing import Dict, List, Optional

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


def find_duplicates_by_hash(directory: str, min_size: Optional[int] = None) -> Dict[str, List[str]]:
    """Find potential duplicate files by size."""
    hash_to_files: Dict[str, List[str]] = {}


    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                file_size = os.path.getsize(file_path)
                if min_size is not None and file_size < min_size:
                    continue
            except OSError:
                continue

            file_hash = calculate_md5(file_path)

            if not file_hash:
                continue
                        
            if file_hash not in hash_to_files:
                hash_to_files[file_hash] = []
            
            hash_to_files[file_hash].append(file_path)
    
    return hash_to_files

def promt_for_deletion(duplicates: List[str]):
    """Prompt the user to select which duplicate file to delete."""
    print("Which file should be deleted?")
    for idx, file in enumerate(duplicates, 1):
        print(f" {idx} {file}")

    try:
        choice = int(input("Enter the number of the file to delete, or any other value to keep all: "))
        if 1 <= choice <= len(duplicates):
            os.remove(duplicates[choice - 1])
            print(f"Deleted: {duplicates[choice - 1]}")
        else:
            print("No files deleted.")
    except ValueError:
        print("Invalid input, no files deleted.")
    
    

if __name__ == "__main__":
    
    min_size: Optional[int] = None
    directory: Optional[str] = None

    for arg in sys.argv[1:]:
        if arg.startswith("--minsize="):
            try:
                min_size = int(arg.split("=")[1])
            except ValueError:
                print("Invalid value for --minsize. It must be an Integer.")
        else:
            directory = arg

   
    if directory is None:
        print("Usage: ./dupplicate_finder.py [--minsize=<size>] <directory>")
        sys.exit(1)
        
    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory")
        sys.exit(1)
    
    duplicates = find_duplicates_by_hash(directory, min_size)

    for file_hash, files in duplicates.items():
        if len(files) > 1:
            checked_duplicates = []
            for i in range(len(files)):
                for j in range(i + 1, len(files)):
                    if files_are_identical(files[i], files[j]):
                        checked_duplicates.append((files[i], files[j]))
            
            for f1, f2 in checked_duplicates:
                print(f"Duplicates: {f1}, {f2}")
                promt_for_deletion([f1, f2])


