# -*- coding:utf8 -*-

"""
common settings

FUTURE:  read setting from a json file
"""


"""
path configuration
"""
ICON_PATH = '../icons/'
CACHE_PATH = '../cache/'
DATA_PATH = '../data/'


"""
mode configuration
"""
DEBUG = True   # 1 for debug
PRODUCTION = False  # 0 for Production Environment
LOGFILE = CACHE_PATH + 'error.log'
MODE = DEBUG


"""
web_assets configuration
"""
HTML_PATH = 'web/'
PUBLIC_PATH = 'web/public/'

"""
icon name
"""
WINDOW_ICON = ICON_PATH + 'FeelUOwn.png'
