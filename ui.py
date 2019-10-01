from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QWidget

app = QApplication([])
app.setStyle('Macintosh')
label = QLabel('Hello world!')
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(label)
window.setLayout(layout)
window.show()
app.exec_()
    


