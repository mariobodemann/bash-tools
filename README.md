# bash-tools

Tools for helping daily work

# color
Tools for converting an rgb (0..1) color into a console 256 color.

Example:
> rgb 1 .5 0 'Hello World'
Hello World

(Okay that will be colored, I'll maybe figure out how to do this in md ...)

## Usage
* Include this in your .bashrc: 

> export BASH_TOOLS_HOME='~/bin/bash'
> for f in $(find ${BASH_TOOLS_HOME} -maxdepth 1 -iname 'bash*' -type f ); do 
>         . $f; 
> done
(Warning: Will execute _all_ files in bash-tools starting with bash!

* Draw a Rainbow:
> for j in $(seq 0 1 9); do for i in $(seq 0 3 359); do hsvText $i 1 0.$j '.'; done; echo; done


