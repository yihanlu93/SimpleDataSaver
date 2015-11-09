#!/bin/bash

sudo apt-get install python-pip -y
    
sudo pip install Django==1.8.6

sudo debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password password rootpass'
sudo debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password_again password rootpass'
sudo apt-get update
sudo apt-get -y install mysql-server-5.5
sudo apt-get -y install libmysqlclient-dev

if [ ! -f /var/log/databasesetup ];
then
    echo "CREATE USER 'wordpressuser'@'localhost' IDENTIFIED BY 'wordpresspass'" | mysql -uroot -prootpass
    echo "CREATE DATABASE firstblog" | mysql -uroot -prootpass
    echo "GRANT ALL ON wordpress.* TO 'wordpressuser'@'localhost'" | mysql -uroot -prootpass
    echo "flush privileges" | mysql -uroot -prootpass

    touch /var/log/databasesetup

    if [ -f /vagrant/data/initial.sql ];
    then
        mysql -uroot -prootpass wordpress < /vagrant/data/initial.sql
    fi
fi

sudo apt-get -y install python-dev
sudo apt-get -y install libffi-dev
sudo apt-get -y install libssl-dev
sudo easy_install mysql-python

sudo python /srv/website/server/FirstBlog/manage.py syncdb --noinput

echo "Please type \"sudo python /srv/website/server/FirstBlog/manage.py runserver 0.0.0.0:66 \" in vagrant virtual machine"
echo "You can access web server from your browser at \"55.55.55.5:66\""



exit