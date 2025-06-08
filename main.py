from instagrapi import Client
from config import Config
import api
import os

# Config
cfg = Config()
cfg.config()

# Login
client = Client()
session_file = f"{username}_session.json"

# Criação de sessão
if os.path.exists(session_file):
    client.load_settings(session_file)
    try:
        client.login(username, password)
    except Exception:
        print("⚠️ Sessão antiga inválida. Logando do zero...")
        client.set_settings({})
        client.login(cfg.username, cfg.password)
        client.dump_settings(session_file)
else:
    client.login(cfg.username, cfg.password)
    client.dump_settings(session_file)
print("✅ Login feito com sucesso!")

# Selecione o que quer fazer

while True:
    threads = client.direct_threads()
    for thread in threads:
        if thread.unseen_count > 0:
            user = thread.users[0].username
            print(f"Nova mensagem de {user}")
    print("""
        1 - Conversar
        2 - Pesquisar
    """)
    menu = int(input("Selecione o que quer fazer:"))
    if menu == 1:
        threads = client.direct_threads(amount=5) # Mostrar conversas
        for i, thread in enumerate(threads):
            print(f"{i+1}. {thread.users[0].username}: {thread.messages[0].text}")
        index = int(input("Selecione a conversa (número): ")) - 1
        thread = threads[index]
        messages = client.direct_messages(thread, amount=20) # Mensagens da conversa escolhida
        print(f"\n🗨️ Histórico de conversa com @:\n")
        for msg in reversed(messages):
            author = client.user_info(msg.user_id).username
            print(f"{author}: {msg.text}")

#msg = input("Digite a mensagem: ")
#client.direct_send(msg, [thread.users[0].pk])
#print("Mensagem enviada.")
