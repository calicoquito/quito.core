Setup Files
===========
The release files and script can be found under the setup directory.
This includes the docker compose files along with the scripts to install and run quito core in docker

Quito Scripts
--------------

- The automatic installer for quito core for Linux and windows is written in a scripting language for the Operating system (Linux Bash and Windows BAT)

- The installer scripts have the installer key word in its name while the scripts to run quito have the names **Start and Stop**

- The **make_release_files.sh script** is use to simplify the creation of the zip files for the Quito core release. It is used to create all the installation instances.

- The above script also rely on the quito.data directory to exist. This directory have to be manually created. This directory would contain demo data that can be used with a quito instance. This can be easily created by adding the ***BlobStorage and Filestorage*** directory to the file from a previously created plone instance.

- There are three directories: Linux, windows and mattermost-docker
 	- The linux directory contains the Quito standalone installation scripts along with the start and stop scripts
 	- The windoes directory contaains the Quito standalone installation scripts along with the start and stop scripts
 	- The mattermost-docker directory contains the installation files along with the docker compose files and environment variable files for the complete installation of Quito core that includes mattermost integration

Docker compose files
---------------------

- The docker-compose.yml file contains the name of the required images along with the env files that contains the envirnment varibales

- There are currently two docker compose files. The one that is found in the mattermost-docker directory includes the mattermost images for docker along with Quito Core. 

- The docker compose solo quito file only contain the docker image startup information. 

Environment files
------------------
- The environment variables for Quito docker image and mattermost can be found in the env directory

- These are sample files and must not be used in a real project. They are there to provide guidance

- The app, db and web env files are related to mattermost while the other two is for Quito environment setting

- The cretaePass.py script is used to create an encrypted password for the Quito.bot that is used to integrate Plone with mattermost. This script should only be called after installation of the quito system and not before. It will create  the mattermost_cred.env file that contains the encrypted information for the Quito Bot (Incorrect usage of this file may cause failure in integration). 

Docker and Image files
--------------------

- To create the Docker image the Dockerfile is used to do so. This contains the code for the plone version and global environment varibales initialization for the quito system.

- The auxilary configuration file is called **docker.cfg**. It is required that the user information for plone is changed from admin:admin to something more secure.

- The docker.cfg and dockerfile follows the plone configuration in creating a docker image based on Plone.

- The current version of plone being used is 5.15

- The repository is connected to the Quito.Core docker hub repository that automatically build the quito.core image on each push instance [it can be found here.](https://cloud.docker.com/u/progsmart/repository/docker/progsmart/quito.core)

Plone and Plonecli
-------------------

- The plone setting for Quito can be found in the Setup.py files

- The Core addon for quito along with all the addons for quito can be found in the src/quito directory. 

- The core addon of quito contains the content types used along with the core code for the integrtion of mattermos and Plone through the Quito Bot also called **SuperAdmin**.

- The plonecli can be used to easily create additional plone functionalities. To get help you need to install plonecli using PIP. Then you would be able to call plonecli -h in the Quito.core main directory. [Link to their repository](https://github.com/plone/plonecli).

Additional Insomania file
-------------------------
- The quito core insomnia APi documentation can also be found in the setup directory for offline view.(Note its not as updated as the Postman Documentation)