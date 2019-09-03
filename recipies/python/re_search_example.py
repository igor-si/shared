import re
m = re.search('(?<=abc)def', 'abcdef')
print m
m.group(0)
print m

