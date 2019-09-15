@echo OFF
title Quito Core
echo Quito Core:Setup
mkdir quito
cd quito
mkdir quito.data
cd quito.data
mkdir blobstorage
mkdir filestorage
cd ..
powershell -c "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha1.1/power_scripts.zip' -OutFile ${PWD}/power_scripts.zip"
powershell -c "Expand-Archive "${PWD}/power_scripts.zip" ${PWD}"
del /f power_scripts.zip
powershell -c "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha1.1/docker-compose_solo_quito.yml' -OutFile ${PWD}/docker-compose_solo_quito.yml"
move docker-compose_solo_quito.yml docker-compose.yml
cd ..
echo Quito Core: Setup Successfully
echo "To run Quito core: <cd quito> then run  <start.bat> as administrator"
pause
del /f quito_installer_windows.bat
