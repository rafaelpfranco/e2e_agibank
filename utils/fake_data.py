from faker import Faker
import random
import unicodedata

faker = Faker("pt_BR")

def strip_accents(text: str) -> str:
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))

def generate_person_data() -> dict:
    # gera nome e sobrenome com o Faker
    raw_first = faker.first_name()
    raw_last  = faker.last_name()

    # limpa acentos e espaços, e passa para minúsculas
    first_clean = strip_accents(raw_first).replace(" ", "").lower()
    last_clean  = strip_accents(raw_last).replace(" ", "").lower()

    # sufixo de dois dígitos aleatórios
    suffix = f"{random.randint(0, 99):02}"

    email = f"{first_clean}_{last_clean}_{suffix}@gmail.com"

    return {
        "first_name": raw_first,
        "last_name": raw_last,
        "email": email
    }
