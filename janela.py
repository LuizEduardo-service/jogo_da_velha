from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("jogo_da_velha.ui", self)

        #contador para definição do turno
        self.contar_turno = 0

        self.bt1 = self.findChild(QPushButton,'pushButton_1')
        self.bt2 = self.findChild(QPushButton,'pushButton_2')
        self.bt3 = self.findChild(QPushButton,'pushButton_3')
        self.bt4 = self.findChild(QPushButton,'pushButton_4')
        self.bt5 = self.findChild(QPushButton,'pushButton_5')
        self.bt6 = self.findChild(QPushButton,'pushButton_6')
        self.bt7 = self.findChild(QPushButton,'pushButton_7')
        self.bt8 = self.findChild(QPushButton,'pushButton_8')
        self.bt9 = self.findChild(QPushButton,'pushButton_9')
        self.bt_start = self.findChild(QPushButton,'pushButton_10')
        self.lb = self.findChild(QLabel, 'label')

        #ação do botão
        self.bt1.clicked.connect(lambda: self.clicker(self.bt1))
        self.bt2.clicked.connect(lambda: self.clicker(self.bt2))
        self.bt3.clicked.connect(lambda: self.clicker(self.bt3))
        self.bt4.clicked.connect(lambda: self.clicker(self.bt4))
        self.bt5.clicked.connect(lambda: self.clicker(self.bt5))
        self.bt6.clicked.connect(lambda: self.clicker(self.bt6))
        self.bt7.clicked.connect(lambda: self.clicker(self.bt7))
        self.bt8.clicked.connect(lambda: self.clicker(self.bt8))
        self.bt9.clicked.connect(lambda: self.clicker(self.bt9))
        self.bt_start.clicked.connect(self.reset)




        #inicia aplicação
        self.show()

    #verifica combinação
    def verifica_combinacao(self):
        #horizontal
        if self.bt1.text() != '' and self.bt1.text() == self.bt4.text() and self.bt1.text() == self.bt7.text():
            self.vencedor(self.bt1, self.bt4, self.bt7)

        if self.bt2.text() != '' and self.bt2.text() == self.bt5.text() and self.bt2.text() == self.bt8.text():
            self.vencedor(self.bt2, self.bt5, self.bt8)

        if self.bt3.text() != '' and self.bt3.text() == self.bt6.text() and self.bt3.text() == self.bt9.text():
            self.vencedor(self.bt3, self.bt6, self.bt9)

        #vertical
        if self.bt1.text() != '' and self.bt1.text() == self.bt2.text() and self.bt1.text() == self.bt3.text():
            self.vencedor(self.bt1, self.bt2, self.bt3)

        if self.bt4.text() != '' and self.bt4.text() == self.bt5.text() and self.bt4.text() == self.bt6.text():
            self.vencedor(self.bt4, self.bt5, self.bt6)

        if self.bt7.text() != '' and self.bt7.text() == self.bt8.text() and self.bt7.text() == self.bt9.text():
            self.vencedor(self.bt7, self.bt8, self.bt9)

        # diagonal
        if self.bt1.text() != '' and self.bt1.text() == self.bt5.text() and self.bt1.text() == self.bt9.text():
            self.vencedor(self.bt1, self.bt5, self.bt9)

        if self.bt3.text() != '' and self.bt3.text() == self.bt5.text() and self.bt3.text() == self.bt7.text():
            self.vencedor(self.bt3, self.bt5, self.bt7)
        
    #define vencedor
    def vencedor(self, btn1, btn2, btn3):
        btn1.setStyleSheet('QPushButton {color: red; font-size: 70px}')
        btn2.setStyleSheet('QPushButton {color: red; font-size: 70px}')
        btn3.setStyleSheet('QPushButton {color: red; font-size: 70px}')
        self.lb.setText(f'{btn1.text()} é o Vencedor!!')
        self.bloquear_btn()

    def bloquear_btn(self):
        button_list: list = [
            self.bt1,
            self.bt2,
            self.bt3,
            self.bt4,
            self.bt5,
            self.bt6,
            self.bt7,
            self.bt8,
            self.bt9,
        ]

        for btn in button_list:
            btn.setEnabled(False)
    #função clicar
    def clicker(self, btn):
        if self.contar_turno % 2 == 0:
            btn.setText("X")
            btn.setEnabled(False)
            self.lb.setText("Jogada do 'X'")
        else:
            btn.setText("O")
            btn.setEnabled(False)
            self.lb.setText("Jogada do 'O'")

        self.contar_turno += 1
        self.verifica_combinacao()

    def reset(self):
        button_list: list = [
            self.bt1,
            self.bt2,
            self.bt3,
            self.bt4,
            self.bt5,
            self.bt6,
            self.bt7,
            self.bt8,
            self.bt9,
        ]
        self.contar_turno = 0
        self.lb.setText("Vamos começar! Turno do 'X'")
        for button in button_list:
            button.setText("")
            button.setStyleSheet('QPushButton {color: black; font-size: 70px}')
            button.setEnabled(True)
        


#roda aplicação
app = QApplication(sys.argv)
UIWindow  = UI()
app.exec_()