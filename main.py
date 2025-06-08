from instagrapi import Client
import configparser

# Login
cl = Client()
cl.login("jorge13.js", "c0id23;g")

# Listar últimas conversas
threads = cl.direct_threads(amount=5)
for i, thread in enumerate(threads):
    print(f"{i+1}. {thread.users[0].username}: {thread.messages[0].text}")

# Selecionar uma conversa e mandar mensagem
index = int(input("Selecione a conversa (número): ")) - 1
thread = threads[index]

msg = input("Digite a mensagem: ")
cl.direct_send(msg, [thread.users[0].pk])
print("Mensagem enviada.")
