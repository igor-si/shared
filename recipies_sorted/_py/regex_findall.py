import re
# 
print "\n"*2,"Example: How to extract a floating number from a string [duplicate]"
test = "Current Level: 13.4 db."
print re.findall("\d+\.\d+", test)
print re.findall(r"[-+]?\d*\.\d+|\d+", test)

test2 = 'hello -34 42 +34.478m 88 cricket -44.3'
print re.findall(r'[\d\.\d]+', test2)

# ============ extract from hou version
re.compile(r"([_]\d{3}[_][t]\d{3})")
re.compile(r"([v]\d+\.*\d+)")
re.compile(r'([v]\d{4})')

re.compile(r'([vt]\d{3})') # INCLUDED EXTRACTIONS
re.compile(r'[vt]\d{3}') # NOT INCLUDED EXTRACTIONS

# Extracting decimal numbers from string 
# with Python regex

file_name = 'setups_rbd_v190_t003.hip'
pattern = re.compile(r'([vt]\d{3})')
print re.split(pattern,file_name)
		

file_name2 = 'item1'
pattern2 = re.compile(r'([\d}])') #[item]
print re.split(pattern2,file_name2)


print "\n"*2
file_list = ['item1','item_val1','item_valf','item_enable2']
pattern = re.compile(r'(item\d)') #[item]
for f in file_list:
	print re.split(pattern,f) , bool(re.search(pattern,f))

# ======= split digits
x = "test4"	
re.split(r'(\d+)',x)