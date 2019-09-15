Installation
============
Complete with Mattermost
------------------------
  The complete installation of Quito includes the the Plone add-on which would allow you to manage your 
  organization or event through the use of the available content types. The content types are also integrated with 
  mattermost which would allow each action to be replicated in mattermost. These actions includes:

  - Each instance of a plone site would result in a Mattermost team being created
  - Creating a new project in Plone which would result in a channel creation in Mattermost.
  - The members of each project would be added as well to the channel on mattermost
  - Modification or deletion of any of the above would result in the same action in Mattermost

  The complete installation for your operating system is below. 

##### Linux
To install Quito on linux you would need to download and run install.sh.
This can be done in the terminal by running the following lines of command.
```
wget https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha2/install.sh
chmod +x install.sh
./install.sh
```
After installation the you would be prompt to enter the quito directory and run start.sh to start the process using the default configuration 

##### Windows
To install Quito on linux you would need to download and run install.bat.
This can be done in the terminal by running the following lines of command.
```
CMD
----
powershell -c "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha2/install.bat' -OutFile ${PWD}/install.bat"
install.bat

Powershell
----------
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha2/install.bat' -OutFile ${PWD}/install.bat
./install.bat

```
After installation the you would be prompt to enter the quito directory and run start.bat to start the process using the default configuration 

Partial Only Quito Core
------------------------
The Partial installation of Quito only includes the the Plone add-on which would allow you to manage your organization or event through the use of the available content types. 
  
The partial installation for your operating system is below.

##### Linux
To install Quito on linux you would need to download and run quito_installer_linux.sh
This can be done in the terminal by running the following lines of command.
```
wget https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha2/quito_installer_linux.sh
chmod +x quito_installer_linux.sh
./quito_installer_linux.sh
```
After installation the you would be prompt to enter the quito directory and run start.sh to start the process using the default configuration  
      

##### Windows
To install Quito on linux you would need to download and run install.bat.
This can be done in the terminal by running the following lines of command.

```
CMD
----
powershell -c "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha2/quito_installer_windows.bat' -OutFile ${PWD}/quito_installer_windows.bat"
quito_installer_windows.bat

Powershell
----------
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha2/quito_installer_windows.bat' -OutFile ${PWD}/quito_installer_windows.bat
./quito_installer_windows.bat

```
After installation the you would be prompt to enter the quito directory and run start.bat to start the process using the default configuration

Test Data
----------
- Quito also came with dummy data that can be used to better understand the architecture of the system. It high required yhat this data is not used to run an instance of quito that is meant for professional use. 
- The dummy data can be installed to your quito instance by going to your quito directory and running 

```
Linux 
-------

wget https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha2/quito_test_data.tar.gz
tar xvfz quito_test_data.tar.gz
rm -rf quito_test_data.tar.gz

Windows
-------

powershell -c "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha2/quito_test_data.zip' -OutFile ${PWD}/quito_test_data.zip"
powershell -c "Expand-Archive "${PWD}/quito_test_data.zip" ${PWD}"
del /f quito_test_data.zip
```
This can also be acccomplished by downloading the [zip file](https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha2/quito_test_data.zip) and unzipping it in the quito directory

