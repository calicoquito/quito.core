Integrations and Plone Scripts
===============================
There are four main scripts that currently controls the Logics for Quito Core. These are the mattermost.py and quito_scripts.py along with their helpers
- The mattermost script is used to control how the two systems integrate 
- The quito script is used to control how the internal logic and worklow react to changes on the system

mattermost.py
--------------
The mattermost.py script has the main codes that are used to control how mattermost react with plone.
- It relys on the plone api to gather information from the plone system and send it to the mattermost system.
- Each plone method in the scripts are called from the configure.zcml whenever the related Plone event occur. 
- The script controls the Configuration of the mattermost system 
- It creates, configure and delete mattermost teams, channels and users based on the event that happen in plone and information that is sent.
- The helper scripts are used to conduct all the smaller jobs and processes to make it possible. 

quito_scripts.py
-----------------
- This script is currently used to do two basic activities in plone. 
- The methods are aonly called when the appropriate event is triggered from the configure.zcml file.
- This script controls the addtion and deletion of plone users through changing their permissions in plone projects and tasks.
  