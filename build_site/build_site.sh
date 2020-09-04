#!/bin/bash
set -e

##
## Builds out the website
##

echo $(ls)

## configure git
#git config --global user.name '${GITHUB_ACTOR}'
#git config --global user.email '${GITHUB_ACTOR}@users.noreply.github.com'
## clone in the group repos
#git clone https://github.com/McCoyGroup/Peeves.git
#git clone https://github.com/McCoyGroup/McUtils.git
#git clone https://github.com/McCoyGroup/Psience.git
#git clone https://github.com/McCoyGroup/RynLib.git
## run the docs script
#python3 References/docs.py
### push back to main
#git add -A && git commit -m "Built out site"
#git push -u origin master HEAD