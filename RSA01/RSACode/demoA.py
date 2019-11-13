#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 16:34
# @Author  : Renln
# @FileName: demoA.py
# @Description:

from Crypto.PublicKey import RSA

rsa = RSA.generate(2048) # 返回的是密钥对象

public_pem = rsa.publickey().exportKey('PEM') # 生成公钥字节流
private_pem = rsa.exportKey('PEM') # 生成私钥字节流

f = open('public.pem','wb')
f.write(public_pem) # 将字节流写入文件
f.close()
f = open('private.pem','wb')
f.write(private_pem) # 将字节流写入文件
f.close()


