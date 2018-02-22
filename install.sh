echo appending bashrc
echo 'export BASH_TOOLS_HOME="'$(pwd)'"' >> ~/.bashrc
echo 'for f in $(find ${BASH_TOOLS_HOME} -maxdepth 1 -iname '"'"'bash*'"'"' -type f ); do
        . $f;
done' >> ~/.bashrc
source ~/.bashrc
echo

make

echo '*.gif diff=image
*.jpg diff=image
*.png diff=image
' >> ~/.gitattributes
git config --global core.attributesfile '~/.gitattributes'
git config --global diff.image.command '${BASH_TOOLS_HOME}/git-imgdiff'

