# bash-tools

Tools for helping daily work

# color
Tools for converting an rgb (0..1) color into a console 256 color.

Example:
> rgb 1 .5 0
\e[38;5;214m

> echo -e "$(rgb 1 .5 0)hello world$(bgr)"
hello world

(Okay that will be colored in orange, I'll maybe figure out how to do this in md)

## Usage
* Include this in your .bashrc:

> export BASH_TOOLS_HOME='~/bin/bash'
> for f in $(find ${BASH_TOOLS_HOME} -maxdepth 1 -iname 'bash\*' -type f ); do
>         . $f;
> done

(Warning: Will execute _all_ files in bash-tools starting with 'bash'!)

* Draw a Rainbow:
> echo -e $(rainbow 'hello')

* Use some rainbows for output command

> for file in $(ls /usr/share/figlet/\*lf); do
>    f=$(basename $file | cut -d'.' -f1);
>    echo -e "$(rgb 0 0 0)$(figlet -f $f $f | sed 's/\\/V/g' | rainbow -bg -- @-;)";
> done;

Note how the \\ curently still needs escaping, an update is to be released soon.
