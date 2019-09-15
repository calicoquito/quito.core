import cryptography
from cryptography.fernet import Fernet
import random, string

def getPass():
	key = Fernet.generate_key()
	code  = makePassword(30)
	f = Fernet(key)
	encrypted = f.encrypt(code)
	return ""+key+"=LKsD0dgGHasfdfas23-dsa"+encrypted

def makePassword(stringLength=20):
    """Generate a random string of letters, digits and special characters """
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))


if __name__== "__main__":
	file = open("mattermost_cred.env", "w+")
	code = getPass()
	set_code = "SACRED="+code
	file.write(set_code)
	file.close()
	print code