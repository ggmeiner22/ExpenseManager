from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QDialog, QLabel, QFrame, QLineEdit, QPushButton, QGridLayout, QWidget, QMessageBox


class AddCategory(QDialog):
    def __init__(self, categories):
        super(AddCategory, self).__init__()
        self.setWindowTitle('Expense Manager: Add Category')
        self.setFixedSize(600, 310)
        self.categories_names = [category.category for category in categories]
        self.home()

    # Creates the buttons on the window and executes their commands
    def home(self):
        
        # Label at top
        self.header = QLabel(self)
        self.header.setGeometry(QRect(10, 10, 101, 16))
        self.header.setText("Add Category")

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

        # Adds Label
        self.category_label = QLabel(self.grid_layout_widget)
        self.grid_layout.addWidget(self.category_label, 0, 0, 1, 1)
        self.category_label.setText("Category")

        # The category added
        self.enter_category = QLineEdit(self.grid_layout_widget)
        self.grid_layout.addWidget(self.enter_category, 0, 1, 1, 1)
        
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
        if self.enter_category.text() not in self.categories_names:
            self.accept()
        else:
            show_msg = QMessageBox(QMessageBox.Critical,
                                   'Error',
                                   "Sorry, that category already exists!",
                                   QMessageBox.Ok)
            show_msg.exec_()

    def get_new_category(self):
        text = self.enter_category.text()
        return text.strip()

