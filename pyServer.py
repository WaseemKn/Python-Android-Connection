# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 20:40:15 2018

@author: Waseem Kntar
@title: pyServer
"""
import socket
#import threading

host, port = "192.168.1.6", 1234
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def recv(): 
    try:
        client.bind((host, port))
    finally:
        pass
    client.listen(10) # how many connections can it receive at one time
    print "Start Listening..."
    
    while True:
        conn, addr = client.accept()
        print "client with address: ", addr, " is connected."
        data = conn.recv(1024)
        print "Recieved this data: <", data, "> from the client."
        
        if data == "Correct":
            reply = "Success"
            conn.send(reply.encode("utf-8"))
            conn.close()
            print "-----------------------------"
        elif data == "Disconnect":
            reply = "Disconnected and the listen has Stopped"
            conn.send(reply.encode("utf-8"))
            conn.close()
            break
        else:
            reply = "Failed"
            conn.send(reply.encode("utf-8"))
            conn.close()
            print "-----------------------------"
            
    client.close()
"""
You can use thread for the recieve operation so that the execution in main thread
isn't wait until complete the recieve operation. 
"""
#thread = threading.Thread(target = recvFromAndroid, args = ())
#thread.start()
recv()
#print "completed"

