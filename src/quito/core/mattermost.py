from zope.component import getUtility
from plone import api
from mattermost_helper import *
import string, pdb

error = '-1'
good = '1'

#Use by plone to create channel when project is created and add users
def ploneCreateChannel(item, event):
	if useMattermost() :
		#pdb.set_trace()
		#check if admin was added and add admin to team
		ploneAddAdmin()
		#add any latent users
		ploneAddlatentUsers()
		#create the vhannel 
		token = authenticate(getSAUsername(),getSAPassword())
		if token != error:
			team_id = getTeamID(token,getTeamName())
			name = str(item.title)
			name_id = str(item.id)
			description = str(item.description)
			createChannel(token,team_id, name_id, name, description)
			channel_id = getChannelID(token, team_id, name_id)
			addAdminsToChannel(token, team_id, channel_id)
			addMembersToChannel(token, team_id,channel_id, item.members)

#use by plone to delete a channel when a project is deleted	
def ploneDeleteChannel(item, event):
	if useMattermost() :
		token = authenticate(getSAUsername(),getSAPassword())
		if token != error:
			team_id =  getTeamID(token,getTeamName())
			#pdb.set_trace()
			name_id = str(item.id)
			channel_id = getChannelID(token, team_id, name_id)
			deleteChannel(token, channel_id)

def ploneModifyChannel(item, event):
	if useMattermost() :
		#pdb.set_trace()
		#add the latent users before applying modification
		ploneAddlatentUsers()
		#continue with the channel modification
		token = authenticate(getSAUsername(),getSAPassword())
		if token != error:
			team_id =  getTeamID(token,getTeamName())
			name_id = str(item.id)
			channel_id = getChannelID(token, team_id, name_id)
			name = str(item.title)
			description = str(item.description)
			modifyChannel(token, channel_id, name, description)
			delMemberFromChannel(token, team_id,channel_id, item.members)
			addAdminsToChannel(token, team_id, channel_id)
			addMembersToChannel(token, team_id,channel_id, item.members)

def ploneCreateTeam(portal):
	if useMattermost() :
		#pdb.set_trace()
		token = authenticate(getSAUsername(),getSAPassword())
		if token != error:
			team_name = portal.getPhysicalPath()[1]
			createTeam(token, team_name)

def ploneDeleteTeam(portal):
	if useMattermost() :
		#pdb.set_trace()
		token = authenticate(getSAUsername(),getSAPassword())
		if token != error:
			team_name = portal.getPhysicalPath()[1].lower().replace(" ","_")
			team_id = getTeamID(token, team_name)
			deleteTeam(token, team_id)

def ploneConfigMattermost():
	if useMattermost() :
		#pdb.set_trace()
		if(authenticate(getSAUsername(), getSAPassword()) ==  error):
			createSuperAdmin(getSAUsername(), getSAPassword())
		token = authenticate(getSAUsername(), getSAPassword())
		if token != error:
			setupConfiguration(token)

def ploneAddAdmin():
	if useMattermost() :
		#pdb.set_trace()
		token = authenticate(getSAUsername(),getSAPassword())
		if token != error:
			team_id =  getTeamID(token,getTeamName())
			if(not isAdminAdded(token, team_id)):addAdminToTeam(token, team_id)

def ploneAddlatentUsers():
	if useMattermost() :
		token = authenticate(getSAUsername(),getSAPassword())
		if token != error:
			team_id =  getTeamID(token,getTeamName())	
			users = api.user.get_users()
			users_usernames = [x.getUserName() for x in users]
			addLatentUsers(token, team_id, users_usernames)

def ploneDataCheck(item = "", event = ""):
	if useMattermost() :
		#pdb.set_trace()
		try:
			ploneAddAdmin()
			ploneAddlatentUsers()
		except Exception:
			print"============ Data Check Failed ================="
#def test2(item = "", event = ""):
	#print item
	#pdb.set_trace()


# if __name__== "__main__":
	#token = authenticate(admin_username,getSAPassword())
	#eam_id = getTeamID(token,"quito")
	#channel_id = getChannelID(token,team_id)
	#deleteChannel(token, channel_id)
	#print createChannel(token,team_id, "abcd")
	#print team_id
	#channel_id = getChannelID(token,team_id, "abc")
	#print addMembersToChannel(token, team_id, channel_id,["user1","user2","user3"])
	#print delMemberFromChannel(token, team_id, channel_id,["user1"])
	#print deleteTeam(token, team_id)
	#print isAdminAdded(token, team_id)
	#if(not isAdminAdded(token, team_id)):print addAdminToTeam(token, team_id)
	#print addAdminToTeam(token, team_id)
	#print addLatentUsers(token, team_id, ["user1", "user2"])
	#print addAdminToChannel(token, team_id, channel_id)