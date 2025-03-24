from listar_usuario import ext_id_usr
from envio_notificaçao import enviar_notificaçao


while True:

    titulo = input("Insira o título da sua notificação: ")
    if not titulo.strip():
        print("O título é obrigatório")
        continue  

    descricao = input("Insira uma descrição para sua notificação: ")
    if not descricao.strip():
        print("A descrição é obrigatória")
        continue

    link = input("Insira um link para a notificação (ou aperte Enter para continuar): ")

    while True:
        nome_usuario = input("Insira o nome do usuário que deseja buscar: ")
        id_usuario = ext_id_usr(nome_usuario)
        print(id_usuario)
        print("Enviando notificação...")
        enviar_notificaçao(titulo, descricao, id_usuario, link=link if link else None)
    

        nova_notificacao = input("Deseja criar outra notificação? (S/N): ").strip().upper()
        if nova_notificacao == "N":
            print("Programa encerrado.")
            break  
    break

