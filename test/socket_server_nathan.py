# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a tempor
"""
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket() as listensocket:
    listensocket.bind((HOST, PORT))
    listensocket.listen()
    conn, addr = listensocket.accept()
    with conn:
        print("Connected by ", addr)
        while True:
            data = conn.recv(1024)
            print(data)