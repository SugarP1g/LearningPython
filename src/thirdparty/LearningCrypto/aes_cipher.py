#!/usr/bin/env python
# encoding: utf-8

import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


def generate_key(length):
    with open("/dev/random", "rb") as f:
        key = f.read(length)
        return key


class AESCipher(object):

    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        # iv = Random.new().read(AES.block_size)
        iv = generate_key(AES.block_size)
        print("encrypt: IV is ", str(iv))
        print("encrypt: key is ", self.key)
        print("encrypt: key length is ", len(self.key))
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        print("decrypt: IV is ", str(iv))
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]


if __name__ == "__main__":
    aes_key = generate_key(16)
    print("AES init key: ", str(aes_key))
    cipher = AESCipher(str(aes_key))
    ciphertext = cipher.encrypt("aaaa")
    print("cipher text: ", ciphertext)
    plaintext = cipher.decrypt(ciphertext)
    print("plain text: ", plaintext)
