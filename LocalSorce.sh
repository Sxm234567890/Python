#!/bin/bash
#tar -cvf repo.tar /etc/yum.repos.d/*
#mv /etc/yum.repos.d/repo.tar  /tmp   如果是yum自身带的国外的yum源地址就可以打包带走
cd /etc/yum.repos.d/
>dvd.repo # 这个命令是重定向操作符 ，如果文件存在会清空内容，不存在会创建一个该文件
#echo '[dvd]'  >> dvd.repo
#echo 'name=dvd'   >>dvd.repo
#echo "baseurl=file:///mnt.cdrom" >>dvd.repo
#echo "gpgcheck=0"  >>dvd.repo
 echo -e  '[dvd]\n name=dvd\n  baseur=file:///mnt.cdrom\n  gpgcheck=0' >>dvd.repo
mkdir /mnt/cdrom
mount /dev/cdrom /mnt/cdrom
sed -i '1i\mount /dev/cdrom  /mnt/cdrom'  /root/.bashrc  #系统开机自动挂载
yum clean all
yum makecache
#确保系统光盘通电


