'''
Name: UDPStats_client.py
Desc: Document Stats Client using UDP
Auth: Vasco Pinto
Date: 24/11/19
'''

import socket

SERVER_NAME = 'localhost'
SERVER_PORT = 5555

while True:

    CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    CLIENT_SOCKET.connect((SERVER_NAME, SERVER_PORT))

    FILE = input("\nEnter filename or 'exit' to exit: ")

    if FILE.endswith('.txt'):

        try:
            with open(FILE,'rb') as DOCUMENT: #Open file as binary to be ready to be sent

                data = DOCUMENT.read()

                print("\nSending File...")
                CLIENT_SOCKET.sendall(data)
        except:
            print("Error Opening File...\n")
            CLIENT_SOCKET.close()
            continue

        stats, SERVER_ADDR = CLIENT_SOCKET.recvfrom(4096)

        if stats:
            print(stats.decode())

        else:
            print("Error analysing the file...")


    elif FILE == 'exit':
        CLIENT_SOCKET.sendall(FILE.encode())
        CLIENT_SOCKET.close()
        break

    else:
        print("Invalid Input!")


    CLIENT_SOCKET.close()

