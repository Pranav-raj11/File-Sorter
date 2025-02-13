# opening and closing a file method 1:
f = open('random_file.txt')

# print(f.mode)
f.close()

# opening and closing a file method 1:
with open('random_file.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)
    # for line in f:
    #     print(line, end='')

# # reading a file
# with open('random_file.txt', 'r') as f:
#     data = f.read()

# # writing data to a file
# with open('random_file.txt', 'w') as f:
#     data= 'adding text'
#     f.write(data)