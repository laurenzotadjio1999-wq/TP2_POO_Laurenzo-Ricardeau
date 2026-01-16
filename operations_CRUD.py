import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
import gestion_donnees

#Créatiuon de la fonction Insérer
def InsererDansAnnuaire(lineEditNom, lineEditPreNom, lineEditCourriel, lineEditTelephone, qtab):
    print("inserer dans la table")
    conn = sqlite3.connect("Annuaire.db")
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
    conn = sqlite3.connect("Annuaire.db")
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


def SupprimerParNom(lineEditSuppNom, qtab):
    print("Supprimer dans la table")
    conn = sqlite3.connect("Annuaire.db")
    cursor = conn.cursor()
    # requette ici
    cursor.execute("DELETE FROM adresse WHERE Nom = ?", (lineEditSuppNom.text(),))
    conn.commit()
    conn.close()
    # rafraîchir l’affichage
    AfficherTout(qtab)

def Remplir_auto(qtab, lineEditNom, lineEditPreNom, lineEditCourriel, lineEditTelephone, row, column):
        # Récupérer les valeurs de la ligne sélectionnée
        nom = qtab.item(row, 0).text()
        prenom = qtab.item(row, 1).text()
        courriel = qtab.item(row, 2).text()
        telephone = qtab.item(row, 3).text()
        # Remplir les champs correspondants dans le formulaire
        lineEditNom.setText(nom)
        lineEditPreNom.setText(prenom)
        lineEditCourriel.setText(courriel)
        lineEditTelephone.setText(telephone)
        # Mettre en évidence la ligne sélectionnée (effet visuel)
        qtab.selectRow(row)

def Modifier(lineEditNom, lineEditPreNom, lineEditCourriel, lineEditTelephone, qtab):
    nom = lineEditNom.text().strip()
    prenom = lineEditPreNom.text().strip()
    courriel = lineEditCourriel.text().strip()
    telephone = lineEditTelephone.text().strip()
    print("Modifier dans la table")
    conn = sqlite3.connect("Annuaire.db")
    cursor = conn.cursor()
    # requette ici
    cursor.execute("""UPDATE adresse SET Nom=?,Prenom=?,Telephone=? WHERE Courriel = ?;""", (nom, prenom, telephone, courriel))
    conn.commit()
    conn.close()
    # rafraîchir l’affichage
    AfficherTout(qtab)