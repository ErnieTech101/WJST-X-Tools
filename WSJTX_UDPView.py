import socket
import struct

MULTICAST_GROUP = '224.0.0.1'
PORT = 2237

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', PORT))

# Join multicast group
mreq = struct.pack('4sL', socket.inet_aton(MULTICAST_GROUP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

try:
    while True:
        data, address = sock.recvfrom(2048)
        print(f"{data.hex()}")
        print(" " * 70)
        
except KeyboardInterrupt:
    print("\n\nStop")
    sock.close()
