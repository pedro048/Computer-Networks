# -*- coding: utf-8 -*-
import socket

serverName = 'servername’
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM) ''' cria o socket do cliente, denominado clientSocket. 
						AF_INET = rede usando IPv4, SOCK_STREAM = socket TCP 
	
						O sistema operacional define o número de porta do
						socket cliente 
					    '''

clientSocket.connect((serverName,serverPort)) ''' Estabelecendo uma conexão TCP entre o cliente e o 
					          servidor (apresentação de três vias)
					      '''
sentence = raw_input(‘Input lowercase sentence:’) ''' obtém uma sentença do usuário '''
clientSocket.send(sentence)			  ''' envia a cadeia sentence pelo socket do cliente para a conexão TCP	'''		  
modifiedSentence = clientSocket.recv(1024) ''' os caracteres chegam do servidor são colocados na cadeia modifiedSentence '''
print ‘From Server:’, modifiedSentence     ''' exibe a mensagem que chegou do servidor ''' 
clientSocket.close()			   ''' fecha o socket e, portanto, fecha a conexão TCP entre cliente e servidor '''
