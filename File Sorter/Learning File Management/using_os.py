# using os

# import os
# listing items in directory
# entries = os.listdir('dir/')
# print(entries)

# with os.scandir('dir/') as entries:
#     for entry in entries:
#         print(entry.name)

# listing only FILES in directory using listdir/scandir

# basepath = 'dir/'
# for entry in os.listdir(basepath):
#     if os.path.isfile(os.path.join(basepath, entry)):
#         print(entry)

# with os.scandir(basepath) as entries:
#     for entry in entries:
#         if entry.is_file():
#             print(entry.name)