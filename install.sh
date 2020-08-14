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
git config --global alias.st status
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
git config --global user.name "Mario Bodemann"
git config --global user.email "mario.bodemann@gmail.com"


if command -v termux-open; then
	echo adding termux shortcuts

	cp -fr shortcuts $HOME/.shortcuts
fi
