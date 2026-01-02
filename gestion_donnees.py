import sqlite3


def CreerTable():
    print("créer la table")
    conn = sqlite3.connect("Annuaire.db")
    cursor = conn.cursor()
    # requette ici
    cursor.execute(
        "CREATE TABLE if not exists adresse(Nom varchar(255),Prenom varchar(255), courriel varchar(255),Telephone int(10));")
    conn.commit()

