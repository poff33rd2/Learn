Two file handlers:

__Open: reading, writing, and creating files__
Accepts two args: open(<filename> <filelocation>, <mode>)

<mode> - indicates which action is required ALSO specifies text or binary output
mode = 'r' - open and read text | 'rb' - open and read binary format | 'r+' - opens files for reading and writing | 'w' - open for writing | 'a' - opens the file for editing or appending data

__binary format__ is for computting operations while __text__ is for user-facing operations with the computer.

__Close: used to close open file location - No arguments__
Close()

__with open: closes file after action is completed__
- no need for close()

with open('example.txt', 'r') as file:
    data = file.read()
    //closes when the code found here is finished
    //more efficient than close() unless its necessary


__reading files__ - get the content found in a file
__read()__ - Returns the entire content of the files as a string
__read(n)__ - returns are int of chars

with open('<filename>', 'r' ) as file:
    print(file.read())
    print(file.read(40)) #use a int to specify how many characters will be returned/read form the file

__readline()__ - returns the first line as a string
__readline(n)__ - returns are int of chars
file content:
This is the first line.
This is the second line.

with open('<filename>', 'r') as file:
    print(file.readline()) #output 1
    print(filen.readline(10)) #output 2

output: this is the first line.
output 2: this is the

__readlines()__ - reads the content of a file and returns it in an ordered list, allows lines to be selected.
__readlines(n)__ - picks out the specified number of lines. you can not select the line number only can iterate

file content:
This is the first line.
This is the second line.
This is the third line.
This is the fourth line.

with open('<filename>', 'r') as file:
Lines = file.readline()
print(len(lines))

for line in lines:
print line

output:
4 
This is the first line.
This is the second line.
This is the third line.
This is the fourth line.


__absolute path__ - used to locate files and directories
- contains forward slashes or drive labels 
- specifies where the file goes explicitly
/user/local/etc/somefile.txt 
C:\users\system\somefiles.txt

__relative paths__ - used to create a file where it
- contains no root directory call - posting file to the current path the operation is being ran at or default location
 





with open('filename.txt', 'r') as source:
even_lines = []

for line in enumerate source:
    if line % 2 == 0:
    even_lines.append()

    print even_lines
