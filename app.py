import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView
)
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt


class PortfolioApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crypto Portfolio")
        self.setGeometry(100, 100, 702, 782)
        self.setStyleSheet("background-color: #111; color: white;")

        self.init_ui()

    def init_ui(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(28, 28, 28, 28)  # Устанавливает отступы: слева, сверху, справа, снизу

        test_number = 23453 # Здесь будет баланс

        # Balance widget
        balance_widget = QWidget()
        balance_layout = QHBoxLayout()

        # это все надпись про баланс да
        balance_widget.setFixedSize(402, 186)  # Устанавливает фиксированный размер
        balance_widget.setStyleSheet("background-color: #a020f0;  border-radius: 15px;")
        

        balance_label = QLabel(f"Current balance: ") 
        balance_label.setStyleSheet("""
            QLabel {
                color: white;
                border-radius: 10px;
                font-size: 20px;
                max-width: 180px;
                max-height: 20px;   
                font-weight: bold;
                padding: 5px;   
            }
        """)
           
    
        balance_number = QLabel(f"{test_number}$")  # Здесь будет баланс
        balance_number.setStyleSheet("""
            QLabel {
                color: white;
                border: 2px solid #d78aff;
                border-radius: 10px;
                font-size: 25px;   
                font-weight: bold;
            }
        """)

        balance_label.adjustSize()
        balance_number.adjustSize()
        balance_layout.setContentsMargins(20, 20, 0, 0)  
        balance_layout.setSpacing(0)
        
        balance_layout.addWidget(balance_label, alignment=Qt.AlignLeft | Qt.AlignTop)
        balance_layout.addWidget(balance_number, alignment=Qt.AlignLeft | Qt.AlignTop)


        info_label = QLabel("Total invested: 3100.43$\nTotal Profit: 59.43$\nRealised Profit: 239.64$")
        info_label.setStyleSheet("color: white;")
        # balance_layout.addWidget(info_label, alignment=Qt.AlignLeft | Qt.AlignBottom)
        
        # balance_layout.addWidget(balance_label)
        # balance_layout.addStretch()
        # balance_layout.addWidget(info_label)
        balance_widget.setLayout(balance_layout)

        # Buttons
        button_layout = QHBoxLayout()
        for text in ["History", "Add new", "Notification"]:
            btn = QPushButton(text)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #d78aff;
                    color: white;
                    border-radius: 10px;
                    padding: 10px 20px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #e0b3ff;
                }
            """)
            button_layout.addWidget(btn)
        button_layout.addStretch()

        # Table
        table = QTableWidget()
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(["Name", "Invested", "Buy Price", "Price", "Amount", "PnL"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setStyleSheet("""
            QTableWidget {
                background-color: #222;
                color: white;
                gridline-color: #444;
            }
            QHeaderView::section {
                background-color: #333;
                color: white;
                font-weight: bold;
            }
        """)

        # Sample data
        data = [
            ("ddd", "$2003.14", "$2003.14", "$2003.14", "$2003.14", "0.1892"),
            ("BTC", "$64561", "$64561", "$64561", "$64561", "0.0013"),
            ("USDT", "$1.0011", "$1.0011", "$1.0011", "$1.0011", "249.73"),
            ("VIA", "$3.56", "$3.56", "$3.56", "$3.56", "1043.2"),
        ]
        table.setRowCount(len(data))
        for row, (name, *values) in enumerate(data):
            table.setItem(row, 0, QTableWidgetItem(name))
            for col, val in enumerate(values, start=1):
                table.setItem(row, col, QTableWidgetItem(val))

        # Assemble
        main_layout.addWidget(balance_widget)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(table)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
#dfhsdfs#

app = QApplication(sys.argv)
window = PortfolioApp()
window.show()
sys.exit(app.exec_())
