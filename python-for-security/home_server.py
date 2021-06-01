import socket

from TCPSniffer.nettypes import EthernetFrame
from TCPSniffer.capture import PCAPFile


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 8080))
    server.listen(1)
    conn, addr = server.accept()
    pcap = PCAPFile('remote.pcap')
    with conn:
        while True:
            data = conn.recv(1024)
            if data:
                pcap.write(data)
    pcap.close()



if __name__ == '__main__':
    main()
