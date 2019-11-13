#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 16:39
# @Author  : Renln
# @FileName: generateKey.py
# @Description: 产生密钥对
import os
from Crypto.PublicKey import RSA
# RSA填充方式  ---PKSCS1_v1_5  -----PKDCD1_OAEP
'''获取当前文件路径'''
path = os .getcwd()
'''生成公钥私钥文件'''
def genKeys(name):
    rsa = RSA.generate(1024)
    public_pem = rsa.publickey().export_key('PEM')
    private_pem = rsa.export_key('PEM')
    tem_file  = open(path+'/pem/public%s.pem' %name,'wb')
    tem_file.write(public_pem)
    tem_file = open(path+'/pem/private%s.pem' %name ,'wb')
    tem_file.write(private_pem)
    tem_file.close()






