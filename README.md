# Duplicate File Finder

## Project Overview

This project is a command-line tool designed to identify duplicate files in a given directory and its subdirectories. The tool recursively scans the directory, lists all files, and will eventually be able to detect and handle duplicate files, freeing up storage space.

## Features Implemented

- **MD5 Hashing for Duplicate Detection**: The script calculates the MD5 hash of each file. Files with the same MD5 hash are reported as probable duplicates.
- **Command-Line Usage**: The script can be run from the command line and accepts a directory path as an argument.
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

### Example Output

The output will display groups of files with the same size, indicating potential duplicates:

```bash
Probable duplicates (MD5 hash: e48f7c224cc0be1934024a15b9f55d52): ./file21 ./file1
```

## Requirements

- Python3.x
