#!/usr/bin/env python3

import socket

# accept transmitted file data and save it
def receive_file(save_path):
    # set up the server to listen on localhost and port 
    HOST, PORT = 'localhost', #port #????
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)  # listen for a single connection
        print(f'Server listening on {HOST}:{PORT}')
        
        conn, addr = s.accept()
        with conn:
            print(f'Connected by {addr}')
            with open(save_path, 'wb') as f:  # write in binary mode
                while True:
                    data = conn.recv(1024)  # receive data in chunks
                    if not data:
                        break  # exit loop if no more data is received
                    f.write(data)  # write received data to file
            print(f'File saved as {save_path}.')

# path to save the received file
output_file_path = 'received_data.txt'

# call the function to receive the file and save it
receive_file(output_file_path)