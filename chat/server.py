import socket
import json
from _thread import *
import os

HOST = '127.0.0.1'
PORT = 12345
ThreadCount = 0
ThreadList = []
# ThreadState = "initial"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((HOST, PORT))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
s.listen(5)

def multi_threaded_client(conn, addr):
    listOfGlobals = globals()
    global ThreadCount
    global ThreadList
    # global ThreadState
    print(ThreadList)
    while True:
        data = conn.recv(1024)
        
        for x in ThreadList:
            if addr == ():
                x.sendall(data)
            else:
                data_address = str(addr[1])
                print( data_address)
                data_decode = data.decode()
                print(type(data_decode))
                data_dict = json.loads(data_decode)
                data_dict['add'] = data_address
                print (data_dict)
                data_end = str.encode(json.dumps(data_dict))
                print (data_end)
                x.sendall(data_end)

        if data == b'exit':
            listOfGlobals['ThreadCount'] -= 1
            ThreadList.remove(conn)
            if ThreadCount == 0:
                # listOfGlobals['ThreadState'] = "null"
                print("close connect")
                listOfGlobals['ThreadList'] = []
                break
            conn.close()

while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    ThreadList.append(conn)
    ThreadCount += 1
    start_new_thread(multi_threaded_client, (conn, addr))
    # multi_threaded_client(conn, addr)


    