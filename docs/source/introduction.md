Introduction
============

![](https://user-images.githubusercontent.com/9387134/61511916-dfca4900-a9bd-11e9-864c-285a92e39251.png)

Quito is an open source project to manage the operations of Organisation, with an initial focus on churches. The software will enable churches to automate common administrative, management and reporting tasks. This will help the Church Leadership Team to improve communications, streamline daily operations and support collaboration.The system would be modular which would make developing the software and customizing the software easier for the users.

-----------


Alpha 1.O
---------

- Alpha version 1.0 is an integration with the Plone quito.core add-on and Mattermost. This allows each user to communicate with each other through channels on Mattermost that are interconnected to Projects in Plone.
This version would allow the user to create a project/event. This project/event could be added to a list that contains relating projects. 
- Each project can contain tasks that can be assigned to one or more participants of the project. 
- Tasks can be organized under a task list with relating tasks.
- Groups can also be added to projects or tasks. Groups are used to contain multiple users with similar relations.

#### Features
- Mattermost and Plone Integration
- Project List
- project
- Task 
- Task List
- Group
- Chat channels for projects

#### Out the Box

Quito out of the functions in a docker conmtainer that makes running the services simple and the setup easy

Dependencies
----------------------
- Docker
- Docker-Compose
- Server