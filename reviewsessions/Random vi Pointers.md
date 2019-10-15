# Random Vim Pointers

Demitri Muna • muna@cshl.edu • <http://github.com/demitri>

The best way to learn vim/vi is to pick up the basic commands (open/save/close files, basic editing, search, navigation), and then learn new commands. There are too many to sit down and learn them all at once. The best single resource is the [Vim Tips Wiki](http://vim.wikia.com/wiki/Vim_Tips_Wiki).

### Cheat Sheets

Below are a few cheat sheets that appear to be useful:

[vi Cheat Sheet](http://www.lagmonster.org/docs/vi.html)  
[vi Advanced Cheat Sheet](http://www.lagmonster.org/docs/vi.html)  

The easiest way to learn how to perform a specific task is to use Google - there are approximately an infinite number of single-task tutorials on StackOverflow and elsewhere for vi.

### Demitri’s `.vimrc` file

You can create a vi "resource file" in your home directory to customize the behavior of vi. It must be called `.vimrc`. The file won't be on your computer by default - you can just create it. You can use a text editor to do this. Maybe vi?

```
set number
set paste

set autoindent
set ignorecase
set showmode
set sm
set tabstop=4
syntax on
color dracula
" color aiseered
" Note - this is a comment in a .vimrc file (note no closing quote)
```

| .vimrc command | what it does |
| -------------- | ------------ |
| `set number` | display line numbers |
| `set paste` | turns off auto-indent when pasting code |
| `set autoindent` | when writing code, keep indentation after hitting return |
| `set ignorecase` | searches are case insensitive |
| `set showmode` | display the active mode on the bottom left of the screen |
| `set sm` | visually indicate matching braces (sm = 'show matching') |
| `set tabstop=4` | indent tab characters by 4 spaces |
| `syntax on` | turn on syntax highlighting |
| `color aiseered` | name of color scheme (see below) |

Other Links:

 * [A Good vimrc](https://dougblack.io/words/a-good-vimrc.html) - An excellent, detailed walkthrough of `.vimrc` options.
 * [The Ultimate Vim Configuration](https://github.com/amix/vimrc) - self-described - down the rabbit hole
 * [Open vimrc File](http://vim.wikia.com/wiki/Open_vimrc_file)

### Color Schemes

Color schemes must be downloaded and placed in the directory `~/.vim/colors`. For example, the `aiseered` color scheme referenced above can be downloaded [here](http://www.vim.org/scripts/script.php?script_id=750). The file is `aiseered.vim` in that directory.

 * <http://vimcolors.com> • This is a web site where you can browse color schemes to download the one(s) you like.

 * [How to set and use a color scheme](https://alvinalexander.com/linux/vi-vim-editor-color-scheme-colorscheme)
 
 * [The Dracula Theme](https://draculatheme.com/vim/) • Becuase why not.