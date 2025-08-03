from faker import Faker
import unicodedata
import uuid

faker = Faker("pt_BR")

def strip_accents(text: str) -> str:
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))

def generate_person_data() -> dict:
    raw_first = faker.first_name()
    raw_last  = faker.last_name()

    first_clean = strip_accents(raw_first).replace(" ", "").lower()
    last_clean  = strip_accents(raw_last).replace(" ", "").lower()

    unique_id = uuid.uuid4().hex[:8]

    email = f"{first_clean}.{last_clean}.{unique_id}@example.com"

    return {
        "first_name": raw_first,
        "last_name":  raw_last,
        "email":      email
    }
