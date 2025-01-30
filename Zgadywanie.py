import random
def generate_code(n):  """generuje losowy (pseudo) szyfr z n cyfr"""
  return [random.randint(0, 9) for _ in range(n)]

def evaluate_guess(code, guess): """ocenanie odgadniecia, zwraca liczbe trafien na wlasciwych i niewlasciwych miejscach"""
  correct_position = sum(c == g for c, g in zip(code, guess))
  correct_digit = sum(min(code.count(d), guess.count(d)) for d in set(guess)) - correct_position
  return correct_position, correct_digit

def play_game(n):
  code = generate_code(n)
  attemps = 0

  print(f"Witaj w grze - odgadnij {n}-cyfrowy szyfr")

  while True:
    guess = input(f"Podaj {n} cyfr (bez spacji): ")
    if len(guess) != n or not guess.isdigit():
      print("Bledne dane - wprowadz dokladnie",n,"cyfr")
      continue
    guess = [int(digit) for digit in guess]
    attemps += 1

    correct_position, correct_digit = evaluate_guess(code, guess)

    if correct_position == n:
      print(f"Gratulacje - odgadles szyfr {code} w {attemps} probach"
      break
    else:
      print(f"poprawnych cyfr na wlasciwych miejscach: {correct_position}")
      print(f"poprawnych cyfr na niewlasciwych miejscach: {correct_digit}")
"""Uruchomienie gry dla n=4 szyfru"""
play_game(4)
  
  
