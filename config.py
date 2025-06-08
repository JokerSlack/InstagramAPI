import configparser
import os

# Classe que fará esta lib funcionar
class Config:
    def __init__(self, configFileName="config.ini", username="default", password="default") -> object:
        self.configFileName = configFileName
        self.username = username
        self.password = password

    def config(self):
        if os.path.exists("./" + self.configFileName):
            print("Arquivo de configuração encontrado!")
        else:
            if input("Você quer criar um arquivo de configuração[Y/n]: ").upper() == "Y":
                print("Inicializando criação de arquivo...")
                username = input("Username: ")
                password = input("Password: ")
                config = configparser.ConfigParser()
                config["instagram"] = {'username': username, 'password': password}
                with open('config.ini', 'a') as f:
                    config.write(f)
                print("Arquivo de configuração criado!")
            else:
                raise FileNotFoundError("Arquivo de configuração não foi encontrado!")

        parser = configparser.ConfigParser()
        parser.read(self.configFileName)
        self.username = parser["instagram"]["username"]
        self.password = parser["instagram"]["password"]
        print("Configuração concluída!")
