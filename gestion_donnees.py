import sqlite3


def CreerTable():
    print("créer la table")
    conn = sqlite3.connect("Annuaire")
    cursor = conn.cursor()
    # requette ici
    cursor.execute(
        "CREATE TABLE if not exists adresse(Nom TEXT,Prenom TEXT, Courriel TEXT,Telephone TEXT);")
    conn.commit()

