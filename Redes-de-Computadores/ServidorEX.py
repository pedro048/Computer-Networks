# -*- coding: utf-8 -*-

import socket

serverPort = 12000			   ''' número de porta do servidor '''	  
serverSocket = socket(AF_INET,SOCK_STREAM) ''' cria o socket do servidor, denominado serverSocket. 
					       AF_INET = rede usando IPv4, SOCK_STREAM = socket TCP '''
serverSocket.bind(('',serverPort))         ''' associamos o número de porta do servidor, serverPort , ao socket.
					       serverSocket será o socket de entrada. Depois de estabelecer essa porta de entra-
					       da, o servidor fica escutando até que algum cliente bata'''
serverSocket.listen(1)			   ''' o servidor escuta as requisições de conexão TCP do cliente. O parâmetro especifica
					       o número máximo de conexões em fila (pelo menos 1) '''
print ‘The server is ready to receive’     ''' indica que o servidor esta pronto para receber requisicoes '''

while 1:

	connectionSocket, addr = serverSocket.accept() ''' Quando o cliente bate na porta do servidor, o programa chama o método 
							   accept() para serverSocket, que cria um novo socket no servidor, chamado 
							   connectionSocket (dedicado a esse cliente específico).
	
							   Eh criada uma conexão TCP entre o clientSocket do cliente e o connection-
							   Socket do servidor e bytes são trocados entre eles. (bytes não são perdidodos 
							   e chegam em ordem).'''
	sentence = connectionSocket.recv(1024)	       ''' os caracteres chegam do cliente são colocados na cadeia sentence '''
	capitalizedSentence = sentence.upper()	       ''' os caracteres da cadeia sentence são transformados em maiúsculo e 
							   colocados em capitalizedSentence'''
	connectionSocket.send(capitalizedSentence)     ''' envia capitalizedSentence para o cliente '''
	connectionSocket.close()		       ''' depois de enviar a sentença modificada ao cliente, o socket da conexão he fechado. Mas,
							   o serverSocket permanece aberto, ou seja, outro cliente pode bater à porta do servidor e 
							   enviar uma nova sentença para ser modificada.
						       '''
