# Duplicate File Finder

## Project Overview

This project is a command-line tool designed to identify duplicate files in a given directory and its subdirectories. The tool recursively scans the directory, lists all files, and will eventually be able to detect and handle duplicate files, freeing up storage space.

## Features Implemented

- **MD5 Hashing for Duplicate Detection**: The script calculates the MD5 hash of each file. Files with the same MD5 hash are reported as probable duplicates.
- **Full Byte-by-Byte Comparison for Duplicates**: After detecting probable duplicates using MD5 hashes, the script now performs a full byte-by-byte comparison of the files to confirm they are truly identical.
- **Minimum File Size Filter**: You can specify a minimum file size with the --minsize=<size> argument. Files smaller than the specified size will be ignored when checking for duplicates.
- **Command-Line Usage**: The script can be run from the command line and accepts a directory path as an argument and a minimum file size in **bytes** as optional argument.
- **Error Handling**: If an invalid directory is provided, the script returns an error message.

## Usage

To detect potential duplicate files based on size:

```bash
./duplicate_finder.py <directory>
```

For example, if you are already in the directory that has the python script:

```bash
./duplicate_finder.py .
```

To detect duplicates while ignoring files smaller than a certain size:

```bash
./duplicate_finder.py --minsize=1000 <directory>
```

This will only consider files that are 1,000 bytes or larger when detecting duplicates.

### Example Output

The output will display groups of files with the same size, indicating potential duplicates:

```bash
Duplicates: ./file1 ./subdir/duplicateoffile1
```

## Requirements

- Python3.x
