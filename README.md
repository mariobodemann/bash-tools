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

use the `install.sh` script for setting it up.
