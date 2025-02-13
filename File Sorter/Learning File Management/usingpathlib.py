from pathlib import Path
import shutil

entries = Path('dir/')
# Directory Listing
for entry in entries.iterdir():
    print(entry.name)

# Files in directory
for entry in entries.iterdir():
    if entry.is_file():
        print(entry.name)

# Subdirectories in directory
for entry in entries.iterdir():
    if entry.is_dir():
        print(entry.name)


# Making a directory
# p = Path('newdir/')
# p.mkdir()

# Making multiple directories
# p = Path('2024/12/11')
# p.mkdir(parents=True)


# Making flexible file listings
p = Path('.')
for name in p.glob('*.py'):
    print(name)


# Deleting files
# data_file = Path('dir/delte.txt')
# try:
#     data_file.unlink()
# except IsADirectoryError as e:
#     print(f'Error: {data_file} : {e.strerror}')

# Deleting empty directories
# data_dir = Path('dir/deldir')
# try:
#     Path('dir/deldir/txt.txt').unlink()
#     data_dir.rmdir()
# except OSError as e:
#     print(f'Error: {data_dir} : {e.strerror}')

# Deleting entire directory trees (needs shutil import)
# trash_dir = 'dir/dir2'
# try: 
#     shutil.rmtree(trash_dir)
# except OSError as e:
#     print(f'Error: {trash_dir} : {e.strerror}')

# Copying files
# src = 'dir/copy_of_copiedfile.txt'
# dst = 'newdir/copy_of_copy_of_copiedfile.txt'
# shutil.copy(src,dst)

# Copying directories
# shutil.copytree('newdir', 'dir/copy_of_newdir')

# Moving files and directories (also renames if you set it)
# shutil.move('newdir/copy_of_newdir', 'dir/newname')

# Renaming files (using pathlib.Path) 
# --- > This method can also move files if new path is set
# data_file = Path('dir/something.txt')
# data_file.rename('dir/somethingelse.txt')
data_file = Path('dir/collector.c')
data_file.rename('dir/collector.c')