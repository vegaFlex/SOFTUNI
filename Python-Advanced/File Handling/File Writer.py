import os
#
# try:
#     with open('my_first_file.txt', 'w',) as file:
#         file.writelines('I just created my first file!')
# except FileNotFoundError:
#     print('File not found')

with open('my_first_file.txt', 'a') as file:
    file.writelines('I just created my first file!')

with open('my_first_file.txt', 'a') as file:
    file.writelines('second line')