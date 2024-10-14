# Duplicate File Finder

## Project Overview

This project is a command-line tool designed to identify duplicate files in a given directory and its subdirectories. The tool recursively scans the directory, lists all files, and will eventually be able to detect and handle duplicate files, freeing up storage space.

## Features Implemented

- **Recursive File Listing**: The script accepts a directory as input and lists all files within that directory, including files in subdirectories.
- **Command-Line Usage**: The script can be run from the command line and accepts a directory path as an argument.
- **Error Handling**: If an invalid directory is provided, the script returns an error message.

## Usage

To list all files in a directory recursively, run the following command:

```bash
./duplicate_finder.py <directory>
```

For example, if you are already in the directory that has the python script:

```bash
./duplicate_finder.py .
```

### Example Output

```bash
./file1
./file2
./subdir/file3
...
```

## Requirements

- Python3.x
