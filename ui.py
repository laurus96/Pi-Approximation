from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QWidget

class interfaccia_utente():

    def __init__(self):
        self.app = QApplication([])
        self.app.setStyle('Macintosh')
        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.title = str('PI: ')
        self.label = str('')

        

    def label_change(self, new_string):
        self.label = QLabel(new_string)
        self.layout.addWidget(self.title)
        #self.layout.addWidget(self.label)
        self.window.setLayout(self.layout)
        self.window.show()
        self.app.exec_()
  


if __name__ == '__main__':
    newUi = interfaccia_utente()

    stringa = str(input('Inserisci qualcosa a tuo piacimento: '))

    newUi.label_change(stringa)


    
    


