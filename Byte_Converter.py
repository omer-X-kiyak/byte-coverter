def bit_to_byte(num):
    return num / 8

def convert(size, unit_from, unit_to, units):
    size *= 1024 ** units.index(unit_from.lower())
    size = size / 1024 ** units.index(unit_to.lower())
    return size

def main():
    # Dil seçimi için kullanıcının seçeceği dilin kodu
    languages = {
        "en": {
            "size_input": "Enter the size: ",
            "unit_from_input": "Enter the unit (BIT, BYTE, KB, MB, GB, TB, PB, EB, ZB, YB): ",
            "unit_to_input": "Enter the unit to convert to (BIT, BYTE, KB, MB, GB, TB, PB, EB, ZB, YB): ",
            "size_output": "Size in {}:",
            "continue_prompt": "Do you want to continue? (y/n): "
        },
        "tr": {
            "size_input": "Boyutu girin: ",
            "unit_from_input": "Birimleri girin (BIT, BYTE, KB, MB, GB, TB, PB, EB, ZB, YB): ",
            "unit_to_input": "Dönüştürmek istediğiniz birimi girin (BIT, BYTE, KB, MB, GB, TB, PB, EB, ZB, YB): ",
            "size_output": "{} olarak boyut:",
            "continue_prompt": "Devam etmek istiyor musunuz? (e/h): "
        }
    }

    # Dil seçimi için kullanıcıdan girdi alınması
    while True:
        lang_choice = input("Select language (en/tr): ").lower()
        if lang_choice in languages.keys():
            lang = languages[lang_choice]
            break
        else:
            print("Invalid choice. Try again.\n")

    # Programın çalışması için gerekli olan birimlerin listesi
    units = ["bit", "byte", "kb", "mb", "gb", "tb", "pb", "eb", "zb", "yb"]


    while True:
        size = float(input(lang["size_input"]))
        unit_from = input(lang["unit_from_input"]).lower()
        unit_to = input(lang["unit_to_input"]).lower()

        if unit_from == "bit":
            size = bit_to_byte(size)
            unit_from = "byte"

        size = convert(size, unit_from, unit_to, units)

        print(lang["size_output"].format(unit_to.upper()), size)

        answer = input(lang["continue_prompt"]).lower()
        if answer not in ["y", "e"]:
            break


if __name__ == "__main__":
    main()
