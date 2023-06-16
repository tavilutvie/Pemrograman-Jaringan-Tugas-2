import sys
import socket
import logging

def kirim_data(name=""):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning(f"membuka socket {name}")

    server_address = ('localhost', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        message = 'TIME\r\n'
        logging.warning(f"[CLIENT] sending {message}")
        sock.sendall(message.encode('utf-8'))
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(1024).decode('utf-8')
            amount_received += len(data)
            logging.warning(f"[DITERIMA DARI SERVER] {data}")
    finally:
        logging.warning("closing")
        sock.close()
    return

if __name__=='__main__':
    for i in range(1,20):
        kirim_data(i)