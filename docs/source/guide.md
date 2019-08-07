Guide on how to use Quito
==========================

This Guide consist of the documentation on how to manipulate the various functionailty that comes with Quito. 
It will cover all the data types and all the configuration on the site

Project List
-------------
- The project List is a container that which is used to sort a set of project base on the criteria that is set for the project. This criteria could include being in a folder, publish, unpublish for a specific date and more.

- No you cant have nested project list but you could have project list witht the criteria being set to another project list.  

##### Creation

##### Modification

##### Deltetion

Project
--------
- The Project is a content type which can be used to create a project or event. This project or event can have members and who are assigned to it, an image and the other factors to describe what that project is. 
- You can have nested projects, however, it is advice to reduce creating them
- A project can be a container to also a task , task list or a group
- A creation of a project in plone will prompt a creation of a channel in mattermost. The member of the project will be added to the channel if they are available. 

##### Creation

##### Modification

##### Deltetion

Task
-----
- A task is a content type that can be used to describe a specific activity that should be done for a project. A task can have two states depending on if it is completed or not and members can be attached to a task
- A task can also only exist within a project or Task list. 

##### Creation

##### Modification

##### Deltetion

Task List
----------
- A task list is a folder like object that can be used to group relating tasks together.
- A task list can only exist within a project

##### Creation

##### Modification

##### Deltetion

Groups
------
- A group is an object to hold a list of members. 
- A group can be used to add or remove a list of members with similar interest to a project or task
- A group can only exist within a taks list or task

##### Creation

##### Modification

##### Deltetion