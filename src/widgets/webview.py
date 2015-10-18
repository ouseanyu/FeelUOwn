# -*- coding: utf8 -*-
import json

from PyQt5.QtCore import *
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtWebKit import QWebSettings

from interfaces import ControllerApi
from constants import MODE, PUBLIC_PATH, DEBUG, HTML_PATH

from base.logger import LOG
from base.utils import func_coroutine


class ExposeToJs(QObject):
    def __init__(self):
        super().__init__()

    @pyqtSlot(str, str, bool, result=str)
    @pyqtSlot(str, str, result=str)
    def login(self, username, password, phone=False):
        data = ControllerApi.api.login(username, password, phone)
        if data['code'] is 200:
            ControllerApi.set_login()
        return json.dumps(data)

    @pyqtSlot(int, result=str)
    def captcha_url(self, captcha_id):
        return ControllerApi.api.get_captcha_url(captcha_id)

    @pyqtSlot(int, str, result=int)
    @pyqtSlot(int, str, result=str)
    def confirm_captcha(self, captcha_id, captcha):
        return ControllerApi.api.confirm_captcha(captcha_id, captchar)

    @pyqtSlot(result=str)
    def get_user_playlists(self):
        playlists = ControllerApi.api.get_user_playlist()
        if playlists is not None:
            data = {}
            data['result'] = playlists
            LOG.info("Get User playlists Success")
            return json.dumps(data)
        LOG.warning("Get User Playlists Failed")
        return None

    @pyqtSlot(result=int)
    def get_user_id(self):
        return ControllerApi.api.uid

    @pyqtSlot(int, bool, result=str)
    @pyqtSlot(int, result=str)
    def get_playlist(self, pid, use_cache=True):
        data = ControllerApi.api.get_playlist_detail(pid, use_cache)
        if data is not None:
            result = dict()
            result['result'] = data
            LOG.info("Get Playlist OK")
            return json.dumps(result)
        LOG.warning("Get Playlist FAIL")
        return data


class WebView(QWebView):
    """这个类的实例可能发出的信号。（也就是说，controller只能绑定这些信号，
    其他信号尽量不要绑定）
    loadProgress(int)
    """
    signal_play = pyqtSignal([int])
    signal_play_songs = pyqtSignal([list])
    signal_search_artist = pyqtSignal([int])
    signal_search_album = pyqtSignal([int])
    signal_play_mv = pyqtSignal([int])

    def __init__(self, parent=None):
        super().__init__(parent)

        self.init()
        self.expose_to_js = ExposeToJs()
        self.js_queue = []  # 保存页面load完，要执行的js代码

        self.load_htmlfile('index.html')

    def init(self):
        self.init_singal_binding()
        if MODE == DEBUG:
            self.settings().setAttribute(QWebSettings.DeveloperExtrasEnabled, True)
        else:
            self.setContextMenuPolicy(Qt.NoContextMenu)

    def init_singal_binding(self):
        self.loadFinished.connect(self.on_load_finished)
        self.linkClicked.connect(self.on_link_clicked)

    def load_css(self):
        all_css = QFileInfo(PUBLIC_PATH + 'all.css').absoluteFilePath()
        self.settings().setUserStyleSheetUrl(QUrl.fromLocalFile(all_css))

    @pyqtSlot(QUrl)
    def on_link_clicked(self, url):
        return False

    @pyqtSlot()
    def on_load_finished(self):
        self.page().mainFrame().addToJavaScriptWindowObject(
            'python', self.expose_to_js)
        for js_code in self.js_queue:
            self.page().mainFrame().evaluateJavaScript(js_code)
        self.js_queue.clear()

    """给js调用的函数, 需要加上pyqtSlot装饰器
    """
    @pyqtSlot(int)
    def play(self, mid):
        """
        """
        LOG.debug("play music: the music_id is " + str(mid))
        self.signal_play.emit(mid)

    @pyqtSlot(int)
    def play_mv(self, mvid):
        LOG.debug("play mv: the mv_id is " + str(mvid))
        self.signal_play_mv.emit(mvid)

    @pyqtSlot(str)
    def play_songs(self, songs_str):
        LOG.debug("play songs")
        songs = json.loads(songs_str)
        tracks = songs['tracks']
        self.signal_play_songs.emit(tracks)

    def search_artist(self, aid):
        LOG.debug("search artist info, the artist id is: " + str(aid))
        self.signal_search_artist.emit(aid)

    @pyqtSlot(int)
    def search_album(self, aid):
        LOG.debug("search album info, the album id is: " + str(aid))
        self.signal_search_album.emit(aid)

    """下面都是给controller调用的函数，最好不要在其他地方调用
    """

    def load_htmlfile(self, filename):
        path = QFileInfo(HTML_PATH + filename).absoluteFilePath()
        self.load(QUrl.fromLocalFile(path))

    def load_search_result(self, songs):
        data = json.dumps(songs)
        path = QFileInfo(HTML_PATH + 'search.html').absoluteFilePath()
        js_code = 'window.fill_search(%s)' % data
        self.js_queue.append(js_code)
        self.load(QUrl.fromLocalFile(path))
