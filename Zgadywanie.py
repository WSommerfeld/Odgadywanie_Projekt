import random

def generate_code(n):
    """Generuje losowy szyfr z n cyfr."""
    return [random.randint(0, 9) for _ in range(n)]

def evaluate_guess(code, guess):
    """Ocena odgadnięcia - zwraca liczbę trafień na właściwych i niewłaściwych miejscach."""
    correct_position = sum(c == g for c, g in zip(code, guess))
    correct_digit = sum(min(code.count(d), guess.count(d)) for d in set(guess)) - correct_position
    return correct_position, correct_digit

def play_game(n):
    """Główna funkcja gry."""
    code = generate_code(n)
    attempts = 0

    print(f"Witaj w grze! Odgadnij {n}-cyfrowy szyfr.")

    while True:
        guess = input(f"Podaj {n} cyfr (bez spacji): ")
        if len(guess) != n or not guess.isdigit():
            print("Błędne dane, wpisz dokładnie", n, "cyfr.")
            continue

        guess = [int(digit) for digit in guess]
        attempts += 1

        correct_position, correct_digit = evaluate_guess(code, guess)

        if correct_position == n:
            print(f"Gratulacje! Odgadłeś szyfr {code} w {attempts} próbach.")
            break
        else:
            print(f"Poprawnych cyfr na właściwych miejscach: {correct_position}")
            print(f"Poprawnych cyfr na złych miejscach: {correct_digit}")

"""Uruchomienie gry dla 4-cyfrowego szyfru"""
play_game(4)
