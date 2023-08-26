from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QFrame, QWidget, QGridLayout, QComboBox, QLineEdit, QTextEdit, \
    QMessageBox


class AddRevenue(QDialog):
    def __init__(self, categories):
        super(AddRevenue, self).__init__()
        self.setWindowTitle('Expense Manager: Add Revenue')
        self.setFixedSize(600, 310)
        self.categories_names = [category.category for category in categories]
        self.home()

    # Creates the buttons on the window and executes their commands
    def home(self):
        # Label at top
        self.header = QLabel(self)
        self.header.setGeometry(QRect(10, 10, 101, 16))
        self.header.setText(QCoreApplication.translate("Dialog", u"Add Revenue", None))

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
        self.to_label = QLabel(self.grid_layout_widget)
        self.grid_layout.addWidget(self.to_label, 0, 0, 1, 1)
        self.to_label.setText("To")

        # Account to be affected
        self.to_box = QComboBox(self.grid_layout_widget)
        self.to_box.addItems(self.categories_names)
        self.grid_layout.addWidget(self.to_box, 0, 1, 1, 1)

        # Adds middle label
        self.enter_amount_label = QLabel(self.grid_layout_widget)
        self.grid_layout.addWidget(self.enter_amount_label, 1, 0, 1, 1)
        self.enter_amount_label.setText("Amount")

        # Amount to affect account
        self.enter_amount = QLineEdit(self.grid_layout_widget)
        self.grid_layout.addWidget(self.enter_amount, 1, 1, 1, 1)

        # Adds bottom Label
        self.description_label = QLabel(self.grid_layout_widget)
        self.grid_layout.addWidget(self.description_label, 2, 0, 1, 1)
        self.description_label.setText("Description")

        # Description
        self.description = QTextEdit(self.grid_layout_widget)
        self.grid_layout.addWidget(self.description, 2, 1, 1, 1)

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
        try:
            category = self.get_category()
            amount = self.get_amount()
            description = self.get_description()
            if description != "" and int(amount) > 0 and category != "":
                show_msg = QMessageBox(QMessageBox.Information,
                                       'Success',
                                       "Thank you! A record was added to the database successfully!",
                                       QMessageBox.Ok)
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


    def get_category(self):
        text = self.to_box.currentText()
        return text.strip()

    def get_amount(self):
        text = self.enter_amount.text()
        return text.strip()

    def get_description(self):
        text = self.description.toPlainText()
        return text.strip()


