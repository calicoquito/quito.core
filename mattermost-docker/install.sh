echo "Quito Core & Mattermost integration"
echo "======================================="
echo "#Downloading quito"
wget https://github.com/calicoquito/quito.core/releases/download/v00002/installer_linux.sh
chmod +x installer_linux.sh
./installer_linux.sh
cd quito
rm docker-compose.yml
echo "#Downloading Mattermost"
git clone https://github.com/mattermost/mattermost-docker.git
cd mattermost-docker
rm docker-compose.yml
rm .gitignore
wget https://github.com/calicoquito/quito.core/releases/download/v000021/docker-compose.yml
cd ..
mv mattermost-docker/* .
rm -rf mattermost-docker
echo "#Installing"
sudo docker-compose build
mkdir -pv ./volumes/app/mattermost/{data,logs,config}
sudo chown -R 2000:2000 ./volumes/app/mattermost/
cd ..
echo "Installtion Finish"
echo "To run type ( cd quito/ then ./run.sh )"
echo "To stop type ( docker-compose down )"
rm -- "$0"