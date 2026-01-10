import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
import gestion_donnees

#Créatiuon de la fonction Insérer
def InsererDansAnnuaire(lineEditNom, lineEditPreNom, lineEditCourriel, lineEditTelephone, qtab):
    print("inser dans la table")
    conn = sqlite3.connect("Annuaire")
    cursor = conn.cursor()
    # requette ici
    cursor.execute(
        "INSERT INTO adresse (Nom, Prenom, Courriel, Telephone) VALUES (?, ?, ?, ?)",

            (lineEditNom.text(), lineEditPreNom.text(), lineEditCourriel.text(), lineEditTelephone.text())

    )
    conn.commit()
    AfficherTout(qtab)


# Créatiuon de la fonction AfficherTout
def AfficherTout(qtab):
    print("afficher toute la table")
    conn = sqlite3.connect("Annuaire")
    cursor = conn.cursor()
    # requette ici
    cursor.execute("SELECT * FROM adresse")
    resultat = cursor.fetchall()
    conn.close()
 # QTable
    qtab.setRowCount(len(resultat))
    qtab.setColumnCount(4)
    qtab.setGeometry(50, 250, 450, 200)
    qtab.setHorizontalHeaderLabels(['Nom', 'Prenom', 'Courriel', 'Telephone'])
    #
    for i in range(len(resultat)):
        for j in range(4):
            qtab.setItem(i, j, QTableWidgetItem(str(resultat[i][j])))


