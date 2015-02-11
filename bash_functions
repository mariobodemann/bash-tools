# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
alias l=ls
alias la='ls -a'
alias ll='l -laH'
alias lg='l | grep' 
alias llg='ll | grep'

function colorize() {
 	tput setab $1; 
 	tput setaf $2; 
	echo -ne "$3"; 
	tput sgr0
}

function rgb126() { # reads one to six, means map from 0-1 to 0-6
	printf %4.3f $(echo 'scale=3; a = '$1' * 6; if ( a > 5 ) 5 else a' | bc | cut -d'.' -f1)
}

function rgbTo256() {
	echo 'scale=3; 16 + '$r' * 36 + '$g' * 6 + '$b | bc | cut -d'.' -f1
}

function rgb() {
	r=$(rgb126 $1);
	g=$(rgb126 $2);
	b=$(rgb126 $3);
	
	text=$4;

	color=$(rgbTo256 $r $g $b)
	tput setab $color; echo -en "$text"; tput sgr0;
}

export PS1="[\u@\h \W]\$ "


