#! /bin/bash

yum update -y
yum install -y httpd
service httpd start

mkdir /var/www/html/scripts /var/www/html/styles

wget https://assignment0.s3.ap-south-1.amazonaws.com/index.html -P /var/www/html
wget https://assignment0.s3.ap-south-1.amazonaws.com/style.css -P /var/www/html
wget jsfile -P /var/www/html/scripts