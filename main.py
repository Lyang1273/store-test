from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QComboBox, QLineEdit, QCheckBox
from PySide6.QtCore import Qt


class mainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(280, 150)
        self.setFixedSize(800, 500)
        self.setWindowTitle("Store")

        usernameLabel = QLabel("用户名", self)
        usernameLabel.move(55, 30)
        passwordLabel = QLabel("密码", self)
        passwordLabel.move(60, 70)

        usernameEdit = QComboBox(self)
        usernameEdit.addItems(["Lyang1273", "Admin", "User"])
        usernameEdit.setEditable(True)
        usernameEdit.setGeometry(110, 30, 100, 20)
        
        passwordEdit = QLineEdit(self)
        passwordEdit.setGeometry(110, 70, 100, 20)

        license = QCheckBox("我已阅读并同意《用户协议》", self)
        license.setGeometry(20, 110, 200, 20)
        license.stateChanged.connect(self.licenseCheck)

        singinButton = QPushButton("登录", self)
        singinButton.setGeometry(210, 110, 50, 25)
        singinButton.setEnabled(False)  # 初始禁用
        singinButton.clicked.connect(self.handle_login)
        
        self.singinButton = singinButton
        self.license = license
        self.usernameEdit = usernameEdit
        self.passwordEdit = passwordEdit

    def licenseCheck(self, state):
        """当复选框状态改变时调用"""
        # state: 0=未选中, 2=选中 (Qt.CheckState.Unchecked 和 Qt.CheckState.Checked)
        if state == Qt.CheckState.Checked.value:
            self.singinButton.setEnabled(True)
        else:
            self.singinButton.setEnabled(False)
    
    def handle_login(self):
        """处理登录逻辑"""
        username = self.usernameEdit.currentText()
        password = self.passwordEdit.text()
        
        if not username or not password:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "警告", "请输入用户名和密码！")
        else:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.information(self, "成功", f"欢迎，{username}！")
            # 这里可以添加登录成功后的操作


if __name__ == "__main__":
    app = QApplication([])
    window = mainWindows()
    window.show()
    app.exec()