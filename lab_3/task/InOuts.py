import json


def read_text(file_name: str) -> str:
    """
    Чтение текстового файла
    """
    with open(file_name, "r", encoding="utf8") as file:
        content = file.read()
    return content


def save_text(file_name: str, content) -> None:
    """
    Сохранение текстового файла
    """
    with open(file_name, "w", encoding="utf8") as file:
        file.write(content)
    return


def read_bin(file_name: str) -> bytes:
    """
    Чтение бинарного файла
    """
    with open(file_name, "rb") as file:
        content = file.read()
    return content


def save_bin(file_name: str, content) -> None:
    """
    Сохранение бинарного файла
    """
    with open(file_name, "wb") as file:
        file.write(content)
    return


def read_json(file_name: str) -> dict[str: str]:
    with open(file_name) as json_file:
        content = json.load(json_file)
    return content