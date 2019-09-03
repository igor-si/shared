

# URL https://stackoverflow.com/questions/19720711/git-warning-push-default-is-unset-its-implicit-value-is-changing
# GIT Warning 
# As you discovered, the way to get rid of the message 
# is to set push.default. To get the new behavior, use:

git config --global push.default simple


# To get Git's default behavior but without the warning message, use:
git config --global push.default matching

# add file
git add "test.py" 

# add everythin in the directory
git add .
git add -A


# to set upstream to master
git push --set-upstream origin master