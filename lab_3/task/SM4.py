import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


bytes_num = 16


def key_gen() -> bytes:
    """
    Генерация ключа симметричного алгоритма
    """
    key = os.urandom(bytes_num)
    return key


def encryption(text: bytes, key: bytes) -> bytes:
    """
    Шифрование алгоритмом SM4
    """
    iv = os.urandom(bytes_num)
    cipher = Cipher(algorithms.SM4(key), modes.CBC(iv))
    padder = padding.ANSIX923(bytes_num).padder()
    padded_text = padder.update(text) + padder.finalize()

    encryptor = cipher.encryptor()
    c_text = encryptor.update(padded_text) + encryptor.finalize()
    return c_text + iv


def decryption(c_text: bytes, key: bytes) -> bytes:
    """
    Дешифрование алгоритмом SM4
    """
    split_idx = len(c_text)-bytes_num
    iv = c_text[split_idx:]

    cipher = Cipher(algorithms.SM4(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    dc_text = decryptor.update(c_text[:split_idx]) + decryptor.finalize()

    unpadder = padding.ANSIX923(bytes_num).unpadder()
    unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()
    return unpadded_dc_text