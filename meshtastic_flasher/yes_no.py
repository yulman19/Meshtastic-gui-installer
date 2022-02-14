"""YesNo confirmation box"""

from PySide6 import QtCore
from PySide6.QtWidgets import QMessageBox, QDialog

class YesNo(QMessageBox):
    """Custom yes no dialog to allow for key press Y and N"""

    def __init__(self, parent=None, message=None):
        """constructor"""
        super(YesNo, self).__init__(parent)

        self.setWindowTitle("Question")
        self.setText(message)
        self.setIcon(QMessageBox.Question)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.exec()

    def keyPressEvent(self, event):
        """Deal with a key press"""
        super(YesNo, self).keyPressEvent(event)
        if event.key() == QtCore.Qt.Key_Y:
            self.setResult(QDialog.Accepted)
            self.close()
        if event.key() in [QtCore.Qt.Key_N, QtCore.Qt.Key_Escape]:
            self.setResult(QDialog.Rejected)
            self.close()
