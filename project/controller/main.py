#!/usr/bin/python3
# coding: utf-8


from PyQt5.QtWidgets import QApplication

import sys

from project.view.window import Window


if __name__ == "__main__":
    port = sys.argv[1]

    app = QApplication(sys.argv)
    window = Window(port)
    window.show()
    app.exec_()
