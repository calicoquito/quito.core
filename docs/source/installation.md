Installation
============
- ### Complete with Mattermost
  The complete installation of Quito includes the the Plone add-on which would allow you to manage your 
  organization or event through the use of the available content types. The content types are also integrated with 
  mattermost which would allow each action to be replicated in mattermost. These actions includes:

  - Each instance of a plone site would result in a Mattermost team being created
  - Creating a new project in Plone which would result in a channel creation in Mattermost.
  - The members of each project would be added as well to the channel on mattermost
  - Modification or deletion of any of the above would result in the same action in Mattermost

  The complete installation for your operating system is below. 

   #### Linux
    To install Quito on linux you would need to download and run install.sh.
    This can be done in the terminal by running the following lines of command.
    ```
    wget https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha1.1/install.sh
    chmod +x install.sh
    ./install.sh
    ```
    After installation the you would be prompt to enter the quito directory and run start.sh to start the process using the default configuration 

   #### Windows

    To install Quito on linux you would need to download and run install.bat.
    This can be done in the terminal by running the following lines of command.
    ```
    CMD
    ----
    powershell -c "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha1.1/install.bat' -OutFile ${PWD}/install.bat"
    install.bat

    Powershell
    ----------
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha1.1/install.bat' -OutFile ${PWD}/install.bat
    ./install.bat

    ```
    After installation the you would be prompt to enter the quito directory and run start.bat to start the process using the default configuration 

   #### Post Installation
     To configure quito for personal and production use follow the instructions below.
     - ##### Configuration
        1) To Enable nginx proxy you would need to modify the docker-compose.yml file and uncomment the docker service for it.
          This would also require uncommenting the code for both app and quito-core.
            ```
            depends_on:
              - nginx-proxy
            ```
          After modifying the configuration you would need to edit the virtual host name for both quito.core and the "app" service.
          The environment variable file can be found in the env folder. 

        2) To use your personal configuration delete all the files without the ".sample" extension. After you would need to modify each ".sample" file. Each file is for each docker service. You would need to change the database credentials and enable the necessary  configurations. When you are done you may remove the ".sample" extension from the filename then start Quito.

     - ##### Getting started
        To start using Quito Core You may follow the documentation at:

- ### Partial Only Quito.Core
  The Partial installation of Quito only includes the the Plone add-on which would allow you to manage your organization or event through the use of the available content types. 
  

  The partial installation for your operating system is below.

  #### Linux
    To install Quito on linux you would need to download and run quito_installer_linux.sh
    This can be done in the terminal by running the following lines of command.
    ```
    wget https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha1.1/quito_installer_linux.sh
    chmod +x quito_installer_linux.sh
    ./quito_installer_linux.sh
    ```
    After installation the you would be prompt to enter the quito directory and run start.sh to start the process using the default configuration  
      

  #### Windows
    To install Quito on linux you would need to download and run install.bat.
    This can be done in the terminal by running the following lines of command.

    ```
    CMD
    ----
    powershell -c "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha1.1/quito_installer_windows.bat' -OutFile ${PWD}/quito_installer_windows.bat"
    quito_installer_windows.bat

    Powershell
    ----------
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://github.com/calicoquito/quito.core/releases/download/v1.0-alpha1.1/quito_installer_windows.bat' -OutFile ${PWD}/quito_installer_windows.bat
    ./quito_installer_windows.bat

    ```
    After installation the you would be prompt to enter the quito directory and run start.bat to start the process using the default configuration 
      

  #### Post Installation
    - ##### Getting started
        To start using Quito Core You may follow the documentation at:
      
Troubleshooting
---------------------
