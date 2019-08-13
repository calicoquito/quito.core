Guide on how to use Quito
==========================

This Guide consist of the documentation on how to manipulate the various functionailty that comes with Quito. 
It will cover all the data types and all the configuration on the site

Project List
-------------
- The project List is a container that which is used to sort a set of project base on the criteria that is set for the project. This criteria could include being in a folder, publish, unpublish for a specific date and more.

- No you cant have nested project list but you could have project list witht the criteria being set to another project list.  

##### Creation
- To create a new Project List you would first need to Login to your Plone site for Quito. After doing so you need to select content 

![](images/projectList/toContents.png)

- In the root directory you can create a folder and enter the root of that folder or you could create the new project List in the root of your directory. For this tutorial a project list would be added to the root of the main directory. 

![](images/projectList/toContent.png)

- On the left of the screen you would see the **add new button**. Press it and then select Project list as shown below.

![](images/projectList/addProlist.png)

- When you have done that you would be greeted with the form for the project List. Enter the name and summary.

![](images/projectList/add_p_list_screen.png)

- For the project list you would need to add the criteria for the contents that you would like to search for in the list. The main criteria that you must have is the criteria of **type = Project**. You may select the criterias as shown in the picture below. 

![](images/projectList/add_p_list_screen2.png)

- When you are done you are able to write some html/ use the editor To show static content to describe the screen then press **Save**.

![](images/projectList/save_Plist.png)

- Successful creation would lead you to the Project List display screen. 

![](images/projectList/plistcreated.png)

- ***Congratulations you have created your project list***

##### Modification
- You need to Login to Plone first
- To modify your project List you first need to open into your project list 
- when your on its display screen like below you need to select **Edit** from the menu on the left

![](images/projectList/edit_plist.png)

- After you should be greeted with the screen with the forms.

![](images/projectList/edit_plist_screen1.png)

- Make your changes and after you have editted your project list press the **Save** button

![](images/projectList/save_plist_edit.png)

- Your changes have been made and your project list editted.

##### Deltetion
*Warning this process is not reversable*
- You need to login to plone first 
- To delete your project you need enter into your project list. 
- In your project on the left side of the screen select the Actions button

![](images/projectList/go_to_del_plist.png)

- After you would see the option to **delete** select the option

![](images/projectList/plist_press_del.png)

- Finally you would need to confirm the delete (note this object would not be able to be retrieved after this).

![](images/projectList/confirm_plist_del.png)

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