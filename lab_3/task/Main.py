import InsOuts
import App


def main() -> None:
    try:
        settings_json = InsOuts.parse_arguments()
        App.app(settings_json)
    except Exception as exc:
        print(f"Возникла ошибка: {exc}")


if __name__ == "__main__":
    main()