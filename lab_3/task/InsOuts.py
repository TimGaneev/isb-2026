import argparse
import json


from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


def parse_arguments() -> str:
    """
    Парсинг аргументов из командной строки
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--settings", default="settings.json", type=str, help="settings file path")
    args = parser.parse_args()
    return args.settings


def save_text(file_name: str, content) -> None:
    """
    Сохранение текстового файла
    """
    with open(file_name, "w", encoding="utf8") as file:
        file.write(content)
    print("Текст сохранён в файл", file_name)
    return


def read_text(file_name: str) -> str:
    """
    Чтение текстового файла
    """
    with open(file_name, "r", encoding="utf8") as file:
        content = file.read()
    print("Текст считан из файла", file_name)
    return content


def save_bin(file_name: str, content) -> None:
    """
    Сохранение бинарного файла
    """
    with open(file_name, "wb") as file:
        file.write(content)
    return


def read_bin(file_name: str) -> bytes:
    """
    Чтение бинарного файла
    """
    with open(file_name, "rb") as file:
        content = file.read()
    print("Симметричный ключ считан из файла", file_name)
    return content


def save_public_key(public_pem: str, public_key) -> None:
    """
    Сериализация открытого ключа
    """
    with open(public_pem, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                 format=serialization.PublicFormat.SubjectPublicKeyInfo))
    print("Открытый ключ сохранён в файл", public_pem)
    return


def read_public_key(public_pem: str):
    """
    Десериализация открытого ключа
    """
    with open(public_pem, 'rb') as pem_in:
        public_bytes = pem_in.read()
    d_public_key = load_pem_public_key(public_bytes)
    print("Открытый ключ считан из файла", public_pem)
    return d_public_key


def save_private_key(private_pem: str, private_key) -> None:
    """
    Сериализация закрытого ключа
    """
    with open(private_pem, 'wb') as private_out:
        private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                    encryption_algorithm=serialization.NoEncryption()))
    print("Закрытый ключ сохранён в файл", private_pem)
    return


def read_private_key(private_pem: str):
    """
    Десериализация закрытого ключа
    """
    with open(private_pem, 'rb') as pem_in:
      private_bytes = pem_in.read()
    d_private_key = load_pem_private_key(private_bytes,password=None,)
    print("Закрытый ключ считан из файла", private_pem)
    return d_private_key


def read_json(file_name: str) -> dict[str: str]:
    """
    Чтение файла настроек
    """
    with open(file_name) as json_file:
        content = json.load(json_file)
    print("Пути к файлам считаны из", file_name)
    return content