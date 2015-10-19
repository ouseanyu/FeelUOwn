# -*- coding: utf-8 -*-

import os
import json

from base.logger import LOG
from base.utils import func_coroutine
from constants import DATA_PATH
from interfaces import ControllerApi, View

from .normalize import NetEaseAPI

netease_normalize = NetEaseAPI()


def init():
    """init plugin """

    LOG.info("NetEase Plugin init")

    ControllerApi.api = netease_normalize

    if os.path.exists(DATA_PATH + netease_normalize.user_info_filename):
        with open(DATA_PATH + netease_normalize.user_info_filename) as f:
            data = f.read()
            data_dict = json.loads(data)
            uid = data_dict.get('uid')
            if uid is not None:
                LOG.info("Find Availabel User Data")
                netease_normalize.uid = uid
                js_code = "window.setLogin(%s)" % json.dumps(data_dict)
                View.webview.run_js(js_code)

    if os.path.exists(DATA_PATH + netease_normalize.ne.cookies_filename):
        @func_coroutine
        def check_cookies():
            netease_normalize.ne.load_cookies()
            if netease_normalize.check_login_successful():
                ControllerApi.set_login()
        check_cookies()
    else:
        LOG.info("找不到您的cookies文件，请您手动登录")
