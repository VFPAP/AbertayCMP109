'''
Name: UDPCalc_client.py
Desc: Calculator Client using UDP
Auth: Vasco Pinto
Date: 22/11/19
'''

import socket

SERVER_NAME = 'localhost'
SERVER_PORT = 5555

while True:

    CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    OPERATION = input("\n\nType your simple operation (one operator only) or 'exit' to exit: ")

    if any(elem in OPERATION for elem in {'+', '-', '*', '/', 'exit'}): #Check if any operator or 'exit' is present in the input

        CLIENT_SOCKET.sendto(OPERATION.encode(), (SERVER_NAME, SERVER_PORT))
        RESULT, SERVER_ADDR = CLIENT_SOCKET.recvfrom(2048)

        print(RESULT.decode())

        if 'exit' in RESULT.decode():
            CLIENT_SOCKET.close()
            break

    else: #In case none of the operators or 'exit' is in the input, throw error
        print("Invalid Operation!")

    CLIENT_SOCKET.close()
