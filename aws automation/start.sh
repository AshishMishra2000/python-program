#! /bin/bash

yum update -y
sudo yum install -y httpd24 php56 php56-mysqlnd
sudo service httpd start
sudo chkconfig httpd on
sudo groupadd www 
sudo usermod -a -G www ec2-user 
exit