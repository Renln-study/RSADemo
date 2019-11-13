from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

def rsa_encrypt(plain):
    with open('publicA.pem','rb') as f:
        data = f.read()
        key = RSA.importKey(data)
        rsa = PKCS1_v1_5.new(key)
        cipher = rsa.encrypt(plain)
        return base64.b64encode(cipher)

def rsa_decrypt(cipher):
    with open('privateA.pem','rb') as f:
        data = f.read()
        key = RSA.importKey(data)
        rsa = PKCS1_v1_5.new(key)
        plain = rsa.decrypt(base64.b64decode(cipher),'ERROR') # 'ERROR'必需
        return plain

if __name__ == '__main__':
    plain_text = b'This_is_a_test_string!'
    cipher = rsa_encrypt(plain_text)
    print(cipher)
    plain = rsa_decrypt(cipher)
    print(plain)