# Syntax Highlighting in nano


Follow the instructions here:
[https://github.com/scopatz/nanorc](https://github.com/scopatz/nanorc)




__Another Way__

The following recipe will show you how to install the `nano` text editor on your computer and enable color syntax highlighting.

### Linux

If you are on Linux, the solution is much easier. Use the native package manager to install the current version of `nano`. For example, on Ubuntu/Debian the command would be:

```
sudo apt-get install nano
```

For CentOS/Red Hat:

```
sudo yum install nano
```

Skip to the `Enabling Syntax Highlighting` section below.

### macOS

The default version of `nano` installed on macOS does not support syntax highlighting, so we will need to install an updated version on our own. This will involve downloading the source code, compiling it, and installing it. Note that these commands are very typical for installing most Unix programs.

By default, macOS does not include a C compiler. To install it, you will need to download a program called Xcode from the App Store (which is free). You will not need to use this program; just downloading and launching it once will isntall the compilers you need (and many other programs, e.g. `git`).

##### Get the source code.

This is the [home page](https://www.nano-editor.org/download.php) for `nano`. Get the URL for the latest version and download it to your computer, e.g.

```
wget https://www.nano-editor.org/dist/v2.8/nano-2.8.7.tar.xz
```

or

```
curl -O https://www.nano-editor.org/dist/v2.8/nano-2.8.7.tar.xz
```

##### Unpack the source.

The source code is compressed and needs to be unpacked with this command (use the name of the file you downloaded if different):

```
tar -xzf nano-2.8.7.tar.xz
```

##### Configure the program for your computer.

The source code can be used on many different kinds of unix-like computers, but each have their own idiosyncrasies. You need to run a program to configure the files for your specific computer. One configuration we will customise is where to install the program. Here, we will place it in `/usr/local/nano-2.8.7`.

```
cd nano-2.8.7
./configure --prefix=/usr/local/nano-2.8.7
```

A long list of messages will stream by in your terminal. If all goes well, you won’t see any errors.

##### Compile the program.

To compile the program, execute the `make` command:

```
make
```

This will compile the code using one CPU. If you want to justify all that money you spent on your fancy modern multi-core processor, you can use this command to make things Go Faster:

```
make -j4
```

##### Install nano.

Assuming there were no errors, you can now install `nano` on your computer:

```
sudo make install
```

We need to use the `sudo` command since we are installing the program in a system (i.e. non-user) location.

Next, we will create a soft link (think: alias) to the folder we just created:

```
cd /usr/local
sudo ln -s nano-2.8.7 nano
```

There are a few advantages to this method. First, the whole program we just installed is in a single location: `/usr/local/nano-2.8.7`. If we ever want to delete it, we can just delete that one directory. We can also (if we wanted) install more than one version, e.g.

```
/usr/local/nano-2.8.7
/usr/local/nano-2.8.9
```

The `ln -s` command above points `/usr/local/nano` to `/usr/local/nano-2.8.7`:

```
[/usr/local] % ll -d nano*
lrwxr-xr-x  1 root  wheel   10 Oct 16 16:23 nano@ -> nano-2.8.7
drwxr-xr-x  4 root  wheel  136 Oct 16 15:43 nano-2.8.7/
drwxr-xr-x  4 root  wheel  136 Oct 16 15:55 nano-2.8.9/
```

We can change which program we want to use just by changing the soft link.


##### Update your `$PATH`.

When you type `nano` now, you will still be using the system-provided version, which is not what we want. We need to tell your shell to look in this new location to use the `nano` we just installed. If you’re using bash, open the file `.profile` in your home directory using your favorite text editor, e.g.

```
vi ~/.profile
```

and add this line to the bottom:

```
export PATH=/usr/local/nano/bin:${PATH}
```

Open a new shell, type `nano`, and you should be using the new version.

### Enabling Syntax Highlighting

Many programs allow you to customize them by creating a “resource” file in your home directory. These typically are “dot files” (i.e. they begin with a `.` and are invisible with `ls`), have the name of the program, and end with `rc` (“resource”). `nano`'s resource file is: `.nanorc`. (While this is a standard naming scheme, you need to check each program’s documentation for the exact name of the file.) It’s not a problem if that file is not present; it’s an optional way to customize a program.

To enable syntax highlighting, we need to create the `~/.nanorc` file and place a command for each language we want `nano` to add syntax highliting to. The form of the command is:

```
include /usr/local/nano-2.8.7/share/nano/python.nanorc
```

This will add syntax highlighting for Python. Note that this is the path to a file in a specific location on your computer - if that file is not there, it (of course) won’t work. The path above is specific to what we just installed. (On the Mac – if you're on Linux, you will need to find the location of these files on your own system, which is probably `/usr/share/nano/`). This will work, but if we ever update `nano`, we would need to update our `~/.nanorc`, which is tedious. Instead, we’ll use the soft link (alias) we made above:

```
include /usr/local/nano/share/nano/python.nanorc
```

As long as `/usr/local/nano` points to the version we want to use, the `~/.nanorc` will work and not need modification. Look in the directory above to see all of the available languages.

If you want to include all of the available languages, you can copy this into your `~/.nanorc` file:

```
include /usr/local/nano/share/nano/asm.nanorc
include /usr/local/nano/share/nano/autoconf.nanorc
include /usr/local/nano/share/nano/awk.nanorc
include /usr/local/nano/share/nano/c.nanorc
include /usr/local/nano/share/nano/changelog.nanorc
include /usr/local/nano/share/nano/cmake.nanorc
include /usr/local/nano/share/nano/css.nanorc
include /usr/local/nano/share/nano/debian.nanorc
include /usr/local/nano/share/nano/default.nanorc
include /usr/local/nano/share/nano/elisp.nanorc
include /usr/local/nano/share/nano/fortran.nanorc
include /usr/local/nano/share/nano/gentoo.nanorc
include /usr/local/nano/share/nano/go.nanorc
include /usr/local/nano/share/nano/groff.nanorc
include /usr/local/nano/share/nano/guile.nanorc
include /usr/local/nano/share/nano/html.nanorc
include /usr/local/nano/share/nano/java.nanorc
include /usr/local/nano/share/nano/javascript.nanorc
include /usr/local/nano/share/nano/json.nanorc
include /usr/local/nano/share/nano/lua.nanorc
include /usr/local/nano/share/nano/makefile.nanorc
include /usr/local/nano/share/nano/man.nanorc
include /usr/local/nano/share/nano/mgp.nanorc
include /usr/local/nano/share/nano/mutt.nanorc
include /usr/local/nano/share/nano/nanohelp.nanorc
include /usr/local/nano/share/nano/nanorc.nanorc
include /usr/local/nano/share/nano/nftables.nanorc
include /usr/local/nano/share/nano/objc.nanorc
include /usr/local/nano/share/nano/ocaml.nanorc
include /usr/local/nano/share/nano/patch.nanorc
include /usr/local/nano/share/nano/perl.nanorc
include /usr/local/nano/share/nano/php.nanorc
include /usr/local/nano/share/nano/po.nanorc
include /usr/local/nano/share/nano/postgresql.nanorc
include /usr/local/nano/share/nano/pov.nanorc
include /usr/local/nano/share/nano/python.nanorc
include /usr/local/nano/share/nano/ruby.nanorc
include /usr/local/nano/share/nano/rust.nanorc
include /usr/local/nano/share/nano/sh.nanorc
include /usr/local/nano/share/nano/spec.nanorc
include /usr/local/nano/share/nano/tcl.nanorc
include /usr/local/nano/share/nano/tex.nanorc
include /usr/local/nano/share/nano/texinfo.nanorc
include /usr/local/nano/share/nano/xml.nanorc
```

### Bonus Unix Trickery

Extra credit: Instead of copying the lines above into `~/.nanorc`, try this (note: everything from the `for` is all one line):

```
rm ~/.nanorc
for i in `ls *.nanorc`; do echo include /usr/local/nano/share/nano/$i >> ~/.nanorc; done
```

Homework: Figure out what the heck just happened there.

### TL;DR

Standard procedure to install Unix software:

```
wget <file-1.2.3.tar.gz>
tar -xzf <file-1.2.3.tar.gz>
cd <file.1.2.3>
./configure
make
make install
```

