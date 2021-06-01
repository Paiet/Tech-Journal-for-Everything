

def mac_addr(bytestring):
    return ':'.join('{:02x}'.format(piece) for piece in bytestring).upper()
