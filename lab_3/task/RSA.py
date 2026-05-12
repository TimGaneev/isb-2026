from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def key_gen():
    """
    Генерация открытого и закрытого ключей
    """
    keys = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    private_key = keys
    public_key = keys.public_key()
    return private_key, public_key


def encryption(text: bytes, public_key) -> bytes:
    """
    Шифрование алгоритмом RSA-OAEP
    """
    c_text = public_key.encrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    return c_text


def decryption(c_text: bytes, private_key) -> bytes:
    """
    Дешифрование алгоритмом RSA-OAEP
    """
    dc_text = private_key.decrypt(c_text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    return dc_text