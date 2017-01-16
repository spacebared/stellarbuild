import ed25519 as src
import crc16
import binascii
import os
import struct
import base64

def process(v, data):
    dat=v+data
    chksum = struct.pack('H',crc16.crc16xmodem(dat))
    ans=base64.b32encode(dat+chksum).decode()
    return ans
def make_key_pair():
    init=32
    seed=os.urandom(init)
    signkey=src.SigningKey(seed)
    verifykey=signkey.get_verifying_key()
    one=binascii.a2b_hex('30')
    two=binascii.a2b_hex('90')
    datapk=signkey.to_seed()
    data=verifykey.to_bytes()
    public=process(one,data)
    private=process(two,datapk)
    return (public, private)


if __name__=="__main__":
    pubkey,pk=make_key_pair()
    print(pubkey,pk)
