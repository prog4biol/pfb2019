lsblk
## find the device name
device='/dev/xvdb'
sudo file $device
sudo mkfs -t ext4 $device

sudo mkdir /data
sudo mount $device /data
sudo cp /etc/fstab /etc/fstabBAK

# find the UUID for $device
sudo file -s $device
sudo vi /etc/fstab

 `UUID=b0992451-8b09-4df9-94ee-2729aa100bcc	/data	ext4	defaults,nofail02`

sudo umount /data
sudo mount /data



mkdir /data/project
sudo chgrp -R project /data/project
sudo chmod g+wrx /data/project/


sudo groupadd project

echo 'PASTE PUB KEY HERE' > PFB2017_Projects.pub 

## add user names to file called users.txt

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

