from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QFrame, QWidget, QGridLayout, QComboBox, QLineEdit, \
    QMessageBox


class TransferMoney(QDialog):
    def __init__(self, categories):
        super(TransferMoney, self).__init__()
        self.setWindowTitle('Expense Manager: Transfer Money')
        self.setFixedSize(600, 310)
        self.categories_object_list = categories
        self.categories_names = [category.category for category in categories]
        self.home()

    # Creates the buttons on the window and executes their commands
    def home(self):
        # Label at top
        self.header = QLabel(self)
        self.header.setGeometry(QRect(10, 10, 101, 16))
        self.header.setText(QCoreApplication.translate("Dialog", u"Transfer Money", None))

        # Line across top
        self.top_line = QFrame(self)
        self.top_line.setGeometry(QRect(10, 30, 580, 16))
        self.top_line.setFrameShape(QFrame.HLine)
        self.top_line.setFrameShadow(QFrame.Sunken)

        # Creates Grid Layout Widget and layout for center with margins
        self.grid_layout_widget = QWidget(self)
        self.grid_layout_widget.setGeometry(QRect(19, 69, 401, 161))
        self.grid_layout = QGridLayout(self.grid_layout_widget)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)

        # Adds Top label
        self.from_label = QLabel(self.grid_layout_widget)
        self.grid_layout.addWidget(self.from_label, 0, 0, 1, 1)
        self.from_label.setText("From")

        # The account the money is being taken from
        self.from_box = QComboBox(self.grid_layout_widget)
        self.from_box.addItems(self.categories_names)
        self.grid_layout.addWidget(self.from_box, 0, 1, 1, 1)

        # Adds middle label
        self.to_label = QLabel(self.grid_layout_widget)
        self.grid_layout.addWidget(self.to_label, 1, 0, 1, 1)
        self.to_label.setText("To")

        # The account the money is being moved to
        self.to_box = QComboBox(self.grid_layout_widget)
        self.to_box.addItems(self.categories_names)
        self.grid_layout.addWidget(self.to_box, 1, 1, 1, 1)

        # Adds bottom Label
        self.amount_label = QLabel(self.grid_layout_widget)
        self.grid_layout.addWidget(self.amount_label, 2, 0, 1, 1)
        self.amount_label.setText("Amount")

        # The amount of money moved
        self.enter_amount = QLineEdit(self.grid_layout_widget)
        self.grid_layout.addWidget(self.enter_amount, 2, 1, 1, 1)

        # Line across Bottom
        self.bottom_line = QFrame(self)
        self.bottom_line.setGeometry(QRect(10, 250, 580, 16))
        self.bottom_line.setFrameShape(QFrame.HLine)
        self.bottom_line.setFrameShadow(QFrame.Sunken)

        # Cancel Button
        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.move(500, 270)
        self.cancel_button.clicked.connect(self.reject)

        # Submit Button
        self.submit_button = QPushButton('Submit', self)
        self.submit_button.move(400, 270)
        self.submit_button.clicked.connect(self.show_msg_box)

    def show_msg_box(self):
        amount = self.get_amount()
        sender = self.get_sending_category()
        receiver = self.get_receiving_category()
        try:
            if sender != receiver and int(amount) <= self.get_category_object(sender).get_balance():
                amount = f'{int(amount):.2f}'
                show_msg = QMessageBox(QMessageBox.Information, 'Success', "$" + amount +
                                   " transferred successfully from " + sender.lower()
                                   + ' to ' + receiver.lower(), QMessageBox.Ok)
                show_msg.exec_()
                self.accept()
            else:
                self.show_error()
        except Exception as e:
            print(e)
            self.show_error()

    def show_error(self):
       show_msg = QMessageBox(QMessageBox.Critical,
                                'Error',
                                "Sorry, an error occurred while processing your request",
                                QMessageBox.Ok)
       show_msg.exec_()

    def get_sending_category(self):
        text = self.from_box.currentText()
        return text.strip()

    def get_receiving_category(self):
        text = self.to_box.currentText()
        return text.strip()

    def get_amount(self):
        text = self.enter_amount.text()
        return text.strip()

    # Gets category
    def get_category_object(self, category_text):
        for category in self.categories_object_list:
            if category.category == category_text:
                return category