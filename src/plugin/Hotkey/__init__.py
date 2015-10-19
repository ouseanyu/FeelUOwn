# -*- coding:utf-8 -*-

import sys
import asyncio
from _thread import start_new_thread

from base.logger import LOG
from interfaces import ControllerApi


def init():

    LOG.info("Global Hotkey Plugin Init")

    if sys.platform == "darwin":
        from .mac import run_event_loop
        player = ControllerApi.player
        app_event_loop = asyncio.get_event_loop()
        app_event_loop.call_later(1, run_event_loop, player)
    elif sys.platform.lower() == "linux":
        from .linux import KeyEventLoop
        event = KeyEventLoop(ControllerApi.player)
        start_new_thread(event.run, ())
