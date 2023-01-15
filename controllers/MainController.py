import random
import sys

from PyQt5.QtWidgets import QPushButton

from model.model import Model
from views.ButtonMines import ButtonMines
from views.MainWindow import MainWindow
from views.UserLabels import UserLabels


class MainController:
    def __init__(self):
        # model

        self.model = Model()

        # views

        self.mainWindow = MainWindow(self)
        self.userLabels = UserLabels(self)
        self.buttonMines = ButtonMines(self)

    def main(self) -> None:
        # initialize main window
        self.mainWindow.main()

        # initialize user labels
        self.userLabels.select_difficulty()

        # initialize mine buttons
        self.buttonMines.main()

    # listeners

    def check_bomb(self, btn: QPushButton) -> None:
        chance = random.randint(1, 100)

        if chance < self.model.difficulty:
            btn.setIcon(self.model.icon)
            self.userLabels.game_over()
            sys.exit(0)

        else:
            btn.setIcon(self.model.secure_icon)
            btn.setDisabled(True)

    def start_game(self) -> None:
        if self.userLabels.easy_radio.isChecked():
            self.model.difficulty = self.model.easy

        elif self.userLabels.hard_radio.isChecked():
            self.model.difficulty = self.model.hard

        elif self.userLabels.veteran_radio.isChecked():
            self.model.difficulty = self.model.veteran

        # default mode is medium, whatever happens

        else:
            self.model.difficulty = self.model.medium

        self.userLabels.close()
