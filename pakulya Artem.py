from  PyQt5.QtCore import*
from  PyQt5.QtWidgets import*
from  PyQt5.QtGui import QIcon
app=QApplication([])
window=QWidget()
window.setWindowTitle("QWERTTY")
window.setWindowIcon(QIcon('ping-pong.png'))
window.resize(200,200)
window.move(200,100)
window.show()

app.exec()