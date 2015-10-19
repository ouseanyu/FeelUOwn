# -*- coding:utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from interfaces import ControllerApi, View
from constants import WINDOW_ICON

from base.player import Player
from base.network_manger import NetworkManager

from widgets.webview import WebView

from widgets.lyric import LyricWidget
from widgets.desktop_mini import DesktopMiniLayer
from widgets.notify import NotifyWidget


class Controller(QWidget):

    ui = None

    def __init__(self, parent=None):
        super().__init__(parent)

        self.webview = WebView()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.webview)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        ControllerApi.player = Player()
        ControllerApi.desktop_mini = DesktopMiniLayer()
        ControllerApi.lyric_widget = LyricWidget()
        ControllerApi.notify_widget = NotifyWidget()

        ControllerApi.network_manager = NetworkManager()

        self._switch_mode_shortcut = QShortcut(QKeySequence(Qt.Key_Escape), self)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_MacShowFocusRect, False)
        self.setWindowIcon(QIcon(WINDOW_ICON))
        self.setWindowTitle('FeelUOwn')
        self.resize(960, 580)
        self.setLayout(self.layout)

    def paintEvent(self, event):
        option = QStyleOption()
        option.initFrom(self)
        painter = QPainter(self)
        painter.setCompositionMode(QPainter.CompositionMode_Clear)
        painter.fillRect(self.rect(), Qt.transparent)
        painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
        style = self.style()
        style.drawPrimitive(QStyle.PE_Widget, option, painter, self)
