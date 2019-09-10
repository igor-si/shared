import re

# Multiple replace
def multiReplace():
	name = 'test_balalaika_user'
	replace_list=['test','user']
	for r in replace_list: name=name.replace(r,'')
	print name
multiReplace()


def matchString():
	file_name = 'IS_instanceRBDGeoPrep_123'
	pattern = r'(IS_instanceRBDGeoPrep*)'
	bool(re.match(pattern,file_name)) #or return object


	