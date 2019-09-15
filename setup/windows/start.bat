@echo OFF
title Quito Core
::echo "Prepaing volume"
::setfacl  -R -m u:500:rwX quito.data
echo Starting ...
docker-compose up -d
echo Quito Core: Running
echo To stop Quito Core run : stop.bat
pause
