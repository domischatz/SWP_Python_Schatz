from flask import Flask, jsonify, request
import sqlite3
import json

app = Flask(__name__)
def setup_db():
    connection = sqlite3.connect('spiel_data.db')  # Verbindung DB
    cursor = connection.cursor()  # Cursor erstellen, für Datenbankabfragen

    # Tabelle
    cursor.execute('''CREATE TABLE IF NOT EXISTS stats (
                        name TEXT,
                        value INTEGER
                    )''')

    connection.commit()  # Änderungen in der Datenbank speichern
    connection.close()  # Verbindung zur Datenbank schließen

# Speichern der Daten in die Datenbank
def save_json_data_to_database(data):
    connection = sqlite3.connect('spiel_data.db')
    cursor = connection.cursor()

    # Tabelle leeren, um alte Daten zu entfernen
    cursor.execute("DELETE FROM stats")

    # neue Daten einfügen
    for key, value in data.items():
        cursor.execute("INSERT INTO stats (name, value) VALUES (?, ?)", (key, value))

    connection.commit()
    connection.close()

#Laden von Daten
def load_data_from_json(filename):
    with open(filename, 'r') as file:  # JSON-Datei öffnen
        data = json.load(file)  #JSON-Datei laden
    return data

#Abrufen gespeicherten Daten
def get_data_from_database():
    connection = sqlite3.connect('spiel_data.db')
    cursor = connection.cursor()

    #Daten aus der Tabelle abrufen
    cursor.execute("SELECT * FROM stats")
    data = cursor.fetchall()  # Alle Datensätze abrufen
    connection.close()
    return data

@app.route('/get_data', methods=['GET'])
def get_saved_data():
    data = get_data_from_database()  # Daten aus der Datenbank abrufen
    return jsonify(data)

#
@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.get_json()  # JSON-Daten von der Anfrage erhalten
    save_json_data_to_database(data)  # Daten in DB speichern
    return 'Daten erfolgreich gespeichert!'

if __name__ == '__main__':
    setup_db()
    json_data = load_data_from_json('C:/Users/Schule/PycharmProjects/SWP_Python_Schatz/RSP/Data.json')  # Daten laden
    save_json_data_to_database(json_data)  # Daten speichern
    app.run(debug=True)
