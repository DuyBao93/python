import socket
import multiprocessing
import sys
import os
from _thread import *
import json
import numpy as np
import cv2

HOST_SERVER = '127.0.0.1'
PORT_SERVER = 12345

# HOST = '127.0.0.1'
# PORT = 13569
def conference():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH , 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

        

        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
def write_message(name, s, q, fileno):
    sys.stdin = os.fdopen(fileno)
    while True:
        input_message = input()
        dataIn = input_message.encode()
        data_dic = {
            'msg' : input_message,
            'name' : name 
        }
        data = str.encode(json.dumps(data_dic))
        s.sendall(data)

        if dataIn == b'exit':
            break
        q.put_nowait(dataIn)

def handle(name, s):
    while True:
        data = s.recv(1024)
        # data_array = data.decode().split()
        # print(data_array[3] + " : " + data_array[0])
        # dataDecode = (data_array[0] +
        #               " " +
        #               data_array[1] +
        #               " " +
        #               data_array[2])
        data_decode = data.decode()
        data_dict = json.loads(data_decode)
        if data_dict['name'] != name:
            print(data_dict['name'] + " : " + data_dict['msg'])
        #portName = str(s.getsockname()[1])
        if (data_dict['msg'])== "exit":
            print(data_dict['name'] +" close connect")
            break

def init_process(name):
    q = multiprocessing.Queue()
    fn = sys.stdin.fileno()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST_SERVER, PORT_SERVER))
        process_video_conference = multiprocessing.Process(target=conference, args=())
        process_write_message = multiprocessing.Process(target=write_message, args=(name, s, q, fn))
        process_handle = multiprocessing.Process(target=handle, args=(name, s, ))

        print("connected ...........")
        print("You can talk anything")
        process_video_conference.start()
        process_write_message.start()
        process_handle.start()

        process_video_conference.join()
        process_write_message.join()
        process_handle.join()
        print("close connect")

if __name__ == "__main__":
    Name = sys.argv[1]
    init_process(Name)

    
