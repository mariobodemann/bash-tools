# bash-tools

Tools for helping daily work

# color
Tools for converting an rgb (0..1) color into a console 256 color.

Example:
> rgb 1 .5 0 'Hello World'
Hello World

(Okay that will be colored, I'll maybe figure out how to do this in md ...)

## Usage
Include this in your .bashrc: 

> for f in $(find ${BASHTOOLS_HOME}/bash-tools/ -iname 'bash*' -type f); do 
> 	. $f; 
> done

(Warning: Will execute _all_ files in bash-tools starting with bash!

