from zope.component import getUtility
from quito_scripts_helper import *
import string, pdb

def ploneAddUsersToProject(item, event):
	addUserToProject(item)

def ploneUpdateProjectUsers(item, event):
	removeAllUsersFromProject(item)
	addUserToProject(item)