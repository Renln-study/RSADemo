#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 16:56
# @Author  : Renln
# @FileName: ProcessRsa.py
# @Description: 加密解密验证签名过程

from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5

from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import base64

class PRsa:

    def __init__(self, pub_key, pri_key):
        self.pri_key_obj = None
        self.pub_key_obj = None
        self.verifier = None
        self.signer = None
        if pub_key:
            pub_key = RSA.importKey(pub_key)
            self.pub_key_obj = Cipher_pkcs1_v1_5.new(pub_key)
            self.verifier = PKCS1_v1_5.new(pub_key)
        if pri_key:
            pri_key = RSA.importKey(pri_key)
            self.pri_key_obj = Cipher_pkcs1_v1_5.new(pri_key)
            self.signer = PKCS1_v1_5.new(pri_key)

    def public_long_encrypt(self, data, charset='utf-8'):
        length = len(data)
        default_length = 117
        res = []
        for i in range(0, length, default_length):
            res.append(self.pub_key_obj.encrypt(data[i:i + default_length]))
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

    def sign(self, data):
        h = SHA256.new(data)
        signature = self.signer.sign(h)
        return base64.b64encode(signature)

    def verify(self, data, sign,  charset='utf-8'):
        h = SHA256.new(data.encode(charset))
        return self.verifier.verify(h, base64.b64decode(sign))

