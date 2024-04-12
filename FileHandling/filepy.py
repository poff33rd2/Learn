#files permenantly stores data for future use and record keeping.
import random
#create new file if the file name doesn't exist
#overrides previous content on file
# with open('newfile.txt', 'w') as file:
#     file.writelines(('This is a new file', '\nAnother line added here'))

#if newfile.txt exists, the code then appends evertime the code is run
# with open('newfile.txt', 'a') as file:
#     file.writelines(('\n', '\nThis is a new file', '\nAnother line added here'))

#use try: except: for known errors like wrong or missing directory, missspelling, and more
# try:
#     with open('errorfile.txt', 'r') as file:
#         file.writelines('This file should not exist and write')
# except FileNotFoundError as e:
#     print('error:', e)

#print multiple lines from 
# with open('loremipme.txt', 'r') as file:
#     data = file.readlines()

#     for x in file:
#         print(x)

with open('petnames.txt', 'r') as file:
    f = file.read()
    # print(f)
    f_list = f.split('\n')
    print(random.choice(f_list))