import os
from utilitis import compare_squares, translate_message

# Шлях до файлу MyData.txt
DATA_FILE = 'MyData.txt'

def read_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as file:
                lines = file.readlines()
                x = int(lines[0].strip())
                y = int(lines[1].strip())
                language = lines[2].strip()
                return x, y, language
        except (ValueError, IndexError):
            return None
    return None

def write_data(x, y, language):
    with open(DATA_FILE, 'w') as file:
        file.write(f"{x}\n")
        file.write(f"{y}\n")
        file.write(f"{language}\n")
    print(f"Дані збережено в файл {DATA_FILE}")

def get_user_input():
    x = int(input("Введіть число x: "))
    y = int(input("Введіть число y: "))
    language = input("Введіть мову інтерфейсу (uk/en): ")
    return x, y, language

def main():
    data = read_data()
    if not data:
        print("Файл MyData відсутній або містить некоректні дані.")
        x, y, language = get_user_input()
        write_data(x, y, language)
        return

    x, y, language = data
    if language not in ['uk', 'en']:
        language = 'uk'  # Використовуємо українську мову за замовчуванням

    print(translate_message("Мова", language) + f": {language}")
    print(translate_message("Два числа", language) + f" x={x}, y={y}")

    result_message = compare_squares(x, y, language)
    print(result_message)

if __name__ == "__main__":
    main()
