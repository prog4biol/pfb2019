# See link for full reference:
#
# http://bash-hackers.org/wiki/doku.php/scripting/terminalcodes
#
# \033 indicates a control character is to follow
#
# For full list, "man bash" and search to 2nd "PROMPTING" or see:
# http://tldp.org/HOWTO/Bash-Prompt-HOWTO/bash-prompt-escape-sequences.html
#
# \u : username
# \h : host to first "."
# \w : current full working directory
# \W : last part of path

# ALL control sequences (i.e. non-printing characters)
# MUST start with a \[ and end with a \]. This tells
# the shell that these are control characters.
# One set of escaped brackets can be used for several
# in a row, but can be done for each alone as defined
# below. If this is not done the line wrap will not
# function properly (since the shell doesn't know how
# long the prompt is).

COL_BLACK=$'\[\033[30m\]'
COL_RED=$'\[\033[31m\]'
COL_GREEN=$'\[\033[32m\]'
COL_YELLOW_ORANGE=$'\[\033[33m\]'
COL_BLUE=$'\[\033[34m\]'
COL_MAGENTA=$'\[\033[35m\]'
COL_CYAN=$'\[\033[36m\]'
COL_LIGHT_GREY=$'\[\033[37m\]'
COL_NORM=$'\[\033[39m\]'

PMPT_BOLD=$'\[\033[1m\]'
PMPT_NORM=$'\[\033[0m\]'
PMPT_UNDERLINE=$'\[\033[4m\]'
PMPT_BLINK=$'\[\033[5m\]'
PMPT_INVERSE=$'\[\033[7m\]'

# See: http://networking.ringofsaturn.com/Unix/Bash-prompts.php
# for a longer list of colours.

# actual command that sets prompt

PS1="${PMPT_BOLD}${COL_CYAN}\h${COL_NORM} [\w] %${PMPT_NORM} "
