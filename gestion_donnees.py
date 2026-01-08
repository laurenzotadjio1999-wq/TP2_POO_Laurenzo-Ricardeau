import sqlite3


def CreerTable():
    print("créer la table")
    conn = sqlite3.connect("Annuaire.db")
    cursor = conn.cursor()
    # requette ici
    cursor.execute(
        "CREATE TABLE if not exists adresse(Nom TEXT(255),Prenom TEXT(255), courriel TEXT(255),Telephone TEXT(10));")
    conn.commit()

