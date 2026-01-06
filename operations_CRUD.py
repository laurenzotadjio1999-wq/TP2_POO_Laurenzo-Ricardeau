import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
import interface_graphique
import gestion_donnees

#Créatiuon de la fonction Insérer
def InsererDansAnnuaire():
    print("inser dans la table")
    conn = sqlite3.connect("Annuaire.db")
    cursor = conn.cursor()
    # requette ici
    cursor.execute(
        "INSERT INTO Annuaire VALUES (" + interface_graphique.lineEditNom.text() + ",'" + interface_graphique.lineEditPreNom.text() + "','" + interface_graphique.lineEditcourriel.text() + "','" + interface_graphique.lineEditTelephone.text() + "');")
    conn.commit()
    AfficherTout()


# Créatiuon de la fonction AfficherTout
def AfficherTout():
    print("afficher toute la table")
    conn = sqlite3.connect("Annuaire.db")
    cursor = conn.cursor()
    # requette ici
    cursor.execute("SELECT * FROM adresse")
    resultat = cursor.fetchall()
 # QTable
    interface_graphique.qtab.setRowCount(len(resultat))
    interface_graphique.qtab.setColumnCount(4)
    interface_graphique.qtab.setGeometry(50, 250, 450, 200)
    interface_graphique.qtab.setHorizontalHeaderLabels(['Nom', 'Prenom', 'Courriel', 'Telephone'])
    #
    for i in range(len(resultat)):
        for j in range(4):
            interface_graphique.qtab.setItem(i, j, QTableWidgetItem(str(resultat[i][j])))
