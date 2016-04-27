import argparse, socket, sys
from struct import *

MAX_BYTES = 65535
Src = "192.168.1.1"
Dest = "255.255.255.255"
clientPort = 67
serverPort = 68

#Convert a string of 6 characters of ethernet address into a dash separated hex string
def eth_addr (a) :
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
    return b




if __name__ == '__main__':
    address = ('', clientPort)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    while True:
        data, address= s.recvfrom(MAX_BYTES)
        print("received:", data, "from", addr)
