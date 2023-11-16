import hashlib
import os

def hash_haslo(haslo):
    # Tworzenie soli
    salt = os.urandom(16)

    # Hashowanie hasła z solą
    hashed_haslo = hashlib.pbkdf2_hmac(
        'sha256',  # Używany algorytm skrótu
        haslo.encode('utf-8'),  # Konwersja hasła na bajty
        salt,  # Sól
        100000  # Liczba iteracji
    )
    return salt + hashed_haslo

print("Hello, world!")

login = input("Podaj login: ")
haslo = input("Podaj haslo: ")


hashed = hash_haslohaslo)
print("Zaszyfrowane hasło:", hashed)