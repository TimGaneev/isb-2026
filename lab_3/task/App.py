import InsOuts
import SM4
import RSA


def generate_keys(symmetric_txt: str, public_pem: str, private_pem: str) -> None:
    """
    Генерация и сохранение ключей
    """
    symm_key = SM4.key_gen()
    private_key, public_key = RSA.key_gen()
    c_key = RSA.encryption(symm_key, public_key)
    print("Ключи сгенерированы")

    InsOuts.save_bin(symmetric_txt, c_key)
    print("Зашифрованный симметричный ключ сохранён в", symmetric_txt)
    InsOuts.save_private_key(private_pem, private_key)
    InsOuts.save_public_key(public_pem, public_key)
    return


def symmetric_encryption(text_txt: str, symmetric_txt: str, private_pem: str, encrypted_txt: str) -> None:
    """
    Шифрование данных
    """
    text = InsOuts.read_text(text_txt)
    c_key = InsOuts.read_bin(symmetric_txt)
    private_key = InsOuts.read_private_key(private_pem)

    symm_key = RSA.decryption(c_key, private_key)
    c_text = SM4.encryption(bytes(text, "utf-8"), symm_key)
    print("Текст зашифрован")
    InsOuts.save_bin(encrypted_txt, c_text)
    print("Зашифрованный текст сохранён в", encrypted_txt)
    return


def symmetric_decryption(encrypted_txt: str, symmetric_txt: str, private_pem: str, decrypted_txt: str) -> None:
    """
    Дешифрование данных
    """
    c_text = InsOuts.read_bin(encrypted_txt)
    c_key = InsOuts.read_bin(symmetric_txt)
    private_key = InsOuts.read_private_key(private_pem)

    symm_key = RSA.decryption(c_key, private_key)
    dc_text = SM4.decryption(c_text, symm_key)
    print("Текст расшифрован")
    InsOuts.save_text(decrypted_txt, dc_text.decode("utf-8"))
    print("Расшифрованный текст сохранён в", decrypted_txt)
    return


def menu_interface() -> int:
    """
    Вывод меню
    """
    actions = {
        "1": "Генерация ключей",
        "2": "Шифрование данных",
        "3": "Дешифрование данных",
        "4": "Вывести незашифрованный текст",
        "5": "Вывести расшифрованный текст",
        "6": "Вывести пути к используемым файлам",
        "0": "Завершение работы\n"
    }
    ch = -1
    while ch not in list(actions.keys()):
        print()
        for i, act in actions.items():
            print(i, ": ", act)
        ch = input("Выберите действие: ")
    print("\n")
    return int(ch)


def app(settings_json: str) -> None:
    """
    Приложение
    """
    settings = InsOuts.read_json(settings_json)
    text_txt = settings["initial_file"]
    encrypted_txt = settings["encrypted_file"]
    decrypted_txt = settings["decrypted_file"]
    symmetric_txt = settings["symmetric_key"]
    public_pem = settings["public_key"]
    private_pem = settings["secret_key"]

    act = menu_interface()
    while act:
        if act == 0:        #Завершение работы
            return
        elif act == 1:      #Генерация ключей
            generate_keys(symmetric_txt, public_pem, private_pem)
        elif act == 2:      #Шифрование данных
            symmetric_encryption(text_txt, symmetric_txt, private_pem, encrypted_txt)
        elif act == 3:      #Дешифрование данных
            symmetric_decryption(encrypted_txt, symmetric_txt, private_pem, decrypted_txt)
        elif act == 4:      #Вывести незашифрованный текст
            text = InsOuts.read_text(text_txt)
            print()
            print(text)
        elif act == 5:      #Вывести расшифрованный текст
            d_text = InsOuts.read_text(decrypted_txt)
            print()
            print(d_text)
        elif act == 6:      #Вывести пути к используемым файлам
            print("Шифруемый текст:", text_txt)
            print("Зашифрованный текст:", encrypted_txt)
            print("Расшифрованный текст:", decrypted_txt)
            print("Зашифрованный симметричный ключ:", symmetric_txt)
            print("Открытый ключ:", public_pem)
            print("Закрытый ключ:", private_pem, "\n")
        act = menu_interface()