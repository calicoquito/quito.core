from zope.component import getUtility
from plone import api
import string, os, pdb

error = -1
good = 1

memberRole = ['Contributor','Reader']

def removeAllUsersFromProject(project):
	ploneMembers = api.user.get_users()
	for user in ploneMembers:
		api.user.revoke_roles(username=user.id,roles=memberRole,obj=project)

def addUserToProject(project):
	members = project.members
	ploneMembers = api.user.get_users()
	availableMember = []
	for user in ploneMembers:
		if(user.id in members or user.getProperty('email') in members or user.getProperty('fullname') in members):
			availableMember.append(user.id)
	for member in availableMember:
		api.user.grant_roles(username=member,roles=memberRole,obj=project)
