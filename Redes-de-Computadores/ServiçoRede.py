
# -*- coding: utf-8 -*-

import socket

class Cesar:
   
   def __init__(self):
    self.letras=' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
   '''Metodo que criptografa:
   chamando o metodo 'crip' e passando os atributos Texto_normal e chave, quando a chave nao for passada
   sera igual a 3, por default.'''
   def crip(self,texto_normal,chave=3):
      texto_cifrado= ' '
      texto_normal=texto_normal.upper()
      #Analisando se cada 'i' em 'texto_normal' está em self.letras. Se sim, pegamos a 'posição+chave' e add na string vazia texto_cifrado       
      for i in texto_normal:
         if i in self.letras:
            pos=self.letras.find(i)+chave                
            if pos >= 26:
               pos -= 26
            texto_cifrado += self.letras[pos]      
      return texto_cifrado

   #Metodo que descriptografa 
   def decrip(self, texto_cifrado, chave=-3):
      texto_normal=' '
      texto_cifrado=texto_cifrado.upper()
      
      for i in texto_cifrado:
         if i in self.letras:
            pos=self.letras.find(i)+chave
            texto_normal += self.letras[pos]
      return texto_normal[2:]

# Endereco IP do Servidor
HOST = ''
# Porta que o Servidor vai escutar
PORT = 5002
tcp1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig1 = (HOST, PORT)
tcp1.bind(orig1)
tcp1.listen(1)
while True:
    con1, cliente1 = tcp1.accept()
    print ('Concetado por ', cliente1)
    msg1 = con1.recv(1024)
    print ("Mensagem recebida do cliente: ", msg1)
    print ("Finalizando conexao com o cliente", cliente1)
    con1.close()
    break

#Cliente TCP
# Endereco IP do Servidor
SERVER2 = '127.0.1.1'
# Porta que o Servidor esta escutando
PORT2 = 7651
tcp1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest1 = (SERVER2, PORT2)
tcp1.connect(dest1)
#print("esta chegando aqui!!!")
texto=Cesar()
teste1=texto.crip(msg1)
print("Mensagem criptografada sendo enviada para o servidor: ", teste1)
tcp1.send(teste1)
tcp1.close()
