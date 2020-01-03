'''
Name: UDPStats_server.py
Desc: Document Stats Server using UDP
Auth: Vasco Pinto
Date: 24/11/19
'''

import socket

SERVER_NAME = 'localhost'
SERVER_PORT = 5555

SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVER_SOCKET.bind((SERVER_NAME, SERVER_PORT))

print("Server is ready!")

while True:
    SERVER_SOCKET.listen()
    INCOMING_CONN, CLIENT_ADDR = SERVER_SOCKET.accept()
    DOCUMENT = INCOMING_CONN.recv(4096)

    DOCUMENT = DOCUMENT.decode()

    if DOCUMENT == 'exit':
        break

    elif isinstance(DOCUMENT, str) and DOCUMENT: #Checks if DOCUMENT is a not empty string

        print("File Received...\n")

        chars = 0
        words = 0

        lines = DOCUMENT.replace('\r', '').split('\n')

        for i in lines:

            if i.strip(): #If the string is not empty

                chars += len(i) #nr of chars
                words += len(i.strip().split(' ')) #nr of words

        stats = f"\nNr of Characters: {chars}\n"
        stats += f"Nr of Words: {words}\n\n"

        print("Sending Stats...\n")

        INCOMING_CONN.sendall(stats.encode())

    else:
        pass

SERVER_SOCKET.close()

