# Setting up AWS Instances

Just keeping notes

1. Ubuntu 16.04 OS 
2. A single m4.4xlarge for each group
3. Added 250G of EBS storage to each
4. Used admin pem to start up machines
4. Elastic IP for each
5. Created a record set in Route 53 for 'programmingforbiology.org' for each 'groupname.programmingforbiology.org'
6. added the project group and ta users to one project machine
7. Told them to set up a new github repository for all their scripts to save
8. Set up users and directories with a [shell script](project_aws.sh)
    - Created a group called 'project'
    - Created a directory called 'project'
    - Added all students to project group
    - add student pem to student ~/.ssh/authorized_keys
9. Make sure to put the private key on each student desktop computer
