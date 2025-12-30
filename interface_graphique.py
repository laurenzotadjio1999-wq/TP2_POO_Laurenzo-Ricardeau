
# Importation des packages necessaire.
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QLabel,QGridLayout


#Creation de notre fenêtre:
app = QApplication([])
fenetre = QWidget()
fenetre.setWindowTitle("TP2_POO_Laurenzo-Ricardeau")
fenetre.setGeometry(100, 100, 650, 500)



# grid layout
grid = QGridLayout()
fenetre.setLayout(grid)

# création des Qlabels
#Création d'un message de Bienvenu
message = "*********************************************************\n"
message += "*          BIENVENU DANS NOTRE CARNET D'ADRESSE                  *\n"
message += "********************************************************"
label_bienvenue = QLabel(message)
grid.addWidget(label_bienvenue, 0, 2, 1, 6)
label_bienvenue.setStyleSheet("font-family: Calibri; font-weight: bold;")


#Création du boutton "créer la table"
btn1 = QPushButton(fenetre)
btn1.setText("Créer Table")
btn1.setGeometry(500, 100, 100, 30)
grid.addWidget(btn1, 1,8)
#btn1.clicked.connect(CreerTable)

#Création du boutton "inserer"
btn2 = QPushButton(fenetre)
btn2.setText("INSERER")
btn2.setGeometry(500, 150, 100, 30)
grid.addWidget(btn2, 2,8)
#btn2.clicked.connect(InsererDansTablePersonne)

#Création des champs pour le bouton "inserer"
labelID = QLabel("ID :")
labelNom = QLabel("Nom :")
labelPrenom = QLabel("Prénom :")
labelMail = QLabel("courriel :")

lineEditID = QLineEdit(fenetre)
lineEditID.setGeometry(50, 150, 100, 30)
grid.addWidget(labelID, 2,0)
grid.addWidget(lineEditID, 2,1)

lineEditNom = QLineEdit(fenetre)
lineEditNom.setGeometry(150, 150, 100, 30)
grid.addWidget(labelNom, 2,2)
grid.addWidget(lineEditNom, 2,3)

lineEditPreNom = QLineEdit(fenetre)
lineEditPreNom.setGeometry(250, 150, 100, 30)
grid.addWidget(labelPrenom, 2,4)
grid.addWidget(lineEditPreNom, 2,5)

lineEditMail = QLineEdit(fenetre)
lineEditMail.setGeometry(350, 150, 100, 30)
grid.addWidget(labelMail, 2,6)
grid.addWidget(lineEditMail, 2,7)

#Création du boutton "modifier"
btn4 = QPushButton(fenetre)
btn4.setText("MODIFIER")
btn4.setGeometry(500, 250, 100, 30)
grid.addWidget(btn4, 3,8)

# Création du "QTable" pour l'affichage des différents enregistrements
qtab = QTableWidget(fenetre)
qtab.setRowCount(5)
qtab.setColumnCount(5)
qtab.setGeometry(50, 250, 450, 200)
qtab.setHorizontalHeaderLabels(['id', 'nom', 'prenom', 'courriel','Téléphone'])
grid.addWidget(qtab, 5, 0, 2, 8)

#2- Créer un boutton supprimer
labelSuppID = QLabel("ID ADRESSE A SUPPRIER :")
btn5 = QPushButton(fenetre)
btn5.setText("SUPPRIMER")
btn5.setGeometry(500, 200, 100, 30)
grid.addWidget(btn5, 4,8)
#btn5.clicked.connect(SupprimerId)
lineEditSuppID = QLineEdit(fenetre)
lineEditSuppID.setGeometry(350, 200, 100, 30)
grid.addWidget(labelSuppID, 4,5)
grid.addWidget(lineEditSuppID, 4,7 )

#Création un boutton afficher tout
btn3 = QPushButton(fenetre)
btn3.setText("AfficherTout")
btn3.setGeometry(500, 250, 100, 30)
grid.addWidget(btn3, 5,8)
#btn3.clicked.connect(AfficherTout)



# affichage de la fenetre + execution de l'application ... :)
fenetre.show()
app.exec()