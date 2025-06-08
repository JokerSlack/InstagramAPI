import configParser

config = configparser.ConfigParser()
try:
	with open("config.ini", "r") as f:
		print("Arquivo de configuração encontrado!")
	config.read("config.ini")
except FileNotFoundError:
	print("Arquivo de configuração não encontrado!")

username = config["instagram"]["username"]
password = config["instagram"]["password"]
