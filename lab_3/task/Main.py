import argparse
import os

import InOuts
import SM4
import RSA


def parse_arguments() -> list:
    """
    Парсинг аргументов из командной строки
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-l1", "--pr_language_1", default="cpp", type=str, help="programming language 1")
    parser.add_argument("-l2", "--pr_language_2", default="py", type=str, help="programming language 2")
    parser.add_argument("-l3", "--pr_language_3", default="java", type=str, help="programming language 3")
    args = parser.parse_args()
    return [args.pr_language_1, args.pr_language_2, args.pr_language_3]


def main() -> None:
    try:
        settings = InOuts.read_json("settings.json")
        #langs = parse_arguments()

        symm_key = SM4.key_gen()
        private_key, public_key = RSA.key_gen()

        text = InOuts.read_text(settings["initial_file"])

        c_key = RSA.encryption(symm_key, public_key)
        dc_key = RSA.decryption(c_key, private_key)

        print(symm_key)
        print(dc_key)
    except Exception as exc:
        print(f"Возникла ошибка: {exc}")


if __name__ == "__main__":
    main()