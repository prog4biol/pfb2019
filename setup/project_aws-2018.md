# Creating Amazon EC2 servers for project groups


## Launching an EC2 instance with an Ubuntu AMI 
1. Log into the Amazon *EC2 Management Console*.
2. Click on the _EC2_ link under the *AWS services* pane to view the *EC2 Dashboard*.
3. Click on the blue `Launch Instance` button.
4. From the *Amazon Machine Image* (AMI) table, select the latest version of Ubuntu Server available (18.04 LTS as of this writing).
5. From the *Choose an Instance Type* table, choose "m4.4xlarge" and click the `Next: Configure Instance Details` button in the bottom right corner of the browser page.
6. Click `Next: Add Storage` button in the bottom right corner of the browser page to accept Instance Details defaults
7. Under the "Size (GiB)" column of the instance table, type `500` to add 500 GiB of Disk space to the instance. Click the `Next: Add Tags` button to continue.
8. Click `Next: Configure Security Group` button to skip adding tags
9. Under the *Security Group table*, make sure an Connection type **SSH** is added with Protocol **TCP** , Port Rage of **22**, and Source as **0.0.0.0/0** (*i.e.* anyware). We will create two additional rules, one for Apache web servers and another for Jupyter notebooks:
   1. **Web server**: Click the `Add Rule` button to add an **HTTP** security rule, and accept all defaults. Finally, click the `Review and Launch` button to review the instance configuration and launch the instance.
   2. **Jupyter notebooks**: Click the `Add Rule` button and select **Custom TCP Rule** from the Connection type drop-down. Input **TCP** as the Protocol type, **8888** as the Port Range, and **0.0.0.0/0** in Source.
10. If the instance configuration is correct, press the blue `Launch` button to launch the instance. If you receive a dialogue box requesting a key pair, select "Create new key pair" from the first drop-down menu if this is the first of launch instance, otherwise choose "Choose an existing key pair" and specify the key pair name from the second drop-down menu. Finally, confirm that you have access to the selected private key file and click the `Launch Instances` button.
11. The instance will initialize; make sure it passess all initialization checks before proceeding.


## Assigning project server domain names
1. In the *AWS EC2 Dashboad*, click _Instances_ from the side bar and copy the elastic IP for the running instance to your clipboard.

2. Open a new *Console* window, select the _Route 53_ link under the *Networking & Content Delivery* Section of the *Services* dropdown menu (upper left corner of the browser page). Add the elastic IP address to a new "Record Set" associated with programmingforbiology.org:
  1. Click the _Hosted zones_ link.
  2. Click the _programmingforbiology.org_ link.
  3. Click the blue `Create Record Set` button.
  4. In the right-hand pane, give the new record set the name of the project group.
  5. Paste the elastic IP into the "Value:" field.
  6. Accept all other defaults and click the blue `Save Record Set` button to add the domain to the record set.


## Loading software onto the instance

Log into the Ubuntu EC2 instance via the command-line:
```bash
ssh -i /path/to/admin.pem ubuntu@ec2-*.compute.amazonaws.com
```



### Updating the apt-cache package database

```bash
sudo apt-get update
```



### Installing GNU emacs without X-windows plugin:

```bash
sudo apt-get install emacs25-nox
```



### Installing gcc/g++ and build libs:

```bash
sudo apt-get install build-essential 
sudo apt-get install gfortran
```



### Installing GNU make and Cmake:

```bash
sudo apt-get install make
sudo apt-get install make-doc
sudo apt-get install cmake
sudo apt-get install cmake-doc
```



### Installing Anaconda Python for Linux machines:

```
curl -OL https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh
sudo bash Anaconda3-5.3.0-Linux-x86_64.sh
```
- Do you accept the license terms? **YES**
- Set installation PREFIX: **`/usr/local/anaconda`**
- Do you wish the installer to initialize Anaconda3: **YES**
- Do you wish to install Microsoft VSCode? **NO**

Append the following code to the global bash login resource file  `/etc/bash.bashrc`
```bash
if [ -d /usr/local/anaconda ]; then
   \export PATH="/usr/local/anaconda/bin:$PATH";
   \export INCLUDE_PATH="/usr/local/anaconda/include:$INCLUDE_PATH";
   \export LIBRARY_PATH="/usr/local/anaconda/lib:$LIBRARY_PATH";
   \export LD_LIBRARY_PATH="/usr/local/anaconda/lib:$LD_LIBRARY_PATH";
   \export PKG_CONFIG_PATH="/usr/local/anaconda/lib/pkgconfig:$PKG_CONFIG_PATH";
   \export MANPATH="/usr/local/anaconda/man:$MANPATH";
fi
```



### Installing Nano with syntax highlighting:

Install *libcurses* prerequisites and install `nano` from source:
```bash
# install prereqs:
sudo apt-get install libncurses5-dev libncursesw5-dev

# download nano package
wget https://www.nano-editor.org/dist/v3/nano-3.1.tar.gz

# build and install:
tar -xzvf nano-3.1.tar.gz \
    && cd nano-3.1 \
    && ./configure --prefix=/usr/local \
    && sudo make install

# Add syntax highlighting `include` lines in nano resource (.nanorc) file for new users
for f in /usr/local/share/nano/*.nanorc; do echo "include $f"; done >nano.nanorc
sudo cat nano.nanorc >>/etc/skel/.nanorc
```



In the presence of a `.bash_profile`, the `.bashrc` file does not appear to be `source`'d and we lose Bash syntax highlighting. Create `/etc/skel/.bash_profile` with the following lines to load `.bashrc` settings:

```bash
# in order to preserve terminal color settings in the presence                                                                                                
# of a .bash_profile, we must source the .bashrc file explicitly                                                                                              
if [ -e "$HOME/.bashrc" ]; then
    . "$HOME/.bashrc";
fi

## ---- Add User-specific settings below ----

# END
```

### Installing Java JDK:

The version of JDK installed will change over time. As of this writing, JDK v10 was installed by default.

```bash
sudo apt-get install default-jdk
```

### Installing X11:

First, we must install the X11 server:

```bash
sudo apt-get install xorg xorg-dev openbox
```

Then, configure `ssh` to allow X11 forwarding: In `/etc/ssh/ssh_config`, uncomment the following lines and set to `yes`:

```bash
sudo emacs /etc/ssh/ssh_config
```

```ini
    ForwardX11 yes
    ForwardX11Trusted yes
```

### Installing R/Rscript:

The version of R installed will change over time. As of this writing, R/Rscript v3.4 was installed by default.

```bash
sudo apt-get install r-base
```

### Installing ImageMagick:

```bash
sudo apt install imagemagick-6.q16
```

### Installing Apache2:

```bash
sudo apt-get install apache2
sudo systemctl restart apache2
```

## Opening a Jupyter notebook on the AWS instance

The installed Anaconda Python lacks a web browser, and requires tunneling the connection to Jupyter via a localhost port (the original instructions can be found [here](https://towardsdatascience.com/setting-up-and-using-jupyter-notebooks-on-aws-61a9648db6c5)):

Open a new terminal window. Log into the AWS instance, connection the local host TCP port 8000 to remote host port 8888:

```bash
ssh -L 8000:localhost:8888 -i /path/to/admin.pem ubuntu@ec2-*.compute.amazonaws.com
```

Once logged into the EC2 instance, launch a juptyer notebook:

```bash
jupyter --port=8888 --no-browser
```

Jupyter will report an URL to the terminal window with a hex token that looks somethin like:

```bash
http://localhost:8888/?token=b63246942ed644eafe0bac6de1682f265d972d7fef0b3baf
```

Paste this into a web browser search bar and change the port to 8000, for example:

```bash
http://localhost:8000/?token=b63246942ed644eafe0bac6de1682f265d972d7fef0b3baf
```

Jupyter notebook should then display the Jupyter navigation window for the remote machine.

## Creating user accounts

User names and account names were organzied into files by their group name with the following format:

```bash
# in projectname.txt
FirstName FamilyName\tAccountName\n
```

Created a script that takes the `projectname.txt` files and creates account directories. The code in the script runs:

```bash
#!/bin/bash
project_name=$1;
project_root=/projects

sudo groupadd $project_name

sudo mkdir -p $project_root/$project_name/share
sudo chgrp -R $project_name $project_root/$project_name
sudo chmod 0770 $project_root/$project_name
sudo chmod 0770 $project_root/$project_name/share

for user in `cut -f2 $project_name.txt`
  do
      user_home=$project_root/$project_name/$user
      echo "$user => $user_home"
      sudo useradd -m $user -d $user_home -g $project_name -s /bin/bash
      sudo mkdir -p $user_home/.ssh
      sudo cp ~/PFB2018-student.pub $user_home/.ssh/authorized_keys
      sudo chown -R $user:$project_name $user_home/.ssh
      sudo chmod 0700 $user_home/.ssh
      sudo chmod 0400 $user_home/.ssh/authorized_keys
      sudo chmod 0700 $user_home
      echo 'done'
done
```



### Giving sudo permissions to group TA

**NOTE**: When the user tries to `sudo` they will be asked for a password, which is not set with the command below. I never set any passwords, so I don't know what the password was supposed to be, so this was not very useful:

```bash
sudo usermod -a -G sudo usrname
```

