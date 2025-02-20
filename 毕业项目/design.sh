2 8G 40G
git init .
git clone https://github.com/zhulinn/SpringBoot-Angular7-Online-Shopping-Store.git
#解决npm的错误
yum install -y python3
ln -s /usr/bin/python3 /usr/bin/python
export PYTHON=/usr/bin/python
#npm config set python /usr/bin/python  如果npm还报错

yum remove -y nodejs npm
curl -fsSL https://rpm.nodesource.com/setup_18.x | bash -
yum install -y nodejs
rm -rf node_modules package-lock.json
npm cache clean --force
npm install
#npm audit fix --force 


npm config set registry https://registry.npmmirror.com
npm install --verbose


npm list -g --depth=0 | grep @angular/cli #检查是否安装Angular CLI
npm install -g @angular/cli     #安装
export PATH=$PATH:$(npm bin -g)  #添加环境变量
ng build --prod  #执行
 

#安装java 11 ,maven 包下载安装
wget https://dlcdn.apache.org/maven/maven-3/3.9.6/binaries/apache-maven-3.9.6-bin.tar.gz
#PATH=(maven-*/bin):$PATH
mvn -version #康康是不是对应的是java11
#安装的是清华源的docker 

