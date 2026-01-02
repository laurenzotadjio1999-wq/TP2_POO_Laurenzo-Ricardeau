import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
import interface_graphique
import gestion_donnees

def InsererDansAnnuaire():
    print("inser dans la table")
    conn = sqlite3.connect("Annuaire.db")
    cursor = conn.cursor()
    # requette ici
    cursor.execute(
        "INSERT INTO Annuaire VALUES (" + lineEditNom.text() + ",'" + lineEditPreNom.text() + "','" + lineEditcourriel.text() + "','" + lineEditTelephone.text() + "');")
    conn.commit()
    AfficherTout()