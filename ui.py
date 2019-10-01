from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])
label = QtWidgets.QLabel('Ciao Mondo!')
window = QtWidgets.QWidget()
layout = QtWidgets.QVBoxLayout()
layout.addWidget(label)
window.setLayout(layout)
window.setWindowTitle("Test")
window.show()
app.exec_()