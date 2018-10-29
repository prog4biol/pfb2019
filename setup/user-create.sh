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

