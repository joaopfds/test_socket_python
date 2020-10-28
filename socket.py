import socket
import re
import os
def vp1(url):
    so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        so.connect((url, 80))
    except:
        print("not Conected\n")
        os.system("pause")
    else:
        print("Connected successful\n")
    so.send(b'GET / HTTP/1.0\n\n')
    resposta = so.recv(1024)
    print("Resposta:\n{}".format(str(resposta, "UTF-8")))
    resposta = format(str(resposta, "UTF-8"))
    resposta = resposta.split()
    i = 0
    print("\n")
    print("HTTP VERSION: " + resposta[i])
    for i in range(0, len(resposta), 1):
        if resposta[i] == "100":
            print("Status code: " + resposta[i] + " Continue"
            + " (até o momento tudo está OK e que o cliente pode)"
            + " (continuar com a requisição ou ignorar caso já tenha terminado.)")
        if resposta[i] == "200":
            print("Status code: " + resposta[i] + " OK"
            + " (Esta requisição foi bem sucedida.)")
        if resposta[i] == "300":
            print("Status code: " + resposta[i] + " Multiple Choices "
            + " (A requisição tem mais de uma resposta possível. User-agent ou o user deve escolher uma delas.)")
        if resposta[i] == "400":
            print("Status code: " + resposta[i] + " Bad Request"
            + " (o servidor não entendeu a requisição pois está com uma sintaxe inválida.)")
        if resposta[i] == "404":
            print("Status code: " + resposta[i] + " Not Found"
            + " (O servidor não pode encontrar o recurso solicitado.)")
        if resposta[i] == "500":
            print("Status code: " + resposta[i] + " Internal Server Error "
            + " (O servidor encontrou uma situação com a qual não sabe lidar.)")
        if resposta[i] == "Content-Length:":
            print(resposta[i] +" "+ resposta[i+1])
        if resposta[i] == "Content-Type:":
            print(resposta[i] + " " + resposta[i+1])
    print("Fechando conexão...")
    so.close()

def vp1graduacao(url):
    so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        so.connect((url, 80))
    except:
        print("not Conected\n")
        os.system("pause")
    else:
        print("Connected successful\n")
    so.send(b'GET /graduacao/sistemas-de-informacao HTTP/1.0\n\n')
    resposta = so.recv(1024)
    print("Resposta:\n{}".format(str(resposta, "UTF-8")))
    resposta = format(str(resposta, "UTF-8"))
    resposta = resposta.split()
    i = 0
    print("\n")
    print("HTTP VERSION: " + resposta[i])
    for i in range(0, len(resposta), 1):
        if resposta[i] == "100":
            print("Status code: " + resposta[i] + " Continue"
            + " (até o momento tudo está OK e que o cliente pode)"
            + " (continuar com a requisição ou ignorar caso já tenha terminado.)")
        if resposta[i] == "200":
            print("Status code: " + resposta[i] + " OK"
            + " (Esta requisição foi bem sucedida.)")
        if resposta[i] == "300":
            print("Status code: " + resposta[i] + " Multiple Choices "
            + " (A requisição tem mais de uma resposta possível. User-agent ou o user deve escolher uma delas.)")
        if resposta[i] == "400":
            print("Status code: " + resposta[i] + " Bad Request"
            + " (o servidor não entendeu a requisição pois está com uma sintaxe inválida.)")
        if resposta[i] == "404":
            print("Status code: " + resposta[i] + " Not Found"
            + " (O servidor não pode encontrar o recurso solicitado.)")
        if resposta[i] == "500":
            print("Status code: " + resposta[i] + " Internal Server Error "
            + " (O servidor encontrou uma situação com a qual não sabe lidar.)")
        if resposta[i] == "Content-Length:":
            print(resposta[i] +" "+ resposta[i+1])
        if resposta[i] == "Content-Type:":
            print(resposta[i] + " " + resposta[i+1])
    print("Fechando conexão...")
    so.close()

if __name__ == "__main__":
    url = input("Insira o endereco :\n")
    print("\n")
    cont = 0
    while cont != 1:
        escolha = input("1-Para requisicao / \n2-Para requisicao /graduacao/sistemas-de-informacao/ \n3-sair\n")
        if escolha=="1":
            vp1(url)
        if escolha=="2":
            vp1graduacao(url)
        if escolha=="3":
            cont=1
    os.system("pause")