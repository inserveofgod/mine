from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox, QFormLayout, QRadioButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QPushButton


class UserLabels(QDialog):
    def __init__(self, controller):
        super(UserLabels, self).__init__()
        self.controller = controller
        self.model = self.controller.model

        self.mainLayout = QVBoxLayout()
        self.textLayout = QHBoxLayout()
        self.formLayout = QFormLayout()

        self.label = QLabel("Lütfen bir zorluk derecesi seçiniz.")
        self.easy_radio = QRadioButton("Kolay")
        self.medium_radio = QRadioButton("Orta")
        self.hard_radio = QRadioButton("Zor")
        self.veteran_radio = QRadioButton("Emekli Asker")
        self.confirm_btn = QPushButton("Oyuna Başla")

        self._set_ui()
        self._listeners()

    def _set_ui(self) -> None:
        self.mainLayout.addLayout(self.textLayout)
        self.mainLayout.addLayout(self.formLayout)

        self.setWindowTitle(self.model.title)
        self.setWindowIcon(self.model.icon)
        self.setLayout(self.mainLayout)
        self.setModal(True)

        self.medium_radio.setChecked(True)

    def _listeners(self) -> None:
        self.confirm_btn.clicked.connect(self.controller.start_game)

    def select_difficulty(self) -> None:
        label_font = self.label.font()
        label_font.setPointSize(15)
        label_font.setBold(True)
        self.label.setFont(label_font)
        self.label.setStyleSheet("padding-bottom: 15px")
        self.textLayout.addWidget(self.label, alignment=Qt.AlignCenter)

        self.formLayout.addRow(self.easy_radio)
        self.formLayout.addRow(self.medium_radio)
        self.formLayout.addRow(self.hard_radio)
        self.formLayout.addRow(self.veteran_radio)
        self.formLayout.addWidget(self.confirm_btn)
        self.show()

    def game_over(self) -> None:
        QMessageBox.critical(self, self.model.title, "Bom!!! Patladınız !!!", QMessageBox.Ok)
