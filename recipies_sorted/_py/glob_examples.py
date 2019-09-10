import glob


# glob.glob(pathname)
# Return a possibly-empty list of path names that match pathname,
# which must be a string containing a path specification. 
# pathname can be either absolute (like /usr/src/Python-1.5/Makefile) 
# or relative (like ../../Tools/*/*.gif), and can contain shell-style
# wildcards. Broken symlinks are included in the results (as in the shell).

# glob.iglob(pathname)
# Return an iterator which yields the same values as glob()
# without actually storing them all simultaneously.


path = './1.gif'
glob.glob('./[0-9].*')
# ['./1.gif', './2.txt']

glob.glob('*.gif')
# ['1.gif', 'card.gif']

glob.glob('?.gif')
# ['1.gif']


# If the directory contains files starting with . 
# they wont be matched by default. For example, consider a directory 
# containing card.gif and .card.gif:
glob.glob('*.gif')
# ['card.gif']
glob.glob('.c*')
# ['.card.gif']

# Glob with list
[f for f_ in [glob.glob(e) for e in ('*.jpg', '*.mp4')] for f in f_]