#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 15:32
# @Author  : Renln
# @FileName: generateRSA.py

from Crypto.PublicKey import RSA
# RSA填充方式  ---PKSCS1_v1_5  -----PKDCD1_OAEP
from Crypto.Cipher import PKCS1_v1_5
import  base64
'''生成公钥私钥文件'''
class RSADemo:
    @staticmethod
    def generatePub():
        rsa = RSA.generate(2048)
        public_pem = rsa.publickey().export_key('PEM')
        private_pem = rsa.export_key('PEM')
        tem_file  = open('publicB.pem','wb')
        tem_file.write(public_pem)
        tem_file = open('privateB.pem','wb')
        tem_file.write(private_pem)
        tem_file.close()

    # 读取公私钥文件
    def rsa_encrypt(pubKey,message):
        with open(pubKey, 'rb') as f:
            data = f.read()
        key = RSA.importKey(data)
        rsa = PKCS1_v1_5.new(key)
        length = len(data)
        default_length = 110
        res = []
        for i in range(0, length, default_length):
            res.append(rsa.encrypt(data[i:i + default_length]))
        byte_data = b''.join(res)
        # print(type(res))
        return base64.b64encode(byte_data)

    def rsa_decrypt(priKey,msg):
        # msg = base64.b64decode(msg)
        with open(priKey, 'rb') as f:
            data = f.read()
            key = RSA.importKey(data)
            rsa = PKCS1_v1_5.new(key)
            plain = rsa.decrypt(base64.b64decode(msg), 'ERROR')  # 'ERROR'必需
            return plain

    # def private_long_decrypt(data, sentinel=b'decrypt error'):
    #     data = base64.b64decode(data)
    #     length = len(data)
    #     default_length = 128
    #     res = []
    #     for i in range(0, length, default_length):
    #         res.append(rsa.decrypt(data[i:i + default_length], sentinel))
    #     return str(b''.join(res), encoding="utf-8")



