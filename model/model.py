import os

from PyQt5.QtGui import QIcon


class Model:
    def __init__(self):
        self.root = os.getcwd()

        self.encoding = "UTF-8"
        self.title = "Mayın"
        self.icon = QIcon(os.path.join(self.root, "./assets/img/bomb.png"))
        self.btn_width = 32
        self.btn_height = 32
        self.btn_icon = QIcon(os.path.join(self.root, "./assets/img/radioactivity.png"))
        self.secure_icon = QIcon(os.path.join(self.root, "./assets/img/shield.png"))

        self.easy = 10
        self.medium = 30
        self.hard = 60
        self.veteran = 90
        self.difficulty = self.medium
