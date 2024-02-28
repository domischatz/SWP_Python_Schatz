from Spieler import Player
from Computer import Computer

import json

def game():  # Spiel starten
    options = {1: 'Rock', 2: 'Paper', 3: 'Scissors', 4: 'Spock', 5: 'Lizard'}  # Dictionary
    spiel=True
    data_dic = get_data()  # Landen Spieldaten
    p=Player(input("Name:")) #Namen erstellen
    if input("Statistik(S)/Play(P)")=="S":
        print(data_dic)  # atistike anzeigen,
    c=Computer()  # Computer erstellen
    while spiel:  # Hauptspielschleife
        option= p.option()  # Spieler wählt eine Option
        option2=c.option()  # Computer wählt eine Option
        winner=check_inputs(option,option2)  #Gewinner
        if winner==1:  #Spieler gewinnt
            print(f"{p.name} hat gewonnen mit {options[option]}")
            print(f"Computer {options[option2]}")  # Auswahl Computers
            data_dic["Player"]=data_dic["Player"]+1  # Spieldaten aktualisieren
            data_dic[options[option]]=data_dic[options[option]]+1  # gewählten Optionen aktualisieren
            export_data(data_dic)  # Spieldaten exportieren
        elif winner==2:  #Computer gewinnt
            print(f"{c.name} hat gewonnen mit {options[option2]}")
            print(f"{p.name}: {options[option]}")
            data_dic["Computer"] = data_dic["Computer"] + 1
            data_dic[options[option]] = data_dic[options[option]] + 1
            export_data(data_dic)
        elif winner==0:  # Unentschieden
            print("Unentschieden")
            data_dic["Unentschieden"] = data_dic["Unentschieden"] + 1
            data_dic[options[option]] = data_dic[options[option]] + 1
            export_data(data_dic)
        con=input("Weiterspielen: J/N")
        if con == "N" or con == "n":
            spiel= False  # Spielschleife beenden
        elif con == "J" or con == "j":
            spiel= True

def check_inputs(option1,option2):
    regeln = {
        1: [4, 3],  # Schere schlägt "Echse", "Papier"
        2: [4, 1],  # Stein schlägt "Echse", "Schere"
        3: [2, 5],  # Papier schlägt "Stein", "Spock"
        4: [3, 5],  # Echse schlägt "Papier", "Spock"
        5: [2, 1]  # Spock schlägt "Stein", "Schere"
    }

    if option1 == option2:  # Bei Gleichstand
       return 0  # Unentschieden zurückgeben
    elif option1 not in regeln[option2]:  # Spieler gewinnt nicht
        return 2  # Computer  Gewinner
    else:  # Ansonsten
        return 1  # Spieler Gewinner

def export_data(data):
    with open('Data.json', 'w') as datei:  # Spieldaten in JSON-Datei exportieren
        json.dump(data, datei, indent=2, ensure_ascii=False)  # Daten schreiben

def get_data():
    with open('Data.json', 'r') as datei:  # Spieldaten aus JSON-Datei laden
        daten = json.load(datei)  # Daten laden
        return daten  #

def main():
    game()  # Spiel ausführen

if __name__ =="__main__":
    main()
