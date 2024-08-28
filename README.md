# Directory Modifier

Python script called backup.py that takes a source directory and a destination directory as command-line arguments.

●       The script copy all files from the source directory to the destination directory.

●       Before copying, it checks if the destination directory already contains a file with the same name. If so, it appends a timestamp to the file name to ensure uniqueness.

●       Handle errors gracefully, such as when the source directory or destination directory does not exist.

Sample Command:

python backup.py /path/to/source /path/to/destination
