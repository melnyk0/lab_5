import string

def sort_words(words):
   

    ukrainian_words = []
    english_words = []

    for word in words:
        if word.isalpha() and word.lower() in string.ascii_lowercase:
            english_words.append(word.lower())
        elif word.isalpha():
            ukrainian_words.append(word.lower())

    return sorted(ukrainian_words) + sorted(english_words)

def main():
    filename = "input.txt"  

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            first_line = file.readline().strip()
            print("Перше речення:", first_line)

            
            words = first_line.translate(str.maketrans('', '', string.punctuation)).split()

            sorted_words = sort_words(words)
            print("Відсортовані слова:")
            print(sorted_words)
            print("Кількість слів:", len(sorted_words))

    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")

if __name__ == "__main__":
    main()