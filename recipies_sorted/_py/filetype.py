
# How to identify binary and text files using Python? [duplicate]
# If your script is running on *nix, you could use something like this:
import subprocess
import re

def is_text(fn):
    msg = subprocess.Popen(["file", fn], stdout=subprocess.PIPE).communicate()[0]
    return re.search('text', msg) != None


def is_binay_file(filepathname):
	textchars = bytearray([7,8,9,10,12,13,27]) + bytearray(range(0x20, 0x7f)) + bytearray(range(0x80, 0x100))
	is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))

	if is_binary_string(open(filepathname, 'rb').read(1024)):
		return True
	else:
		return False


		# def istextfile(fileobj, blocksize=512):
	 #   		PY3 = sys.version_info[0] == 3
		# 	int2byte = (lambda x: bytes((x,))) if PY3 else chr
		# 	_text_characters = (
		# 			b''.join(int2byte(i) for i in range(32, 127)) +
		# 			b'\n\r\t\f\b')   		
		# 	""" Uses heuristics to guess whether the given file is text or binary,
		#     by reading a single block of bytes from the file.
		#     If more than 30% of the chars in the block are non-text, or there
		#     are NUL ('\x00') bytes in the block, assume this is a binary file.
		# 	"""

		# 	block = fileobj.read(blocksize)
		# 	if b'\x00' in block:
		# 	# Files with null bytes are binary
		# 		return False
		# 	elif not block:
		# 	# An empty file is considered a valid text file
		# 		return True

		#     # Use translate's 'deletechars' argument to efficiently remove all
		#     # occurrences of _text_characters from the block
		# 	nontext = block.translate(None, _text_characters)
		# 	return float(len(nontext)) / len(block) <= 0.30
		# try:
		# 	istextfile(f)
		# except:
		# 	# print f
		# 	pass


		
	# from __future__ import division
	# import string 
	# def istext(filename):
	# 	s=open(filename).read(512)
	# 	text_characters = "".join(map(chr, range(32, 127)) + list("\n\r\t\b"))
	# 	_null_trans = string.maketrans("", "")
	# 	if not s:
	# 	    # Empty files are considered text
	# 	    return True
	# 	if "\0" in s:
	# 	    # Files with null bytes are likely binary
	# 	    return False
	# 	# Get the non-text characters (maps a character to itself then
	# 	# use the 'remove' option to get rid of the text characters.)
	# 	t = s.translate(_null_trans, text_characters)
	# 	# If more than 30% non-text characters, then
	# 	# this is considered a binary file
	# 	if float(len(t))/float(len(s)) > 0.30:
	# 	    return False
	# 	return True