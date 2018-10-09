#!/usr/bin/env python3


import socket

HOST = '127.0.0.1'
PORT = 62000
BUFFER_SIZE = 1024  # bytes


# uses TCP by default, uses binary encoding by default
class SimpleServer:

    @staticmethod
    def startup(file_name: str):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s, open('file_destination/' + file_name + '_copy', 'w+b') as file_copy:
                s.bind((HOST, PORT))
                s.listen(5)
                print('listening . . .')
                while True:
                    client, addr = s.accept()
                    with client:
                        print(f'Client connection from {addr}')
                        data = client.recv(BUFFER_SIZE)
                        if not data: break
                        file_copy.write(data)

        except Exception as err:  # oof ouch - # TODO should catch OSError-type exceptions instead
            print(f"server: start: error: {err}")
