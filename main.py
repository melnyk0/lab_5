def is_prime(n):
    "Перевіряє, чи є число n простим."
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(a, b):
    # Знаходить всі прості числа між a та b (включно з a і b).
    # Визначаємо початок та кінець діапазону
    start = min(a, b)
    end = max(a, b)
    
    # Знаходимо прості числа в діапазоні
    primes = []
    for i in range(start, end + 1):
        if is_prime(i):
            primes.append(i)
    return primes

# Запитуємо в користувача введення чисел a і b
a = int(input("Введіть перше число (a): "))
b = int(input("Введіть друге число (b): "))

# Знаходимо та виводимо прості числа
primes = find_primes_in_range(a, b)
print(f"Прості числа між {a} і {b}: {primes}")
