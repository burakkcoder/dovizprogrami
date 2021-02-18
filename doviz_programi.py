import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(342, 217)
        Form.setMouseTracking(False)

        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 0, 160, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)

        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 51))

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 80, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText("Birinci Döviz")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 110, 161, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText("İkinci Döviz")

        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 140, 161, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText("Miktar")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 170, 21))

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(5)
        font.setBold(True)
        font.setWeight(75)

        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        url = "https://www.doviz.com/"

        self.response = requests.get(url)

        self.html_icerik = self.response.content

        self.soup = BeautifulSoup(self.html_icerik, "html.parser")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Döviz Programı"))

        self.pushButton_2.setText(_translate("Form", "Gram Altın"))
        self.pushButton_5.setText(_translate("Form", "Dolar"))
        self.pushButton.setText(_translate("Form", "Euro"))
        self.pushButton_4.setText(_translate("Form", "Gümüş"))
        self.pushButton_3.setText(_translate("Form", "Dolar-Euro-TL Çevirici"))

        self.label.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", "Lütfen Yukarıdaki Alanları Doldurun"))

        self.pushButton_2.clicked.connect(self.gram)
        self.pushButton_5.clicked.connect(self.dolar)
        self.pushButton.clicked.connect(self.euro)
        self.pushButton_4.clicked.connect(self.gumus)
        self.pushButton_3.clicked.connect(self.cevirici)

    def gram(self):
        try:
            gram_altin = self.soup.find_all("span",{"data-socket-key":"gram-altin"})
            eklenenler = []
            for x in gram_altin:
                x = x.text
                x = x.replace(",", ".")
                eklenenler.append(x)
            self.label.setText(eklenenler[0] + " TL")
        except:
            pass

    def dolar(self):
        try:
            dolar = self.soup.find_all("span", {"data-socket-key": "USD"})
            eklenenler = []
            for x in dolar:
                x = x.text
                x = x.replace(",", ".")
                eklenenler.append(x)
            self.label.setText(eklenenler[0] + " TL")
        except:
            pass

    def euro(self):
        try:
            euro = self.soup.find_all("span",{"data-socket-key":"EUR"})
            eklenenler = []
            for x in euro:
                x = x.text
                x = x.replace(",", ".")
                eklenenler.append(x)
            self.label.setText(eklenenler[0] + " TL")
        except:
            pass

    def gumus(self):
        try:
            gumus = self.soup.find_all("span",{"data-socket-key":"gumus"})
            eklenenler = []
            for x in gumus:
                x = x.text
                x = x.replace(",",".")
                eklenenler.append(x)
            self.label.setText(eklenenler[0] + " TL")
        except:
            pass

    def cevirici(self):
        dovizler = []

        dolar = self.soup.find_all("span", {"data-socket-key": "USD"})
        eklenenler = []
        for x in dolar:
            x = x.text
            x = x.replace(",",".")
            eklenenler.append(x)
        eklenenler[0] = float(eklenenler[0])
        dovizler.append(eklenenler[0])

        euro = self.soup.find_all("span",{"data-socket-key":"EUR"})
        eklenenler2 = []
        for x in euro:
            x = x.text
            x = x.replace(",", ".")
            eklenenler2.append(x)
        eklenenler2[0] = float(eklenenler2[0])
        dovizler.append(eklenenler2[0])

        miktar = int(self.lineEdit_3.text())

        try:
            if self.lineEdit.text() == "TL" and self.lineEdit_2.text() == "USD":
                sonuc = miktar / dovizler[0]
                self.label.setText("{:.2f} USD".format(sonuc))
            elif self.lineEdit.text() == "TL" and self.lineEdit_2.text() == "EUR":
                sonuc = miktar / dovizler[1]
                self.label.setText("{:.2f} EUR".format(sonuc))
            elif self.lineEdit.text() == "EUR" and self.lineEdit_2.text() == "TL":
                sonuc = miktar * dovizler[1]
                self.label.setText("{:.2f} TL".format(sonuc))
            elif self.lineEdit.text() == "EUR" and self.lineEdit_2.text() == "USD":
                sonuc = miktar / dovizler[1]
                self.label.setText("{:.2f} USD".format(sonuc))
            elif self.lineEdit.text() == "USD" and self.lineEdit_2.text() == "TL":
                sonuc = miktar * dovizler[0]
                self.label.setText("{:.2f} TL".format(sonuc))
            elif self.lineEdit.text() == "USD" and self.lineEdit_2.text() == "EUR":
                sonuc = miktar / dovizler[0]
                self.label.setText("{:.2f} EUR".format(sonuc))
            else:
                self.label_2.setText("Lütfen Kur Değerlerini Doğru Yazınız.")
        except:
            pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

