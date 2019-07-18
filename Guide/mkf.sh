echo "Making zip files"
cd mattermost-docker
tar -czvf quito_full.tar.gz env/ docker-compose.yml
zip -r quito_full.zip env/ docker-compose.yml
cd ..
tar -czvf quito_test_data.tar.gz quito.data/
zip -r quito_test_data.zip quito.data/
cd linux
tar -czvf power_scripts.tar.gz start.sh stop.sh
cd ..
cd windows
zip -r power_scripts.zip start.bat stop.bat
cd ..
mv {mattermost-docker/quito_full.tar.gz,mattermost-docker/quito_full.zip} .
mv {linux/power_scripts.tar.gz,windows/power_scripts.zip} .