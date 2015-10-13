#! /usr/bin/env python3
# -*- coding:utf8 -*-


import sys
import os
import asyncio

path = sys.path[0]
os.chdir(path)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from constants import LOGFILE, MODE, DEBUG, WINDOW_ICON

from controllers import Controller
from quamash import QEventLoop


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    app.setWindowIcon(QIcon(WINDOW_ICON))
    app.setApplicationName("FeelUOwn")
    app.setApplicationVersion("v3.1.0")

    app_event_loop = QEventLoop(app)
    asyncio.set_event_loop(app_event_loop)

    if MODE != DEBUG:
        f_handler = open(LOGFILE, 'w')
        sys.stdout = f_handler
        sys.stderr = f_handler

    w = Controller()
    w.move((QApplication.desktop().width() - w.width())/2, (QApplication.desktop().height() - w.height())/2)
    w.show()

    app_event_loop.run_forever()

    sys.exit()
