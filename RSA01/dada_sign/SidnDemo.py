"""实现图片传输的签名与改签"""
"""1.首先共享公钥
    2.利用hasb函数生成摘要
    3.对摘要，密文实现加密
    4.传输信息
    5.解密，验证签名。
"""
'''测试base64处理图片'''
import base64
import  generateRSA
image_path = 'demo.jpg'
# b代表二进制文件读取
'''获取摘要'''
with open(image_path,'rb') as f:
    image_base64 = base64.b64encode(f.read())
# with open('11.jpg','wb') as f:
#     f.write(base64.b64decode(image_base64))
import  hashlib
# sha1 = hashlib.sha1()
m = hashlib.md5()
m.update(image_base64)
A_data_sign = m.hexdigest().encode(encoding='utf-8')
# print(len(image_base64))
"""读取密钥
    利用A的私钥，然后加密处理签名和数据，假设A已经向B广播公钥，B亦是如此
"""
# print(type(A_data_sign))

# 数字签名
A_reuslt_sign = generateRSA.RSADemo.rsa_encrypt('privateA.pem',A_data_sign)
#明文加密
A_reuslt_data = generateRSA.RSADemo.rsa_encrypt('publicB.pem',image_base64)
print(A_reuslt_sign)
print(len(A_reuslt_data))
print(type(A_reuslt_data))

# plain = b'This_is_a_test_string!'
# #数字签名验证
# B_result_data = generateRSA.RSADemo.rsa_decrypt('privateB.pem',plain)
# print(B_result_data)




