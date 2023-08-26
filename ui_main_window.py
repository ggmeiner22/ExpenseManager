from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qtpy import QtCore
from add_category import AddCategory
from add_revenue import AddRevenue
from add_expense import AddExpense
from expense_report import Category
from transfer_money import TransferMoney
import matplotlib.pyplot as plt
import io


class UIMainWindow(object):
    def setup_ui(self, main_window):
        main_window.setFixedSize(800, 500)  # sets window size

        # Creates the central widget
        self.central_widget = QWidget(main_window)
        # sets background white
        self.central_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        # Creates a horizontal layout
        self.horizontal_layout_widget = QWidget(self.central_widget)
        self.horizontal_layout_widget.setGeometry(QRect(10, 0, 621, 80))

        # Creates layout for adding and transferring
        self.add_and_transfer_layout = QHBoxLayout(self.horizontal_layout_widget)
        self.add_and_transfer_layout.setContentsMargins(0, 0, 0, 0)

        # Add Category Button
        self.add_category_button = QPushButton(self.horizontal_layout_widget)
        # Opens add category dialog when clicked
        self.add_category_button.clicked.connect(self.open_add_category_dialog)
        # sets color to grey
        self.add_category_button.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        # Adds to add_and_transfer_layout
        self.add_and_transfer_layout.addWidget(self.add_category_button)

        # Add Revenue Button
        self.add_revenue_button = QPushButton(self.horizontal_layout_widget)
        # Opens add revenue dialog when clicked
        self.add_revenue_button.clicked.connect(self.open_add_revenue_dialog)
        # sets color to grey
        self.add_revenue_button.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        # Adds to add_and_transfer_layout
        self.add_and_transfer_layout.addWidget(self.add_revenue_button)

        # Add Expense Button
        self.add_expense_button = QPushButton(self.horizontal_layout_widget)
        # Opens add revenue dialog when clicked
        self.add_expense_button.clicked.connect(self.open_add_expense_dialog)
        # sets color to grey
        self.add_expense_button.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        # Adds to add_and_transfer_layout
        self.add_and_transfer_layout.addWidget(self.add_expense_button)

        # Transfer Money Button
        self.transfer_money_button = QPushButton(self.horizontal_layout_widget)
        # Opens transfer money dialog when clicked
        self.transfer_money_button.clicked.connect(self.open_transfer_money_dialog)
        # sets color to grey
        self.transfer_money_button.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        # Adds to add_and_transfer_layout
        self.add_and_transfer_layout.addWidget(self.transfer_money_button)

        # Creates grid widget and layout for comboBox and information display
        self.grid_layout_widget = QWidget(self.central_widget)
        self.grid_layout_widget.setGeometry(QRect(10, 77, 331, 31))
        self.grid_layout_2 = QGridLayout(self.grid_layout_widget)
        self.grid_layout_2.setContentsMargins(0, 0, 0, 0)

        # Creates Combo Box
        self.category_combo_box = QComboBox(self.grid_layout_widget)
        self.grid_layout_2.addWidget(self.category_combo_box, 0, 0, 1, 1)
        # Updates total and table when index is switched
        self.category_combo_box.currentIndexChanged.connect(self.update_total)

        # Scroll Area Layout
        self.scroll_area = QScrollArea(self.central_widget)
        self.scroll_area.setGeometry(QRect(10, 120, 331, 191))
        self.scroll_area_widget_contents = QWidget()
        self.scroll_area_widget_contents.setGeometry(QRect(0, 0, 329, 189))

        # Table
        self.information_view = QTableWidget(self.scroll_area_widget_contents)
        self.information_view.setGeometry(QRect(0, 0, 331, 192))
        # Sets border to black
        self.information_view.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.scroll_area.setWidget(self.scroll_area_widget_contents)

        # Exit Button
        self.exit_button = QPushButton(self.central_widget)
        self.exit_button.setGeometry(QRect(692, 430, 100, 31))
        # sets color to grey
        self.exit_button.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        # Closes main window when clicked
        self.exit_button.clicked.connect(main_window.close)

        # Creates grid widget and layout for display of total of an account
        self.grid_layout_widget_2 = QWidget(self.central_widget)
        self.grid_layout_widget_2.setGeometry(QRect(10, 330, 111, 41))
        self.total_layout = QGridLayout(self.grid_layout_widget_2)
        self.total_layout.setContentsMargins(0, 0, 0, 0)

        # Total Label
        self.total_label = QLabel(self.grid_layout_widget_2)
        font = QFont()
        # Sets font to size 13
        font.setPointSize(13)
        self.total_label.setFont(font)
        self.total_layout.addWidget(self.total_label, 0, 0, 1, 1)

        # Box to display total
        self.display_total = QLineEdit(self.central_widget)
        # Sets border to black
        self.display_total.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.display_total.setGeometry(QRect(210, 330, 132, 41))

        # Line across bottom
        self.line = QFrame(self.central_widget)
        self.line.setGeometry(QRect(10, 400, 771, 16))
        # Sets line to black
        self.line.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        # Creates layout and widget to hold pie chart
        self.grid_layout_widget_3 = QWidget(self.central_widget)
        self.grid_layout_widget_3.setGeometry(QRect(360, 80, 421, 281))
        self.graph_layout = QGridLayout(self.grid_layout_widget_3)
        self.graph_layout.setContentsMargins(0, 0, 0, 0)

        # Pie Chart
        self.pie_chart_area = QLabel(self.grid_layout_widget_3)
        # Sets background to white
        self.pie_chart_area.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.graph_layout.addWidget(self.pie_chart_area, 0, 0, 1, 1)
        # Creates memory object
        self.buffer = io.BytesIO()

        # Completes GUI setup
        main_window.setCentralWidget(self.central_widget)
        self.menu_bar = QMenuBar(main_window)
        self.menu_bar.setGeometry(QRect(0, 0, 800, 26))
        main_window.setMenuBar(self.menu_bar)
        self.status_bar = QStatusBar(main_window)
        main_window.setStatusBar(self.status_bar)

        # Adds button names to screen, labels, and sets window title
        self.retranslate_ui(main_window)

        # List of categories
        self.category_list = []

    # Adds button names to screen, labels, and sets window title
    def retranslate_ui(self, main_window):
        main_window.setWindowTitle("Expense Manager")
        self.add_category_button.setText("Add Category")
        self.add_revenue_button.setText("Add Revenue")
        self.add_expense_button.setText("Add Expense")
        self.transfer_money_button.setText("Transfer Money")
        self.exit_button.setText("Exit")
        self.total_label.setText("Total")

    # opens dialog for AddCategory and adds new category to the dropdown
    def open_add_category_dialog(self):
        dialog = AddCategory(self.category_list)
        # If fields are accepted
        if dialog.exec_() == QDialog.Accepted:
            text = dialog.get_new_category()  # get the text from the QLineEdit
            new_category = Category(text)  # Creates a category object
            self.category_list.append(new_category)  # adds new category object to list
            self.category_combo_box.addItem(new_category.category)  # adds object to comboBox
            self.update_total()  # Updates total as a base 0 for the category if in dropdown

    # Adds revenue to the selected Dialog
    def open_add_revenue_dialog(self):
        dialog = AddRevenue(self.category_list)
        # If fields are accepted
        if dialog.exec_() == QDialog.Accepted:
            # Fields to show
            category_text = dialog.get_category()
            amount = dialog.get_amount()
            description = dialog.get_description()
            # Add to object
            category = self.get_category(category_text)  # finds the object with the name equal to sending_category
            category.add_revenue(int(amount), description)  # Adds the revenue
            self.update_total()  # Updates the total box

    def open_add_expense_dialog(self):
        dialog = AddExpense(self.category_list)
        # If fields are accepted
        if dialog.exec_() == QDialog.Accepted:
            # Fields to show
            category_text = dialog.get_category()
            amount = dialog.get_amount()
            description = dialog.get_description()
            # Add to object
            category = self.get_category(category_text)  # finds the object with the name equal to sending_category
            category.add_expense(int(amount), description)  # Adds the expense
            self.update_total()  # Updates the total box

    def open_transfer_money_dialog(self):
        dialog = TransferMoney(self.category_list)
        # If fields are accepted
        if dialog.exec_() == QDialog.Accepted:
            # Fields to show
            sending_category = dialog.get_sending_category()
            receiving_category = dialog.get_receiving_category()
            amount = dialog.get_amount()
            # Add to object
            # finds the object with the name equal to sending_category
            sending_category_object = self.get_category(sending_category)
            # finds the object with the name equal to sending_category
            receiving_category_object = self.get_category(receiving_category)
            sending_category_object.transfer_money(int(amount), receiving_category_object)  # Transfers Money
            self.update_total()  # Updates the total box

    # Updates the total box
    def update_total(self):
        # Gets current text from the dropdown menu
        category_text = self.category_combo_box.currentText()
        # gets the object of the text
        category = self.get_category(category_text)
        # Displays text on the QLineEdit box
        self.display_total.setText(str(f'{category.get_balance():.2f}'))
        # Updates the accounts
        self.update_account(category)

    # Updates the accounts
    def update_account(self, category):
        # Clears the table
        self.information_view.clear()
        # Adds necessary rows
        self.information_view.setRowCount(len(category.wallet))
        # Adds necessary columns
        self.information_view.setColumnCount(2)
        # Sets header labels
        self.information_view.setHorizontalHeaderLabels(['Item', 'Price'])
        # Stretches columns to fill space
        self.information_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        row = 0  # Index
        # Adds each transaction to the table
        for transaction in category.wallet:
            item_value = QTableWidgetItem(transaction['description'][:23])
            price_value = QTableWidgetItem(str(f"{transaction['amount']:.2f}"))
            self.information_view.setItem(row, 0, item_value)
            self.information_view.setItem(row, 1, price_value)
            row = row + 1
        # Updates pie chart graph
        self.update_graph()

    # Updates Pie-chart graph
    def update_graph(self):
        counts, categories = self.get_counts_and_categories()
        self.buffer.seek(0)  # Gets the first index
        self.buffer.truncate()  # Clears buffer
        if sum(counts) > 0 and len(counts) > 0: # Checks for data to graph
            plt.figure(figsize=(8, 8)) # Creates plot size
            img, ax = plt.subplots()
            # Creates graph
            ax.pie(counts,
                   labels=categories,
                   startangle=-110,
                   shadow=False,
                   autopct="%1.2f%%", labeldistance=1.05)
            plt.title("Spending Percentage")
            img.savefig(self.buffer, format='JPEG') # Saves to memory

            # Adds graph to GUI
            pixmap = QPixmap()
            pixmap.loadFromData(self.buffer.getvalue())
            pixmap = pixmap.scaled(self.pie_chart_area.size(), aspectRatioMode=True,
                                   transformMode=QtCore.Qt.SmoothTransformation)
            self.pie_chart_area.setPixmap(pixmap)

    # Returns the total amount of spending in all accounts
    def get_counts_and_categories(self):
        counts = []
        categories = []
        for category in self.category_list:
            for transaction in category.wallet:
                if transaction['amount'] < 0:
                    if category.category in categories:
                        index = categories.index(category.category)
                        counts[index] = counts[index] + (transaction['amount'] * -1)
                    else:
                        counts.append(transaction['amount'] * -1)
                        categories.append(category.category)
        return counts, categories

    # Gets category of a text
    def get_category(self, category_text):
        for category in self.category_list:
            if category.category == category_text:
                return category
        return None # If no category exists
