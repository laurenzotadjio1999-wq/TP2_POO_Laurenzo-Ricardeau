
# Importation des packages necessaire.
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QLabel,QGridLayout
import gestion_donnees
import operations_CRUD

#Creation de notre fenêtre:
app = QApplication([])
fenetre = QWidget()
fenetre.setWindowTitle("TP2_POO_Laurenzo-Ricardeau")
fenetre.setGeometry(200, 200, 650, 500)



# grid layout
grid = QGridLayout()
fenetre.setLayout(grid)

# création des Qlabels
#Création d'un message de Bienvenu
message = "*********************************************************\n"
message += "*          BIENVENU DANS NOTRE CARNET D'ADRESSE                         ***\n"
message += "*********************************************************"
label_bienvenue = QLabel(message)
grid.addWidget(label_bienvenue, 0, 2, 1, 6)
label_bienvenue.setStyleSheet("font-family: Calibri; font-weight: bold;")


#Création du boutton "créer la table"
btn1 = QPushButton(fenetre)
btn1.setText("Créer Table")
btn1.setGeometry(500, 100, 100, 30)
grid.addWidget(btn1, 1,8)
btn1.clicked.connect(gestion_donnees.CreerTable)

#Création du boutton "inserer"
btn2 = QPushButton(fenetre)
btn2.setText("INSERER")
btn2.setGeometry(500, 150, 100, 30)
grid.addWidget(btn2, 2,8)
btn2.clicked.connect(lambda: operations_CRUD.InsererDansAnnuaire(lineEditNom, lineEditPreNom, lineEditCourriel, lineEditTelephone, qtab))

#Création des champs pour le bouton "inserer"
labelTelephone = QLabel("Telephone :")
labelNom = QLabel("Nom :")
labelPrenom = QLabel("Prénom :")
labelCourriel = QLabel("courriel :")

lineEditNom = QLineEdit(fenetre)
lineEditNom.setGeometry(150, 150, 100, 30)
grid.addWidget(labelNom, 2,0)
grid.addWidget(lineEditNom, 2,1)

lineEditPreNom = QLineEdit(fenetre)
lineEditPreNom.setGeometry(150, 150, 100, 30)
grid.addWidget(labelPrenom, 2,2)
grid.addWidget(lineEditPreNom, 2,3)

lineEditCourriel = QLineEdit(fenetre)
lineEditCourriel.setGeometry(350, 150, 100, 30)
grid.addWidget(labelCourriel, 2,4)
grid.addWidget(lineEditCourriel, 2,5)

lineEditTelephone = QLineEdit(fenetre)
lineEditTelephone.setGeometry(450, 150, 100, 30)
grid.addWidget(labelTelephone, 2,6)
grid.addWidget(lineEditTelephone, 2,7)

#Création du boutton afficher tout
btn3 = QPushButton(fenetre)
btn3.setText("AfficherTout")
btn3.setGeometry(500, 250, 100, 30)
grid.addWidget(btn3, 5,8)
btn3.clicked.connect(lambda :operations_CRUD.AfficherTout(qtab))


#Création du boutton "modifier"
btn4 = QPushButton(fenetre)
btn4.setText("MODIFIER")
btn4.setGeometry(500, 250, 100, 30)
grid.addWidget(btn4, 3,8)
btn4.clicked.connect(lambda: operations_CRUD.Modifier(lineEditNom, lineEditPreNom, lineEditCourriel, lineEditTelephone, qtab))

# Création du "QTable" pour l'affichage des différents enregistrements
qtab = QTableWidget(fenetre)
qtab.setRowCount(8)
qtab.setColumnCount(4)
#qtab.setGeometry(100, 250, 450, 200)
qtab.setMinimumHeight(200)
qtab.setMinimumWidth(450)
qtab.setHorizontalHeaderLabels([ 'Nom', 'Prénom', 'Courriel','Téléphone'])
grid.addWidget(qtab, 7, 0, 2, 8)
qtab.cellClicked.connect(
    lambda row, column: operations_CRUD.Remplir_auto(
        qtab, lineEditNom, lineEditPreNom, lineEditCourriel, lineEditTelephone, row, column
    )
)

#2- Créer un boutton supprimer
labelSuppNom = QLabel("Nom à supprimer :")
btn5 = QPushButton(fenetre)
btn5.setText("SUPPRIMER")
btn5.setGeometry(500, 200, 100, 30)
grid.addWidget(btn5, 4,8)
btn5.clicked.connect(lambda: operations_CRUD.SupprimerParNom(lineEditNom, qtab))
lineEditSuppNom = QLineEdit(fenetre)
lineEditSuppNom.setGeometry(350, 200, 100, 30)
grid.addWidget(labelSuppNom, 4,6)
grid.addWidget(lineEditSuppNom, 4,7 )




# affichage de la fenetre + execution de l'application ... :)
fenetre.show()
app.exec()