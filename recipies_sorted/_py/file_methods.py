close()	Closes the file
detach()	Returns the separated raw stream from the buffer
fileno()	Returns a number that represents the stream, from the operating system's perspective
flush()	Flushes the internal buffer
isatty()	Returns whether the file stream is interactive or not
read()	Returns the file content
readable()	Returns whether the file stream can be read or not
readline()	Returns one line from the file
readlines()	Returns a list of lines from the file
seek()	Change the file position
seekable()	Returns whether the file allows us to change the file position
tell()	Returns the current file position
truncate()	Resizes the file to a specified size
writeable()	Returns whether the file can be written to or not
write()	Writes the specified string to the file
writelines()	Writes a list of strings to the file



# https://www.geeksforgeeks.org/reading-writing-text-files-python/
# Access modes govern the type of operations possible in the opened file. 
# It refers to how the file will be used once its opened. 
# These modes also define the location of the File Handle in the file.
# File handle is like a cursor, which defines from where the data has 
# to be read or written in the file. There are 6 access modes in python.

Read Only (‘r’) 
# Open text file for reading. The handle is positioned at the beginning of the
# file. If the file does not exists, raises I/O error. This is also the default 
# mode in which file is opened.

Read and Write (‘r+’) 
# : Open the file for reading and writing. The handle is positioned at 
# the beginning of the file. Raises I/O error if the file does not exists.

Write Only (‘w’) 
# : Open the file for writing. For existing file, the data is truncated 
# and over-written. The handle is positioned at the beginning of the file.
# Creates the file if the file does not exists.


Write and Read (‘w+’)
# : Open the file for reading and writing. For existing file, 
# data is truncated and over-written. The handle is positioned 
# at the beginning of the file.

Append Only (‘a’) 
# : Open the file for writing. The file is created if it does not exist.
# The handle is positioned at the end of the file. The data being 
# written will be inserted at the end, after the existing data.

Append and Read (‘a+’)
# : Open the file for reading and writing. The file is created
# if it does not exist. The handle is positioned at the end of the file.
# The data being written will be inserted at the end, after the existing data.