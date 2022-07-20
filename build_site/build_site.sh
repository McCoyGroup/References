#!/bin/bash
set -e

##
## Builds out the website
##

# get into the parent folder?
cd /home
# configure git
git config --global user.name ${GITHUB_ACTOR}
git config --global user.email ${GITHUB_ACTOR}@users.noreply.github.com
# clone in the group repos
git clone https://github.com/McCoyGroup/Peeves.git
git clone https://github.com/McCoyGroup/McUtils.git
git clone https://github.com/McCoyGroup/Psience.git
git clone https://github.com/McCoyGroup/RynLib.git
## make sure we're build off of an up to date repo
cd References
git pull

# Zip and push exercises changes
cd McCoy\ Group\ Code\ Academy
zip -r Exercises.zip Exercises
cd ..
git add -A && git commit -m "updated exercises"
git push -u origin HEAD

## run the docs script
# cd /home
# PYTHONPATH=/home python3 References/docs.py
# ### push back to main
# cd References
# git add -A && git commit -m "Built out site"
# git push -u origin HEAD
