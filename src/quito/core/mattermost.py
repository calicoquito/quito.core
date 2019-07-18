import requests, json
import random, string
import pdb
from plone import api

Host = "http://localhost"+"/api/v4"
admin_username = "admin"
error = -1
good = 1

# get the team name 
def getTeamName():
	portal = api.portal.get()
	return portal.getPhysicalPath()[1].lower().replace(" ","_")

#Returns a token to be used on a successdul response
def authenticate(login_id, password):
	try:
		url = Host+"/users/login"
		auth = {"login_id":login_id,"password":password}
		response = requests.post(url, data = json.dumps(auth))
		if(response.status_code == 200):
			return response.headers['Token']
		return error
	except Exception:
		return error

#Use to get the team id for a specific team with name		
def getTeamID(token, name):
	url = Host+"/teams"
	header = {'Authorization': 'Bearer ' + token, 
				'Accept': 'application/json'}
	response = requests.get(url , headers = header)
	if(response.status_code == 200):
		for team in response.json():
			if(team["name"] == name):
				return team["id"]
	return error

#Get the Id for the channel
def getChannelID(token, team_id, name_id):
	url = Host+"/teams/"+team_id+"/channels/name/"+name_id
	header =  {'Authorization': 'Bearer ' + token, 
				'Accept': 'application/json'}
	response = requests.get(url, headers = header)
	if(response.status_code == 200):
		return response.json()["id"]
	return error

# Creaate a new channel given the name and its information
def createChannel(token, team_id, name_id = "project", name = "Project",description = "Quito Channel", visibility = "O"):
	url = Host+"/channels"
	header = {'Authorization': 'Bearer ' + token, 
				'Accept': 'application/json',
				'Content-Type': 'application/json'}
	data = {
	  "team_id": team_id,
	  "name": name_id,
	  "display_name": name,
	  "purpose": description,
	  "header": description,
	  "type": visibility
	}
	response = requests.post(url, data = json.dumps(data), headers = header)
	if(response.status_code == 201):
		return 0
	return error

#Delete a channel using its ID	
def deleteChannel(token, channel_id):
	url = Host+"/channels/"+channel_id
	header =  {'Authorization': 'Bearer ' + token, 
				'Accept': 'application/json'}
	response = requests.delete(url, headers = header)
	if (response.status_code == 200):
		return good
	return error

def modifyChannel(token, channel_id, name = "Project",description = "Quito Channel"):
	url = Host+"/channels/"+channel_id+"/patch"
	header = {'Authorization': 'Bearer ' + token, 
				'Accept': 'application/json',
				'Content-Type': 'application/json'}
	data = {
			  "display_name": name,
			  "purpose": description,
			  "header": description
			}
	response = requests.put(url, data = json.dumps(data), headers = header)
	if (response.status_code == 200):
		return good
	return error

def addMembersToChannel(token, team_id, channel_id, members = []):
	#pdb.set_trace()
	list_url = Host+"/teams/"+team_id+"/members"
	add_url = Host+"/channels/"+channel_id+"/members"
	header =  {'Authorization': 'Bearer ' + token, 
				'Accept': 'application/json',
				'Content-Type': 'application/json'}
	response = requests.get(list_url, headers = header)
	if(response.status_code == 200):
		members_list = response.json()
		for user in members_list:
			user_url = Host+"/users/"+user['user_id']
			response2 = requests.get(user_url, headers = header)
			if(response2.status_code == 200):
				userdata = response2.json()
				fullname =  ""+userdata['first_name']+" "+userdata['last_name']+""
				if(userdata['username'] in members or userdata['nickname'] in members or fullname in members or userdata['email'] in members):
					data = {"user_id": user['user_id']}
					response3 = requests.post(add_url, data = json.dumps(data), headers = header)
					print(response3.status_code)

	return good

def delMemberFromChannel(token, team_id, channel_id, members = []):
	#pdb.set_trace()
	list_url = Host+"/channels/"+channel_id+"/members"
	header =  {'Authorization': 'Bearer ' + token, 
				'Accept': 'application/json'}
	response = requests.get(list_url, headers = header)
	if(response.status_code == 200):
		members_list = response.json()
		for user in members_list:
			user_url = Host+"/users/"+user['user_id']
			response2 = requests.get(user_url, headers = header)
			if(response2.status_code == 200):
				userdata = response2.json()
				fullname =  ""+userdata['first_name']+" "+userdata['last_name']+""
				if (not (userdata['username'] in members or userdata['nickname'] in members or fullname in members or userdata['email'] in members or userdata['username'] == admin_username)):
					del_url = Host+"/channels/"+channel_id+"/members/"+user['user_id']
					response3 = requests.delete(del_url, headers = header)
					print(response3.status_code)
	return good

def createTeam(token, team_name = "Quito Team", types = "O"):
	#pdb.set_trace()
	url = Host+"/teams"
	header =  {'Authorization': 'Bearer ' + token, 
				'Accept': 'application/json',
				'Content-Type': 'application/json'}
	data = {
			  "name": team_name.lower().replace(" ","_"),
			  "display_name": team_name,
			  "type": types
			}
	response = requests.post(url,  data = json.dumps(data), headers = header)
	if(response.status_code == 201):return good
	return error

def deleteTeam(token, team_id):
	#pdb.set_trace()
	url = Host+"/teams/"+team_id
	header =  {'Authorization': 'Bearer ' + token, 
				'Accept': 'application/json'}
	params = {"permanent": True}
	response = requests.delete(url,  params = params, headers = header)
	if response.status_code == 200: return good
	return error

def makePassword(stringLength=20):
    """Generate a random string of letters, digits and special characters """
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

def createSuperAdmin(user_name, password):
	try:
		url = Host+"/users"
		header = {'Content-Type': 'application/json'}
		data = {
				"email": user_name+"@"+Host.replace("https://","").replace("http://","").replace("/api/v4",""),
				"username": user_name,
				"password": password
				}
		response = requests.post(url, data = json.dumps(data), headers = header)
		if(response.status_code == 201):
			saveSAPassword(password)
			return good
		return error
	except Exception:
		return error

def saveSAPassword(password):
	#pdb.set_trace()
	file = open("SA_CRED.enc","w")
	file.write("1")
	file.write(password)
	file.close()

def getSAPassword():
	try:	        
		file = open("SA_CRED.enc","r")
		response = file.read()
		file.close()
		if(response != ""):
			if(response[0] == "1"):return response[1:]
		return error
	except Exception:
		return error

def setupConfiguration(token):
	#pdb.set_trace()
	url = Host+"/config"
	header =  {'Authorization': 'Bearer ' + token, 
				'Accept': 'application/json',
				'Content-Type': 'application/json'}
	response = requests.get(url, headers = header)
	if(response.status_code == 200):
		data = response.json()
		data["ServiceSettings"]["EnableEmailInvitations"] = True
		data["ServiceSettings"]["EnableAPITeamDeletion"] = True
		data["TeamSettings"]["SiteName"] = "Quito"
		data["TeamSettings"]["MaxUsersPerTeam"] = 9000
		data["TeamSettings"]["EnableUserCreation"] = True
		data["TeamSettings"]["EnableOpenServer"] = True
		data["TeamSettings"]["EnableUserDeactivation"] = True
		data["TeamSettings"]["EnableTeamCreation"] = False
		response2 = requests.put(url, data = json.dumps(data), headers = header)
		if(response.status_code == 200):return good
	return error

def addAdminToTeam(token, team_id):
	#pdb.set_trace()
	user_url = Host+"/users"
	header =  {'Authorization': 'Bearer ' + token, 
				'Accept': 'application/json',
				'Content-Type': 'application/json'}
	response = requests.get(user_url, headers = header)
	if(response.status_code == 200):
		members = response.json()
		admin_id = ""
		admin_date = 0
		for user in members:
			if(user["username"] != admin_username):
				create_date = user["create_at"]
				#print create_date
				if(create_date < admin_date or admin_date == 0):
					admin_id = user["id"]
					admin_date = create_date
		#print admin_id
		if(len(admin_id) >= 5):
			team_url = Host+"/teams/"+team_id+"/members"
			add_team_data = {
							"team_id": team_id,
							"user_id": admin_id
							} 
			response3 = requests.post(team_url, data = json.dumps(add_team_data), headers = header)
			#print "r3", response3.status_code
			if(response3.status_code == 201):
				team_role_url = Host+"/teams/"+team_id+"/members/"+admin_id+"/roles"
				team_role_data = {
								  "roles": "team_user team_admin"
								}
				response4 = requests.put(team_role_url, data = json.dumps(team_role_data), headers = header)
				#print "r4", response4.status_code
				if(response4.status_code == 200):
					perm_url = Host +"/users/"+admin_id+"/roles"
					user_role_data = {
									  "roles": "system_user system_admin"
									}
					response5 = requests.put(perm_url, data = json.dumps(user_role_data), headers = header)
					#print "r5", response5.status_code
					if(response5.status_code == 200): return good
	return error

def isAdminAdded(token, team_id):
	url = Host+"/teams/"+team_id+"/members"
	header =  {'Authorization': 'Bearer ' + token, 
			'Accept': 'application/json'}
	response = requests.get(url, headers = header)
	if(response.status_code == 200):
		members = response.json()
		if(len(members)>1): return True
	return False

def addLatentUsers(token, team_id, plone_usernames):
	#pdb.set_trace()
	users_to_add = []
	user_url = Host+"/users"
	header =  {'Authorization': 'Bearer ' + token, 
				'Accept': 'application/json',
				'Content-Type': 'application/json'}
	response = requests.get(user_url, headers = header)
	if(response.status_code == 200):
		members = response.json()
		team_url = Host+"/teams/"+team_id+"/members"
		response2 = requests.get(team_url, headers = header)
		if(response2.status_code == 200):
			team_members = response2.json()
			team_members_id = [x["user_id"] for x in team_members]
			members_username = [x["username"] for x in members]
			for user in plone_usernames:
				if(user in members_username):
					user_id = members[members_username.index(user)]["id"]
					if(not(user_id in team_members_id)):
						users_to_add.append(user_id)
			for uid in users_to_add:
				team_url = Host+"/teams/"+team_id+"/members"
				add_team_data = {
								"team_id": team_id,
								"user_id": uid
								} 
				response3 = requests.post(team_url, data = json.dumps(add_team_data), headers = header)
			return good
	return error
	
#Use by plone to create channel when project is created and add users
def ploneCreateChannel(item, event):
	#pdb.set_trace()
	#check if admin was added and add admin to team
	ploneAddAdmin()
	#add any latent users
	ploneAddlatentUsers()
	#create the vhannel 
	token = authenticate(admin_username,getSAPassword())
	if token != error:
		team_id = getTeamID(token,getTeamName())
		name = str(item.title)
		name_id = str(item.id)
		description = str(item.description)
		createChannel(token,team_id, name_id, name, description)
		channel_id = getChannelID(token, team_id, name_id)
		addMembersToChannel(token, team_id,channel_id, item.members)

#use by plone to delete a channel when a project is deleted	
def ploneDeleteChannel(item, event):
	token = authenticate(admin_username,getSAPassword())
	if token != error:
		team_id =  getTeamID(token,getTeamName())
		#pdb.set_trace()
		name_id = str(item.id)
		channel_id = getChannelID(token, team_id, name_id)
		deleteChannel(token, channel_id)

def ploneModifyChannel(item, event):
	#pdb.set_trace()
	#add the latent users before applying modification
	ploneAddlatentUsers()
	#continue with the channel modification
	token = authenticate(admin_username,getSAPassword())
	if token != error:
		team_id =  getTeamID(token,getTeamName())
		name_id = str(item.id)
		channel_id = getChannelID(token, team_id, name_id)
		name = str(item.title)
		description = str(item.description)
		modifyChannel(token, channel_id, name, description)
		delMemberFromChannel(token, team_id,channel_id, item.members)
		addMembersToChannel(token, team_id,channel_id, item.members)

def ploneCreateTeam(portal):
	#pdb.set_trace()
	token = authenticate(admin_username,getSAPassword())
	if token != error:
		team_name = portal.getPhysicalPath()[1]
		createTeam(token, team_name)

def ploneDeleteTeam(portal):
	#pdb.set_trace()
	token = authenticate(admin_username,getSAPassword())
	if token != error:
		team_name = portal.getPhysicalPath()[1].lower().replace(" ","_")
		team_id = getTeamID(token, team_name)
		deleteTeam(token, team_id)

def ploneConfigMattermost():
	#pdb.set_trace()
	if(getSAPassword() ==  error):
		createSuperAdmin(admin_username, makePassword())
	token = authenticate(admin_username, getSAPassword())
	if token != error:
		setupConfiguration(token)

def ploneAddAdmin():
	#pdb.set_trace()
	token = authenticate(admin_username,getSAPassword())
	if token != error:
		team_id =  getTeamID(token,getTeamName())
		if(not isAdminAdded(token, team_id)):addAdminToTeam(token, team_id)

def ploneAddlatentUsers():
	token = authenticate(admin_username,getSAPassword())
	if token != error:
		team_id =  getTeamID(token,getTeamName())	
		users = api.user.get_users()
		users_usernames = [x.getUserName() for x in users]
		addLatentUsers(token, team_id, users_usernames)

def test(item = "", event = ""):
	#pdb.set_trace()
	ploneAddAdmin()
	ploneAddlatentUsers()

def test2(item = "", event = ""):
	#pdb.set_trace()


if __name__== "__main__":

	token = authenticate(admin_username,getSAPassword())
	team_id = getTeamID(token,"plone10")
	# print createChannel(token,team,"Test Project2")
	#print team_id
	# channel_id = getChannelID(token,team_id,"asshf")
	# print addMembersToChannel(token, team_id, channel_id,["user1","user2","user3"])
	# print delMemberFromChannel(token, team_id, channel_id,["user1"])
	#print deleteTeam(token, team_id)
	#print isAdminAdded(token, team_id)
	#if(not isAdminAdded(token, team_id)):print addAdminToTeam(token, team_id)
	#print addAdminToTeam(token, team_id)
	print addLatentUsers(token, team_id, ["user1", "user2"])