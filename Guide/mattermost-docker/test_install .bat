@echo OFF
title Quito Core
echo Downloading quito file
powershell -c "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://github.com/calicoquito/quito.core/releases/download/v00003/quito_installer_windows.bat' -OutFile ${PWD}/quito_test_installer_windows.bat"
quito_test_installer_windows.bat
cd quito 
del /f docker-compose.yml
echo Downloading Mattermost files
git clone https://github.com/mattermost/mattermost-docker.git
cd mattermost-docker
del /f docker-compose.yml
del /f .gitignore
powershell -c "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://github.com/calicoquito/quito.core/releases/download/v00003/quito_full.zip' -OutFile ${PWD}/quito_full.zip"
powershell -c "Expand-Archive "${PWD}/quito_full.zip" ${PWD}"
del /f quito_full.zip
cd ..
move mattermost-docker/* .
del mattermost-docker
copy env/app.env.sample env/app.env
copy env/db.env.sample env/db.env
copy env/quito.env.sample env/quito.env
copy env/web.env.sample env/web.env
echo Installing
docker-compose build
mkdir -pv ./volumes/app/mattermost/{data,logs,config}
cd ..
echo Installtion Finish
echo To run in the quito folder run start.bat )
echo To stop run stop.bat )
pause
del /f test_install.bat