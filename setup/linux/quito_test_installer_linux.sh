#!/bin/bash 
echo "Quito Core(Test): Setup"
mkdir quito
cd quito
wget https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha1.1/quito_test_data.tar.gz
tar xvfz quito_test_data.tar.gz
rm -rf quito_test_data.tar.gz
wget https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha1.1/power_scripts.tar.gz
tar xvfz power_scripts.tar.gz
rm -rf power_scripts.tar.gz
wget https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha1.1/docker-compose_solo_quito.yml
mv docker-compose_solo_quito.yml docker-compose.yml
wget https://github.com/calicoquito/quito.core/releases/download/v00002/Quito_API_Guide.Insomnia.json
setfacl  -R -m u:500:rwX quito.data
chmod +x start.sh
chmod +x stop.sh
echo "Quito Core(Test): Setup Successfully"
echo "To run Quito core: cd quito (then) ./start.sh"
cd ../
rm -- "$0"
