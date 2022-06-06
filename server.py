import socket
import os
import pickle
import select
import multiprocessing

entradas = []
conexoes = {}
usuarios = {}

def atende_requisicao(clisock):
    comando = ""
    while comando == "":
        comando = pickle.loads(clisock.recv(1024))
    if comando ==  "login":
        usuarios[clisock] = conexoes[clisock]
        msg = "login bem sucedido"
    if comando == "logoff":
        try:
            del usuarios[clisock]
            msg = "logoff sucedido" 
        except:
            msg = "usuario não logado"
    if comando == "lista":
        msg = usuarios
    clisock.send(pickle.dumps(msg))
    clisock.close
    del conexoes[clisock]


HOST = " "
PORTA = 5000
clientes = []
sock = socket.socket()
sock.bind((HOST, PORTA))
sock.listen(50)
sock.setblocking(False)
entradas.append(sock)

while True:
    leitura, escrita, excecao = select.select(entradas,[],[])
    for cliente in leitura:
        if pronto == sock:
            clisock, endr = sock.accept()
            conexoes[clisock] = endr
            tarefa = multiprocessing.Process(target = atende_requisicao,args =(clisock))
            tarefa.start
