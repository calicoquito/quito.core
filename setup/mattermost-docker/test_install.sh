#!/bin/bash 
echo "Quito Core with Mattermost "
echo "======================++"
echo "#Downloading quito files"
wget https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha1.1/quito_test_installer_linux.sh
chmod +x quito_test_installer_linux.sh
./quito_test_installer_linux.sh
cd quito
rm docker-compose.yml
echo "#Downloading Mattermost files"
git clone https://github.com/mattermost/mattermost-docker.git
cd mattermost-docker
rm docker-compose.yml
rm .gitignore
wget https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha1.1/quito_full.tar.gz
tar xvfz quito_full.tar.gz
rm -rf quito_full.tar.gz
cd ..
mv mattermost-docker/* .
rm -rf mattermost-docker 
cp env/app.env.sample env/app.env
cp env/db.env.sample env/db.env
cp env/quito.env.sample env/quito.env
cp env/web.env.sample env/web.env
cd env 
python createPass.py
rm createPass.py
cd ..
echo "#Installing"
docker-compose build
mkdir -pv ./volumes/app/mattermost/{data,logs,config}
chown -R 2000:2000 ./volumes/app/mattermost/
setfacl  -R -m u:500:rwX ./volumes/quito.data
cd ..
echo "Installtion Finish"
echo "To run type ( cd quito/ then ./start.sh )"
echo "To stop type ( ./stop.sh )"
rm -- "$0"
