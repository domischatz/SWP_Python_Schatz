class Player:
    def __init__(self, name):
        self.name = name  # Initialisierung des Spielernamens

    def option(self):
        while True:  # Schleife für wiederholte Eingabe
            try:
                option = int(input("Wählen Sie eine Option (1)Schere, (2)Stein, (3)Papier, (4)Echse, (5)Spock): "))
                if option in range(1, 6):  # Überprüfen, ob die Option gültig ist (zwischen 1 und 5)
                    return option
                else:
                    print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 5 eingeben.")
            except ValueError:  # Eingabe keine Zahl ist
                print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 5 eingeben.")