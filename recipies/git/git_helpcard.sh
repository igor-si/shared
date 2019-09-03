
# how to copy git repository
git clone "https://github.com/igor-si/test.git"

git remote -v
git remote set-url origin https://github.com/igor-si/dev.git

# add any changes
git add "db_links.txt"


# add everythin in the directory
git add .
git add -A
git add *.hip *.hipnc *.hiplc *.cmd *.txt *.otl *.hda *.h *.cpp *.md *.obj *.inc *.hcs *.py *.json *.gal *.sh *.xml *.shelf *.pdf

# check status
git status

# commit changes
git commit -m "message"

# to push changes to the github
git push

#when we want to push ot to origin
git push origin master


git commit -m "initial commit"


# Tutorial
#URL https://www.youtube.com/watch?v=ol_UCWox9kc
#==================================
# create repo
# navigate to directory
git clone https://github.com/igor-si/dev.git #+
# new folder has been created
# we want to push it to the site
# navigate to the repo folder cd ./dev
git remote -v #+
git remote set-url origin https://github.com/igor-si/dev.git #+

# to check if it successfull
git remote -v #+ If "origin" in the beginning we are in business
git push origin master #-
git add -A #+
git status #+  Checking status
git commit -m 'test' #+ test commit
git push origin master #push to repo

# hot to add changes
git add -A
git commit -m 'test'
git push origin master


git remote set-url origin https://github.com/igor-si/scripts.git


git remote set-url origin https://github.com/igor-si/setups.git
#git remote set-url origin https://github.com/AnneMarieHarm/deliverable_one.git









…or create a new repository on the command line
echo "# third_party" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/igor-si/third_party.git
git push -u origin master


…or push an existing repository from the command line
git remote add origin https://github.com/igor-si/third_party.git
git push -u origin master