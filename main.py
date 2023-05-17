import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *




class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        self.setStyleSheet("background-color: light gray;")
        self.setWindowTitle("Calculator")
        self.setGeometry(0, 0, 400, 300)

        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_ground = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_null = QHBoxLayout()
        self.hbox_fourth = QHBoxLayout()
        self.hbox_fifth = QHBoxLayout()
        self.hbox_sixth = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_ground)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_null)
        self.vbox.addLayout(self.hbox_fourth)
        self.vbox.addLayout(self.hbox_fifth)
        self.vbox.addLayout(self.hbox_sixth)
        self.vbox.addLayout(self.hbox_result)

        self.input = QLineEdit(self)
        self.input.setText('0')
        self.hbox_input.addWidget(self.input)
        self.input.setReadOnly(True)

        self.op = None
        self.num_1 = 0
        self.num_2 = 0
        self.already_used = 0

        self.b_clear = QPushButton("AC", self)
        self.hbox_ground.addWidget(self.b_clear)
        self.b_clear.setStyleSheet("background-color : red")
        self.b_clear.setFont(QFont('Times New Roman', 14))

        self.b_del = QPushButton("DEL", self)
        self.hbox_ground.addWidget(self.b_del)
        self.b_del.setStyleSheet("background-color : red")
        self.b_del.setFont(QFont('Times New Roman', 14))

        self.b_pow = QPushButton("^", self)
        self.hbox_null.addWidget(self.b_pow)
        self.b_pow.setStyleSheet("background-color : gray")
        self.b_pow.setFont(QFont('Times New Roman', 14))

        self.b_0 = QPushButton("0", self)
        self.hbox_null.addWidget(self.b_0)
        self.b_0.setStyleSheet("background-color : white")
        self.b_0.setFont(QFont('Times New Roman', 14))

        self.b_sqrt = QPushButton("sqrt", self)
        self.hbox_null.addWidget(self.b_sqrt)
        self.b_sqrt.setStyleSheet("background-color : gray")
        self.b_sqrt.setFont(QFont('Times New Roman', 14))

        self.b_1 = QPushButton("1", self)
        self.hbox_third.addWidget(self.b_1)
        self.b_1.setStyleSheet("background-color : white")
        self.b_1.setFont(QFont('Times New Roman', 14))

        self.b_2 = QPushButton("2", self)
        self.hbox_third.addWidget(self.b_2)
        self.b_2.setStyleSheet("background-color : white")
        self.b_2.setFont(QFont('Times New Roman', 14))

        self.b_3 = QPushButton("3", self)
        self.hbox_third.addWidget(self.b_3)
        self.b_3.setStyleSheet("background-color : white")
        self.b_3.setFont(QFont('Times New Roman', 14))

        self.b_4 = QPushButton("4", self)
        self.hbox_second.addWidget(self.b_4)
        self.b_4.setStyleSheet("background-color : white")
        self.b_4.setFont(QFont('Times New Roman', 14))

        self.b_5 = QPushButton("5", self)
        self.hbox_second.addWidget(self.b_5)
        self.b_5.setStyleSheet("background-color : white")
        self.b_5.setFont(QFont('Times New Roman', 14))

        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)
        self.b_6.setStyleSheet("background-color : white")
        self.b_6.setFont(QFont('Times New Roman', 14))

        self.b_7 = QPushButton("7", self)
        self.hbox_first.addWidget(self.b_7)
        self.b_7.setStyleSheet("background-color : white")
        self.b_7.setFont(QFont('Times New Roman', 14))

        self.b_8 = QPushButton("8", self)
        self.hbox_first.addWidget(self.b_8)
        self.b_8.setStyleSheet("background-color : white")
        self.b_8.setFont(QFont('Times New Roman', 14))

        self.b_9 = QPushButton("9", self)
        self.hbox_first.addWidget(self.b_9)
        self.b_9.setStyleSheet("background-color : white")
        self.b_9.setFont(QFont('Times New Roman', 14))

        self.b_plus = QPushButton("+", self)
        self.hbox_fourth.addWidget(self.b_plus)
        self.b_plus.setStyleSheet("background-color : gray")
        self.b_plus.setFont(QFont('Times New Roman', 14))

        self.b_minus = QPushButton("-", self)
        self.hbox_fourth.addWidget(self.b_minus)
        self.b_minus.setStyleSheet("background-color : gray")
        self.b_minus.setFont(QFont('Times New Roman', 14))

        self.b_mult = QPushButton("*", self)
        self.hbox_fourth.addWidget(self.b_mult)
        self.b_mult.setStyleSheet("background-color : gray")
        self.b_mult.setFont(QFont('Times New Roman', 14))

        self.b_div = QPushButton("/", self)
        self.hbox_fourth.addWidget(self.b_div)
        self.b_div.setStyleSheet("background-color : gray")
        self.b_div.setFont(QFont('Times New Roman', 14))

        self.b_perc = QPushButton("%", self)
        self.hbox_fourth.addWidget(self.b_perc)
        self.b_perc.setStyleSheet("background-color : gray")
        self.b_perc.setFont(QFont('Times New Roman', 14))

        self.b_fact = QPushButton("!", self)
        self.hbox_fourth.addWidget(self.b_fact)
        self.b_fact.setStyleSheet("background-color : gray")
        self.b_fact.setFont(QFont('Times New Roman', 14))

        self.b_log = QPushButton("log(x,y)", self)
        self.hbox_fifth.addWidget(self.b_log)
        self.b_log.setStyleSheet("background-color : yellow")
        self.b_log.setFont(QFont('Times New Roman', 14))

        self.b_sin = QPushButton("sin", self)
        self.hbox_fifth.addWidget(self.b_sin)
        self.b_sin.setStyleSheet("background-color : yellow")
        self.b_sin.setFont(QFont('Times New Roman', 14))

        self.b_cos = QPushButton("cos", self)
        self.hbox_fifth.addWidget(self.b_cos)
        self.b_cos.setStyleSheet("background-color : yellow")
        self.b_cos.setFont(QFont('Times New Roman', 14))

        self.b_tg = QPushButton("tg", self)
        self.hbox_fifth.addWidget(self.b_tg)
        self.b_tg.setStyleSheet("background-color : yellow")
        self.b_tg.setFont(QFont('Times New Roman', 14))

        self.b_ctg = QPushButton("ctg", self)
        self.hbox_fifth.addWidget(self.b_ctg)
        self.b_ctg.setStyleSheet("background-color : yellow")
        self.b_ctg.setFont(QFont('Times New Roman', 14))

        self.b_pi = QPushButton("pi", self)
        self.hbox_sixth.addWidget(self.b_pi)
        self.b_pi.setStyleSheet("background-color : gray")
        self.b_pi.setFont(QFont('Times New Roman', 14))

        self.b_e = QPushButton("e", self)
        self.hbox_sixth.addWidget(self.b_e)
        self.b_e.setStyleSheet("background-color : gray")
        self.b_e.setFont(QFont('Times New Roman', 14))

        self.b_decimal = QPushButton(".", self)
        self.hbox_result.addWidget(self.b_decimal)
        self.b_decimal.setStyleSheet("background-color : green")
        self.b_decimal.setFont(QFont('Times New Roman', 14))

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)
        self.b_result.setStyleSheet("background-color : green")
        self.b_result.setFont(QFont('Times New Roman', 14))

        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_mult.clicked.connect(lambda: self._operation("x"))
        self.b_div.clicked.connect(lambda: self._operation("/"))
        self.b_pow.clicked.connect(lambda: self._operation("^"))
        self.b_sqrt.clicked.connect(lambda: self._operation("sqrt"))
        self.b_fact.clicked.connect(lambda: self._operation("!"))
        self.b_perc.clicked.connect(lambda: self._operation("%"))
        self.b_log.clicked.connect(lambda: self._operation("log"))
        self.b_sin.clicked.connect(lambda: self._operation("sin"))
        self.b_cos.clicked.connect(lambda: self._operation("cos"))
        self.b_tg.clicked.connect(lambda: self._operation("tg"))
        self.b_ctg.clicked.connect(lambda: self._operation("ctg"))
        self.b_del.clicked.connect(lambda: self._delete())
        self.b_clear.clicked.connect(lambda: self._ac())
        self.b_decimal.clicked.connect(lambda: self._button("."))
        self.b_result.clicked.connect(self._result)

        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_pi.clicked.connect(lambda: self._button("{}".format(math.pi)))
        self.b_e.clicked.connect(lambda: self._button("{}".format(math.e)))

    def _button(self, param):
        line = self.input.text()
        if line.count('.') > 0 and param == '.':
            self.input.setText(line.lstrip('0'))
        elif line.count('0') > 0:
            self.input.setText(line.lstrip('0') + param)
        else:
            self.input.setText((line + param).lstrip('0'))
        self.already_used = 0

    def _operation(self, op):
        if self.op == None:
            self.num_1 = float(self.input.text())
        self.op = op
        self.input.setText('0')
        self.already_used = 0

    def _delete(self):
        line = self.input.text()
        if len(line) == 1:
            self.input.setText('0')
        else:
            self.input.setText(line[:-1])
        self.already_used = 0

    def _ac(self):
        self.input.setText('0')
        self.op = None
        self.num_1 = None
        self.num_2 = None
        self.already_used = 0

    def _result(self):
        if self.already_used != 1:
            self.num_2 = float(self.input.text())
        if self.op == "+":
            self.input.setText(str(self.num_1 + self.num_2))
        elif self.op == "-":
            self.input.setText(str(self.num_1 - self.num_2))
        elif self.op == "x":
            self.input.setText(str(self.num_1 * self.num_2))
        elif self.op == "%":
            self.num_2 = 1
            self.input.setText(str(self.num_1 * self.num_2 / 100))
        elif self.op == "log":
            if self.num_2 >= 0 and self.num_2 != 1:
                self.input.setText(str(math.log(self.num_1, self.num_2)))
            else:
                self._error()
        elif self.op == "!":
            self.num_2 = 1
            if self.num_1 >= 0:
                self.input.setText(str(math.factorial(self.num_1) * self.num_2))
            else:
                self._error()
        elif self.op == "^":
            self.input.setText(str(math.pow(self.num_1, self.num_2)))
        elif self.op == "sqrt":
            if self.num_2 == 0:
                self.num_2 = 0.5
                if self.num_1 >= 0:
                    self.input.setText(str(math.pow(self.num_1, self.num_2)))
                else:
                    self._error()
            else:
                self.num_1 = 0.5
                if self.num_2 >= 0:
                    self.input.setText(str(math.pow(self.num_2, self.num_1)))
                else:
                    self._error()
        elif self.op == "/":
            if self.num_2 != 0:
                self.input.setText(str(self.num_1 / self.num_2))
            else:
                self._error()
        elif self.op == "sin":
            if self.num_1 != 0:
                self.num_2 = 1
                self.input.setText(str(round(math.sin(self.num_1), 5)))
            else:
                self.num_1 = 1
                self.input.setText(str(round(math.sin(self.num_2), 5)))
        elif self.op == "cos":
            if self.num_1 != 0:
                self.num_2 = 1
                self.input.setText(str(round(math.cos(self.num_1), 5)))
            else:
                self.num_1 = 1
                self.input.setText(str(round(math.cos(self.num_2), 5)))
        elif self.op == "tg":
            if (self.num_1 != 0) and (self.num_1 != math.pi/2) and (self.num_1 != math.pi/2*3) and \
                    (self.num_1 != math.pi/2*5) and (self.num_1 != math.pi/2*7):
                self.num_2 = 1
                self.input.setText(str(round(math.tan(self.num_1), 5)))
            elif (self.num_2 != 0) and (self.num_2 != math.pi/2) and (self.num_2 != math.pi/2*3) and \
                    (self.num_2 != math.pi/2*5) and (self.num_2 != math.pi/2*7):
                self.num_1 = 1
                self.input.setText(str(round(math.tan(self.num_2), 5)))
            else:
                self._error()
        elif self.op == "ctg":
            if (self.num_1 != 0) and (self.num_1 % math.pi != 0):
                self.num_2 = 1
                self.input.setText(str(round(1/math.tan(self.num_1), 5)))
            elif (self.num_2 != 0) and (self.num_2 % math.pi != 0):
                self.num_1 = 1
                self.input.setText(str(round(1/math.tan(self.num_2), 5)))
            else:
                self._error()
        self.already_used = 1
        self.num_1 = float(self.input.text())
        self.op = None

    def _error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText('Введены некорректные значения')
        msg.setWindowTitle("Error")
        msg.exec_()


app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())
