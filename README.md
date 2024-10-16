# Duplicate File Finder

## Project Overview

This project is a command-line tool designed to identify duplicate files in a given directory and its subdirectories. The tool recursively scans the directory, lists all files, and will eventually be able to detect and handle duplicate files, freeing up storage space.

## Features Implemented

- **Potential Duplicate Detection**: The script compares file sizes to identify potential duplicates. If two or more files have the same size, they are reported as potential duplicates.
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
Potential duplicates (size: 100 bytes): ./file1 ./file21
Potential duplicates (size: 100 bytes): ./subdir/duplicateoffile1 ./file1
```

## Requirements

- Python3.x
