import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('0.0.0.0', 12345)
sock.bind(addr)



while True:
    client = sock.recvfrom(1518)
    
    message_bytes = client[0]
    client_addr = client[1]

    print('Message: ' + message_bytes.decode('utf-8'))
    print('From: ' * client_addr[0] + ':' + str(client_addr[1]))
    
sock.close()
