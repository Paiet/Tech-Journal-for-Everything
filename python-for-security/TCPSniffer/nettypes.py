import socket 
from struct import unpack

from .utils import mac_addr

class EthernetFrame:
    length = 14
    def __init__(self, data):
        unpacked_data = unpack('!6s6sH', data[0:self.length])
        self.protocol = socket.ntohs(unpacked_data[2])
        self.destination = mac_addr(data[0:6])
        self.source = mac_addr(data[6:12])
        self.leftover_data = data[self.length:]

    def __str__(self):
        return """
            Source:             {source}
            Destination:        {destination}
            Protocol:           {protocol}
        """.format(**self.__dict__)


class IPHeader:
    length = 20
    def __init__(self, data):
        unpacked_data = unpack('!BBHHHBBH4s4s', data[0: self.length])
        self.version = data[0] >> 4
        self.header_length = (data[0] & 15) * 4
        self.ttl = unpacked_data[5]
        self.protocol = unpacked_data[6]
        self.source_addr = socket.inet_ntoa(unpacked_data[8])
        self.dest_addr = socket.inet_ntoa(unpacked_data[9])
        self.leftover_data = data[self.length:]

    def __str__(self):
        return """
            IP Header....
            - Source Address:            {source_addr}
            - Destination Address:       {dest_addr}
            - Protocol:                  {protocol}
        """.format(**self.__dict__)


class TCPSegment:
    length = 20
    def __init__(self, data):
        unpacked_data = unpack('!HHLLBBHHH', data[0:self.length])
        self.src_port = unpacked_data[0]
        self.dest_port = unpacked_data[1]
        self.sequence = unpacked_data[2]
        self.acknowledgement = unpacked_data[3]
        self.doffset_reserved = unpacked_data[4]
        self.header_length = self.doffset_reserved >> 4
        self.leftover_data = self._parse_http_data(data[self.length:])

    def __str__(self):
        return """
            TCPSegment:
             - Source Port:       {src_port}
             - Destination Port:  {dest_port}
             - Data:              {leftover_data}
        """.format(**self.__dict__)

    def _parse_http_data(self, data):
        try:
            return data.decode('utf-8')
        except Exception as e:
            return data

class UDPSegment:
    length = 8
    def __init__(self, data):
        unpacked_data = unpack('!HHHH', data[0:self.length])
        self.src_port = unpacked_data[0]
        self.dest_port = unpacked_data[1]
        self.length = unpacked_data[2]
        self.checksum = unpacked_data[3]
        self.leftover_data = data[self.length:]

    def __str__(self):
        return """
            UDPSegment:
             - Source Port:          {src_port}
             - Destination Port:     {dest_port}
             - Checksum:             {checksum}
             - Data:                 {leftover_data}
        """.format(**self.__dict__)













