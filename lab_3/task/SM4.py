import os


from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


bytes_num = 16

def key_gen() -> bytes:
    key = os.urandom(bytes_num)
    return key


def cipher_setup(key: bytes):
    iv = os.urandom(bytes_num)
    cipher = Cipher(algorithms.SM4(key), modes.CBC(iv))
    return cipher


def encryption(text: str, cipher) -> bytes:
    padder = padding.ANSIX923(bytes_num).padder()
    padded_text = padder.update(bytes(text, 'UTF-8')) + padder.finalize()

    encryptor = cipher.encryptor()
    c_text = encryptor.update(padded_text) + encryptor.finalize()
    return c_text


def decryption(c_text: bytes, cipher) -> bytes:
    decryptor = cipher.decryptor()
    dc_text = decryptor.update(c_text) + decryptor.finalize()

    unpadder = padding.ANSIX923(bytes_num).unpadder()
    unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()
    return unpadded_dc_text