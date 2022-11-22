from PyQt6 import QtCore
from PyQt6.QtWidgets import QDialog, QDialogButtonBox

from designer.set_password import Ui_dialogSetPassword
from utils import password_format_valid


class SetPasswordUi(QDialog, Ui_dialogSetPassword):
    password_set = QtCore.pyqtSignal(str)

    def __init__(self):
        super(SetPasswordUi, self).__init__()
        self.setupUi(self)

        self.lineEditPassword.setFocus()
        self.setFixedSize(self.geometry().width(), self.geometry().height())
        self.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setEnabled(False)

        self.buttonBox.accepted.connect(self.emit_password)
        self.lineEditPassword.textChanged.connect(self.enable_ok_button)
        self.lineEditConfirm.textChanged.connect(self.enable_ok_button)

    def enable_ok_button(self):
        enabled = password_format_valid(self.lineEditPassword.text()) and self.lineEditPassword.text() == self.lineEditConfirm.text()
        self.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setEnabled(enabled)

    def emit_password(self):
        self.password_set.emit(self.lineEditPassword.text())
