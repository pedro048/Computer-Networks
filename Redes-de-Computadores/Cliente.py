#Cliente TCP
import socket
# Endereco IP do Servidor
SERVER = '127.0.0.1'
# Porta que o Servidor esta escutando
PORT = 5002
tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp.connect((SERVER, PORT))
msg = raw_input("Input lowercase sentence:")
tcp.send(msg)
modifiedSentence = tcp.recv(1024)
print("From Server:", modifiedSentence) 
tcp.close()
