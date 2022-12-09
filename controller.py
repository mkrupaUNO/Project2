from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow, QLineEdit):
    """
    Class to control the application.
    """
    def __init__(self, *args, **kwargs):
        """
        Function to set up the application and its processes
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_clear.clicked.connect(lambda: self.clear_label())
        self.button_change_sign.clicked.connect(lambda: self.change_sign())
        self.button_percentage.clicked.connect(lambda: self.percentage())
        self.button_divide.clicked.connect(lambda: self.divide())
        self.button_multipy.clicked.connect(lambda: self.multiply())
        self.button_subtract.clicked.connect(lambda: self.subtract())
        self.button_add.clicked.connect(lambda: self.add())
        self.button_equal.clicked.connect(lambda: self.equal())
        self.button_decimal.clicked.connect(lambda: self.decimal())
        self.button_0.clicked.connect(lambda: self.zero())
        self.button_1.clicked.connect(lambda: self.one())
        self.button_2.clicked.connect(lambda: self.two())
        self.button_3.clicked.connect(lambda: self.three())
        self.button_4.clicked.connect(lambda: self.four())
        self.button_5.clicked.connect(lambda: self.five())
        self.button_6.clicked.connect(lambda: self.six())
        self.button_7.clicked.connect(lambda: self.seven())
        self.button_8.clicked.connect(lambda: self.eight())
        self.button_9.clicked.connect(lambda: self.nine())

        self.number_one = ''
        self.number_two = ''
        self.number_active = 'one'
        self.operation = ''
        self.label_output.setText('0')

    def clear_label(self):
        """
        Function to clear the output label when the C button is pressed
        """
        self.number_one = ''
        self.number_two = ''
        self.number_active = 'one'
        self.label_output.setText('0')

    def change_sign(self):
        """
        Function to change the sign if the value is not error when the change sign button is pressed
        """
        if self.number_one != 'Error':
            if self.number_active == 'one':
                if self.number_one == '':
                    self.number_one = '-'
                elif self.number_one[0] == '-':
                    self.number_one = self.number_one[1:]
                else:
                    self.number_one = '-' + self.number_one
            else:
                if self.number_two == '':
                    self.number_two = '-'
                elif self.number_two[0] == '-':
                    self.number_two = self.number_two[1:]
                else:
                    self.number_two = '-' + self.number_two
            self.update_label()

    def percentage(self):
        """
        Function that runs when the percentage button is pressed, and it moves the decimal place over 2 to the left
        """
        if self.number_one != 'Error' and self.number_two != '':
            if self.number_one != '-' and self.number_two != '-':
                if self.number_active == 'one':
                    self.number_one = str(float(self.number_one) * 100)
                else:
                    self.number_two = str(float(self.number_two) * 100)
                self.update_label()

    def divide(self):
        """
        Function that runs when the division button is pressed, and it sets the operation to division and allows user to
        enter the second number
        """
        if self.number_active == 'one':
            self.operation = 'division'
            self.number_active = 'two'
            self.label_output.setText('0')
        elif self.number_active == 'two':
            self.equal()
            self.operation = 'division'
            self.number_active = 'two'
            self.label_output.setText('0')

    def multiply(self):
        """
        Function that runs when the multiplication button is pressed, and it sets the operation to multiplication and
        allows user to enter the second number
        """
        if self.number_one != 'Error':
            if self.number_active == 'one':
                self.operation = 'multiplication'
                self.number_active = 'two'
                self.label_output.setText('0')
            elif self.number_active == 'two':
                self.equal()
                self.operation = 'multiplication'
                self.number_active = 'two'
                self.label_output.setText('0')

    def subtract(self):
        """
        Function that runs when the subtraction button is pressed, and it sets the operation to subtraction and allows
        user to enter the second number
        """
        if self.number_one != 'Error':
            if self.number_active == 'one':
                self.operation = 'subtraction'
                self.number_active = 'two'
                self.label_output.setText('0')
            elif self.number_active == 'two':
                self.equal()
                self.operation = 'subtraction'
                self.number_active = 'two'
                self.label_output.setText('0')

    def add(self):
        """
        Function that runs when the addition button is pressed, and it sets the operation to addition and allows user to
        enter the second number
        """
        if self.number_one != 'Error':
            if self.number_active == 'one':
                self.operation = 'addition'
                self.number_active = 'two'
                self.label_output.setText('0')
            elif self.number_active == 'two':
                self.equal()
                self.operation = 'addition'
                self.number_active = 'two'
                self.label_output.setText('0')

    def equal(self):
        """
        Function that runs when the equal button is pressed, and it runs when the values are numbers and not error
        It equates the numbers based on the operation selected before
        """
        if self.number_one != 'Error' and self.number_two != '':
            if self.number_one != '-' and self.number_two != '-':
                if self.operation == 'addition':
                    self.number_one = str(float(self.number_one) + float(self.number_two))
                elif self.operation == 'subtraction':
                    self.number_one = str(float(self.number_one) - float(self.number_two))
                elif self.operation == 'multiplication':
                    self.number_one = str(float(self.number_one) * float(self.number_two))
                elif self.operation == 'division':
                    if float(self.number_two) != 0.0:
                        self.number_one = str(float(self.number_one) / float(self.number_two))
                    else:
                        self.number_one = 'Error'
                self.number_active = 'one'
                self.number_two = ''
                self.update_label()

    def decimal(self):
        """
        Function that runs when the decimal button is pressed, and it adds a decimal to the end of the number only if
        there isn't one already.
        """
        if self.number_one != 'Error':
            if self.number_active == 'one':
                if '.' not in self.number_one:
                    self.number_one += '.'
            else:
                if '.' not in self.number_two:
                    self.number_two += '.'
            self.update_label()

    def zero(self):
        """
        Function that runs when the zero button is pressed, and it adds a zero to the end of the number
        """
        if self.number_one != 'Error':
            if self.number_active == 'one':
                self.number_one += '0'
            else:
                self.number_two += '0'
            self.update_label()

    def one(self):
        """
        Function that runs when the one button is pressed, and it adds a one to the end of the number
        """
        if self.number_one != 'Error':
            if self.number_active == 'one':
                self.number_one += '1'
            else:
                self.number_two += '1'
            self.update_label()

    def two(self):
        """
        Function that runs when the two button is pressed, and it adds a two to the end of the number
        """
        if self.number_one != 'Error':
            if self.number_active == 'one':
                self.number_one += '2'
            else:
                self.number_two += '2'
            self.update_label()

    def three(self):
        """
        Function that runs when the three button is pressed, and it adds a three to the end of the number
        """
        if self.number_one != 'Error':
            if self.number_active == 'one':
                self.number_one += '3'
            else:
                self.number_two += '3'
            self.update_label()

    def four(self):
        """
        Function that runs when the four button is pressed, and it adds a four to the end of the number
        """
        if self.number_one != 'Error':
            if self.number_active == 'one':
                self.number_one += '4'
            else:
                self.number_two += '4'
            self.update_label()

    def five(self):
        """
        Function that runs when the five button is pressed, and it adds a five to the end of the number
        """
        if self.number_one != 'Error':
            if self.number_active == 'one':
                self.number_one += '5'
            else:
                self.number_two += '5'
            self.update_label()

    def six(self):
        """
        Function that runs when the six button is pressed, and it adds a six to the end of the number
        """
        if self.number_one != 'Error':
            if self.number_active == 'one':
                self.number_one += '6'
            else:
                self.number_two += '6'
            self.update_label()

    def seven(self):
        """
        Function that runs when the seven button is pressed, and it adds a seven to the end of the number
        """
        if self.number_one != 'Error':
            if self.number_active == 'one':
                self.number_one += '7'
            else:
                self.number_two += '7'
            self.update_label()

    def eight(self):
        """
        Function that runs when the eight button is pressed, and it adds an eight to the end of the number
        """
        if self.number_one != 'Error':
            if self.number_active == 'one':
                self.number_one += '8'
            else:
                self.number_two += '8'
            self.update_label()

    def nine(self):
        """
        Function that runs when the nine button is pressed, and it adds a nine to the end of the number
        """
        if self.number_one != 'Error':
            if self.number_active == 'one':
                self.number_one += '9'
            else:
                self.number_two += '9'
            self.update_label()

    def update_label(self):
        """
        Function to update label
        """
        if self.number_active == 'one':
            self.label_output.setText(self.number_one[:9])
        else:
            self.label_output.setText(self.number_two[:9])
