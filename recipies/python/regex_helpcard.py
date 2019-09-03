
# METHODS
# Determine if the RE matches at the beginning of the string.
match()	

# Scan through a string, looking for any location where 
# this RE matches.
search()

 # Find all substrings where the RE matches, and returns 
 # them as a list.
findall()

# Find all substrings where the RE matches, 
# and returns them as an iterator.
finditer()







# Matches any decimal digit; this is equivalent to the class [0-9].
'\d'

# Matches any non-digit character; 
# this is equivalent to the class [^0-9].
'\D'

# Matches any whitespace character; this is equivalent 
# to the class [ \t\n\r\f\v].
'\s'

# Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
'\S'

# Matches any alphanumeric character; this is equivalent 
# to the class [a-zA-Z0-9_].
'\w'

# Matches any non-alphanumeric character; this is equivalent 
# to the class [^a-zA-Z0-9_].
'\W'