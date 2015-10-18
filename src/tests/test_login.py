# encoding: utf-8

def test_login_view(qtbot):
    from widgets import LoginDialog
    w = LoginDialog()
    w.show()
    qtbot.addWidget(w)
