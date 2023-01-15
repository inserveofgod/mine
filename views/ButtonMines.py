from PyQt5.QtWidgets import QPushButton, QGridLayout
from functools import partial


class ButtonMines:
    def __init__(self, controller):
        self.controller = controller
        self.count = 9
        self.win = self.controller.mainWindow
        self.model = self.controller.model
        self.buttonsLayout = QGridLayout()

        self._buttons()

    def _buttons(self) -> None:
        for row in range(self.count):
            for col in range(self.count):
                btn = QPushButton()
                btn.setIcon(self.model.btn_icon)
                btn.setFixedSize(self.model.btn_width, self.model.btn_height)
                btn.clicked.connect(partial(self.controller.check_bomb, btn))
                self.buttonsLayout.addWidget(btn, row, col)

    def main(self) -> None:
        self.win.mainFrame.setLayout(self.buttonsLayout)
