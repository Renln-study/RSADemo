#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 16:49
# @Author  : Renln
# @FileName: SignDemo.py
# @Description: 模拟签名主过程

import  base64
import  generateKey
import ProcessRsa
import os

path = os .getcwd()

"""读取图片"""
def readIMg():
    file = 'Code.jpg'
    with open(file,'rb') as f :
        imageBase64 = base64.b64encode(f.read())
    return imageBase64

"""明文加密，内容摘要"""
def Process(message):
    """读取密钥"""
    with open(path+'/pem/publicB.pem','rb') as f :
        pubKey = f.read()
    with open(path+'/pem/privateB.pem', 'rb') as f:
        priKey = f.read()
    PRsa = ProcessRsa.PRsa(pubKey,priKey)
#     密文 c 明文message
    c = PRsa.public_long_encrypt(message)
    print(f"密文：{c}")
    m = PRsa.private_long_decrypt(c)
    print(f"密文：{m}")
    # print(type(m))
    # print(type(message))
#   生成签名，验证签名
#    类初始化，已经传入私钥
    sign = PRsa.sign(message)
    print(f'sign: {sign}')
#   验证签名，利用公钥
    verify = PRsa.verify(m, sign)
    print(f'verify: {verify}')
#     根据明文还原为图片
    ImgRes = base64.b64decode(m)
    with open("ResCode.jpg","wb") as f :
        f.write(ImgRes)

def main():
    # 生成密钥对
    # generateKey.genKeys("")`
    message =  readIMg()
    Process(message)


if __name__ == '__main__':
    main()