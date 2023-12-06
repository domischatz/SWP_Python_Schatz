import random

def generate_random_income():
    return random.randint(10000, 50000)

# Liste mit Personen
persons = ["Person1", "Person2", "Person3", "Person4", "Person5"]

# Dictionary erstellen, wobei jedem Namen ein zufälliges Einkommen zugeordnet wird
income_dict = {person: generate_random_income() for person in persons}

# Steuerklasse zuordnen
for person, income in income_dict.items():
    if income <= 15000:
        income_dict[person] = {"Einkommen": (income*0.60), "Steuerklasse": 1}
    else:
        income_dict[person] = {"Einkommen": income*0.50, "Steuerklasse": 2}

# Ausgabe des aktualisierten Dictionaries
for person, data in income_dict.items():
    print(f"{person}: Einkommen {data['Einkommen']} Euro, Steuerklasse {data['Steuerklasse']}")
