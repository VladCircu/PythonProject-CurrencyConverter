import data as d
import converter
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot



class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.currency = 'RON'
        self.currency2 = 'RON'
        combo = QComboBox(self)
        combo2 = QComboBox(self)
        combo.addItem('RON')
        combo2.addItem('RON') 
        for x in d.data():
            combo.addItem(x)
            print(x)
        for x in d.data():
            combo2.addItem(x)
            print(x)

        combo.move(50, 25)
        combo.currentTextChanged.connect(self.onComboChanged)
        # global c1
        # c1 = combo.currentText()
        # x = str(combo.currentText())
        combo2.move(500,25)
        combo2.currentTextChanged.connect(self.onCombo2Changed)
        # text2 = str(combo2.currentText())

        self.textbox = QLineEdit(self)
        self.textbox.move(150, 25)
        self.textbox.resize(100,30)

        self.button = QPushButton('Convert to:', self)
        self.button.move(300,25)
        self.button.clicked.connect(self.on_click)
        self.show()

        self.qlabel = QLabel(self)
        # self.qlabel.move(50,25)

        # combo.activated[str].connect(self.onChanged)      

        self.setGeometry(50,50,800,100)
        self.setWindowTitle("Currency converter")
        self.show()
        # self.uiComboBox.view().pressed.connect(self.handleItemPressed)
        # self.combo.currentTextChanged.connect(self.on_combobox_changed)

    def onComboChanged(self, text):
        print("current change: " + text)
        self.currency = text
        return text
    
    # def currentcombo(self, index):
    #     print(self.combo.itemData(index).toString())

    def onCombo2Changed(self, text):
        print("current change: " + text)
        self.currency2 = text
        return text


    def on_click(self):
        textboxValue = self.textbox.text()
        # text = str(self.combo.currentText())
        print(self.currency)
        print(self.currency2)
        new = float(converter.convert(self.currency,textboxValue,self.currency2))
        QMessageBox.question(self, 'Done!', "Exchanged Value is :  " + str(new), QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
    
    

    # def on_combobox_changed(self, value):
    #     print("combobox changed", value)
    # # do your code
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

# print(combo1)