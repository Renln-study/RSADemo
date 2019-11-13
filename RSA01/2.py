#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 18:42
# @Author  : Renln
# @FileName: 2.py
# @Description: 模拟图片传递，图片--base64 ---加解密 --- 数字签名 ----验证签名


from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5

from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import base64


class RsaUtil:

    def __init__(self, pub_key, pri_key):
        self.pri_key_obj = None
        self.pub_key_obj = None
        self.verifier = None
        self.signer = None
        if pub_key:
            pub_key = RSA.importKey(base64.b64decode(pub_key))
            self.pub_key_obj = Cipher_pkcs1_v1_5.new(pub_key)
            self.verifier = PKCS1_v1_5.new(pub_key)
        if pri_key:
            pri_key = RSA.importKey(base64.b64decode(pri_key))
            self.pri_key_obj = Cipher_pkcs1_v1_5.new(pri_key)
            self.signer = PKCS1_v1_5.new(pri_key)

    def public_long_encrypt(self, data, charset='utf-8'):
        length = len(data)
        print(length)
        default_length = 117
        res = []
        for i in range(0, length, default_length):
            res.append(self.pub_key_obj.encrypt(data[i:i + default_length]))
        print(res)
        byte_data = b''.join(res)
        return base64.b64encode(byte_data)

    def private_long_decrypt(self, data, sentinel=b'decrypt error'):
        data = base64.b64decode(data)
        length = len(data)
        default_length = 128
        res = []
        for i in range(0, length, default_length):
            res.append(self.pri_key_obj.decrypt(data[i:i + default_length], sentinel))
        return str(b''.join(res), encoding = "utf-8")

    def sign(self, data, charset='utf-8'):
        h = SHA256.new(data)
        signature = self.signer.sign(h)
        return base64.b64encode(signature)

    def verify(self, data, sign,  charset='utf-8'):
        h = SHA256.new(data.encode(charset))
        return self.verifier.verify(h, base64.b64decode(sign))


pub_key = '''
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCQFA4YVQZatJAyO7TsuzkWE8dz
17qi8GuOCnegKbKd6alLXkDzKhVG3kd3GijouHtlqsm2zFCK7K+I5MUu8Fuk23OE
wIVZn9StltjLzJ1hB1AZC1/NCoCFZG5T2+AaQolrw8LvPS5jH2TuYQf7oLDHR88B
KJgV/tZlr22Jicqm0wIDAQAB
'''
pri_key = '''
MIICWwIBAAKBgQCQFA4YVQZatJAyO7TsuzkWE8dz17qi8GuOCnegKbKd6alLXkDz
KhVG3kd3GijouHtlqsm2zFCK7K+I5MUu8Fuk23OEwIVZn9StltjLzJ1hB1AZC1/N
CoCFZG5T2+AaQolrw8LvPS5jH2TuYQf7oLDHR88BKJgV/tZlr22Jicqm0wIDAQAB
AoGAMP6A5IlVRdcNCef/2Fi6SuWi96OuleYHzR+GGnLTiJuCtFxy3b27yoOf7cJ5
ktnZLHNtcLn90aA2+OhCnXmiz+M9PNArzfvtDoAKMlM9UEpBjGW/QYPkcHgnKOs9
utAr4OnPB9PFdvCuwya4P8AL/7kpjSW+4zQpUT459BlJFxECQQDYUnQQgyR3CZiG
Pj9vPfmmFmogpZpJTG9zAuOjOCxa5BQvV4iKhk6pkQAaVsjc7WMobEIhLqXn/I8E
ldsqIPj1AkEAqoFZULpjke8CQm0rmr2UdbhU74KKYzeS2KKKc/2TdQUzTqvBdY2+
VCyc0Ok6BWctBHfsu4FR6YpDYsg3QwvjpwJAEHeuaDdjhkBPwSBp+dDw+UjJiXSx
2xSbg1jb9WfoUH7+XmA+f7UbteLY7ChhIBheLQyYuCfx70gVpxa1WW6rJQJAEahR
mpWi6CMLZduub1kAvew4B5HKSRohQAQdOIPjOHQwaw5Ie6cRNeBk4RG2K4cS12qf
/o8W74udDObVKkFZ8wJAPL8bRWv0IWTlvwM14mKxcVf1qCuhkT8GgrG/YP/8fcW8
SiT+DifcA7BVOgQjgbTchSfaA+YNe7A9qiVmA+G4GQ==
'''
print(len(pub_key))
with open('Code.jpg','rb') as f :
     img = base64.b64encode(f.read())
data = img
rsa_util = RsaUtil(pub_key, pri_key)
print(f'原文: {data}')

encrypt = rsa_util.public_long_encrypt(data)
print(f'加密: {encrypt}')
decrypt_str = rsa_util.private_long_decrypt(encrypt)
print(f'解密: {decrypt_str}')
img_de =decrypt_str.encode('utf-8')
# print(img_de)
with open('deCode.jpg','wb') as f:
    f.write(base64.b64decode(img_de))


sign = rsa_util.sign(data)
print(f'sign: {sign}')

verify = rsa_util.verify(decrypt_str, sign)
print(f'verify: {verify}')

