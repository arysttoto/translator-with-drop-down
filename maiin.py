from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from googletrans import Translator
app = QApplication([])
window = QWidget()
window.setWindowTitle('Translator')
# window.resize(300, 300)
vl = QVBoxLayout()
translator = Translator()

h = QHBoxLayout()
combo1 = QComboBox()
combo1.addItem("English")
combo1.addItem("Russian")
combo2 = QComboBox()
combo2.addItem("English")
combo2.addItem("Russian")
h.addWidget(combo1)
h.addWidget(combo2)


h2 = QHBoxLayout()
text_box = QTextEdit()
translated_box = QTextEdit()
h2.addWidget(text_box)
h2.addWidget(translated_box)

h3 = QHBoxLayout()
trans_btn = QPushButton('Translate!')
h3.addWidget(trans_btn)

vl.addLayout(h)
vl.addLayout(h2)
vl.addLayout(h3)

language = {
    'English': 'en',
    'Russian': 'ru'
}
def set_to_eng():
    text = text_box.toPlainText()
    new_text = translator.translate(text, dest=language[str(combo2.currentText())], src=language[str(combo1.currentText())])
    translated_box.setText(new_text.text)

trans_btn.clicked.connect(set_to_eng)


window.setLayout(vl)
window.show()
app.exec()
