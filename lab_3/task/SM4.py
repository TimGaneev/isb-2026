import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


bytes_num = 16


def key_gen() -> bytes:
    """
    Генерация ключа симметричного алгоритма

    Returns:
        ключ симметричного алгоритма
    """
    key = os.urandom(bytes_num)
    return key


def encryption(text: bytes, key: bytes) -> bytes:
    """
    Шифрование алгоритмом SM4

    Args:
        text: шифруемое сообщение
        key: ключ симметричного алгоритма
    Returns:
        зашифрованное сообщение и инициализирующий вектор
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

    Args:
        c_text: зашифрованное сообщение и инициализирующий вектор
        key: ключ симметричного алгоритма
    Returns:
        расшифрованное сообщение
    """
    split_idx = len(c_text)-bytes_num
    iv = c_text[split_idx:]

    cipher = Cipher(algorithms.SM4(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    dc_text = decryptor.update(c_text[:split_idx]) + decryptor.finalize()

    unpadder = padding.ANSIX923(bytes_num).unpadder()
    unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()
    return unpadded_dc_text