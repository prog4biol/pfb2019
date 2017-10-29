
# Format and mount drive

## find the device name
```
lsblk
device='/dev/xvdb'
sudo file $device
sudo mkfs -t ext4 $device
```

## make a directory to mount the drive
```
sudo mkdir /data
sudo mount $device /data
sudo cp /etc/fstab /etc/fstabBAK
```

## find the UUID for $device
```
sudo file -s $device
```

## add the following line to the fstab file
```
sudo vi /etc/fstab

UUID=b0992451-8b09-4df9-94ee-2729aa100bcc	/data	ext4	defaults,nofail 0 2
```

## test fstab entry
```
sudo umount /data
sudo mount /data
```

# Add users and group

## add group
```
sudo groupadd project
```

## create group directory
```
sudo mkdir /data/project
sudo chgrp -R project /data/project
sudo chmod g+wrx /data/project/
```

## add student pub key
```
echo 'PASTE PUB KEY HERE' > PFB2017_Projects.pub 
```


## add user names to file called users.txt
```
for i in `cat users.txt`
  do
    echo $i
    sudo useradd -m $i -d /data/$i -g project -s /bin/bash
    sudo mkdir /data/$i/.ssh
    sudo cp ~/PFB2017_Projects.pub /data/$i/.ssh/authorized_keys
    sudo chown -R $i:project  /data/$i/.ssh
    sudo chmod 0700  /data/$i/.ssh
    sudo chmod 0400  /data/$i/.ssh/authorized_keys
    echo 'done'
done
```

# Install

##  update
`sudo apt-get update`

## Install anaconda from anaconda.org
```
curl -OL https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
sudo sh Anaconda3-5.0.1-Linux-x86_64.sh
```
### Directory to install anaconda
`/usr/local/anaconda`

### edit /etc/bash.bashrc
```
PATH=/usr/local/anaconda/bin:$PATH
export PATH

LIBRARY_PATH=/usr/local/anaconda/lib:$LIBRARY_PATH
export LIBRARY_PATH

LD_LIBRARY_PATH=/usr/local/anaconda/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH
```

### Allow users to use conda install
```
sudo chgrp -R project /usr/local/anaconda
sudo chmod -R g+w /usr/local/anaconda
```

## install emacs
`sudo apt-get install emacs`

## install make
`sudo apt-get make`
`sudo apt-get make-doc`

## install gcc and fortran
`sudo apt-get install gcc`
`sudo apt-get install gfortran`

## install apache
`sudo apt-get install apache2`
`sudo systemctl restart apache2`

## install java 8
`sudo apt-get install default-jdk`

## install R/Rscript
`sudo apt-get install r-base`

