# Unix Review 1 • 2017.10.16

Demitri Muna • <muna@cshl.edu> • <http://github.com/demitri>

## Customizing Your Bash Prompt

The bash prompt can be customized by setting the `PS1` environment variable. For example,

```
export PS1="\h % "
```

sets the prompt to be the computer’s host name followed byt a '%' sign, followed by a space. It can be anything you want, e.g.

```
export PS1="--> "
```

Special codes (like `\h`) perform substitutions. The most common ones are:

| Prompt code | Function |
| ----------- | -------- |
| \u          | username |
| \h          | host to first "." |
| \w          | current full working directory |
| \W          | last part of path |

This is a link that provides the full list: <http://tldp.org/HOWTO/Bash-Prompt-HOWTO/bash-prompt-escape-sequences.html>

When you are happy with the prompt, place the line in your `~/.profile` file (on a Mac) or your `~/.bashrc` file on Linux.

I have included the `prompts.sh` file that I use to customize my prompt. You can copy this to your computer and `source` it instead of copying the whole thing into your `.profile` or `.bashrc`.

[Mac] Note that you can define the color that the "bold" style is in from the Terminal preferences window.

And if you really want to go crazy: <http://osxdaily.com/2013/04/08/add-emoji-command-line-bash-prompt/>

## Aliases

An alias is a means of customizing unix commands. If you regularly type:

```
% ls -l
```

you might create an alias to do the same thing:

```
% alias ll="ls -l"
```

Some useful aliases:

```
alias ll='ls -l'
alias lh='ls -h'
alias lc='wc -l'
alias df='df -h'
```

You can put your alias definitions in your `~/.profile` / `~/.bashrc` files, but it’s easiest to keep all of them in a dedicated file and source it from the startup file, e.g.

```
source .my_aliases.sh
```

(The `.sh` extension is useful to indicate a bash script since the way to define an alias can vary from shell to shell.)

## Bash startup scripts

This is one way to organize your bash startup scripts.

1. Create a folder in your home directory:

    ```
    mkdir ~/.bash_scripts
    ```

2. Create a new file for each type of startup script, e.g.:

    ```
    cd ~/.bash_scripts
    touch aliases.sh
    touch autocomplete.sh
    touch colors.sh
    touch environment.sh
    touch paths.sh
    touch prompt.sh
    ```
3. Add these lines to your your [Mac] `~/.profile` [Linux] `~/.bashrc` file:

    ```
    source ~/.bash_scripts/aliases.sh
    source ~/.bash_scripts/autocomplete.sh
    source ~/.bash_scripts/colors.sh
    source ~/.bash_scripts/environment.sh
    source ~/.bash_scripts/paths.sh
    source ~/.bash_scripts/prompt.sh
    ```

This is overkill when you only have a line or two (or none) for each file, but as you become more experienced with the command line, the files will grow. They are also easier to copy from one server to another without containing anything platform-specific.

## Odds & Ends

 * [Mac] Recommended text editor: BBEdit <http://barebones.com>
 * [Mac] Drag a folder icon (or a file) from your desktop to a terminal window to copy the full path to the item.
 