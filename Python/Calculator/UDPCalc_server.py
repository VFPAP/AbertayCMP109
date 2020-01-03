'''
Name: UDPCalc_server.py
Desc: Calculator Server using UDP
Auth: Vasco Pinto
Date: 22/11/19
'''

import socket

SERVER_NAME = 'localhost'
SERVER_PORT = 5555

SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

SERVER_SOCKET.bind((SERVER_NAME, SERVER_PORT))
print("Server is ready!")

def parseDigits(nums): #Function to check if digits are valid and to handle floats

    if len(nums) == 2: #Only valid if there are two digits

        if nums[0].isdigit() and nums[1].isdigit():
            return [int(nums[0]), int(nums[1])]

        elif '.' in nums[0] and nums[0].replace('.','',1).isdigit():
            if '.' in nums[1] and nums[1].replace('.','',1).isdigit():
                return [float(nums[0]), float(nums[1])]

            elif nums[1].isdigit():
                return [float(nums[0]), int(nums[1])]

            else:
                return nums.clear()

        elif '.' in nums[1] and nums[1].replace('.','',1).isdigit():
            if nums[0].isdigit():
                return [int(nums[0]), float(nums[1])]
            else:
                return nums.clear()

        else:
            return nums.clear()

    else:
        return nums.clear()

while True:

    OPERATION, CLIENT_ADDR = SERVER_SOCKET.recvfrom(2048)

    OPERATION = OPERATION.decode().replace(' ', '') #Get rid of whitespaces


    if 'exit' in OPERATION:
        SERVER_SOCKET.sendto(OPERATION.encode(), CLIENT_ADDR)
        break

    elif '+' in OPERATION:
        op = OPERATION.split('+')
        op = parseDigits(op)

        if op: #If parseDigits() didn't return empty list
            RESULT = op[0] + op[1]
        else:
            err = "Invalid Operation!"
            print(err)
            SERVER_SOCKET.sendto(str(err).encode(), CLIENT_ADDR)
            continue

    elif '-' in OPERATION:
        op = OPERATION.split('-')
        op = parseDigits(op)

        if op: #If parseDigits() didn't return empty list
            RESULT = op[0] - op[1]
        else:
            err = "Invalid Operation!"
            print(err)
            SERVER_SOCKET.sendto(str(err).encode(), CLIENT_ADDR)
            continue

    elif '*' in OPERATION:
        op = OPERATION.split('*')
        op = parseDigits(op)

        if op: #If parseDigits() didn't return empty list
            RESULT = op[0] * op[1]
        else:
            err = "Invalid Operation!"
            print(err)
            SERVER_SOCKET.sendto(str(err).encode(), CLIENT_ADDR)
            continue

    elif '/' in OPERATION:
        op = OPERATION.split('/')
        op = parseDigits(op)

        if op: #If parseDigits() didn't return empty list
            if op[1] == 0:
                err = "Can't divide by 0!"
                print(err)
                SERVER_SOCKET.sendto(str(err).encode(), CLIENT_ADDR)
                continue
            else:
                RESULT = op[0] / op[1]

        else:
            err = "Invalid Operation!"
            print(err)
            SERVER_SOCKET.sendto(str(err).encode(), CLIENT_ADDR)
            continue

    else:
        err = "Invalid Operation!"
        print(err)
        SERVER_SOCKET.sendto(str(err).encode(), CLIENT_ADDR)
        continue

    print(f"{OPERATION} = {RESULT}")
    SERVER_SOCKET.sendto(str(RESULT).encode(), CLIENT_ADDR)

SERVER_SOCKET.close()
