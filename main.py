import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from src.uiloader import UIHandler


class OakStore(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_handler = UIHandler()
        self.container = self.ui_handler.load_and_setup(self, "main_window_classic.ui")

        if self.container:
            self.setCentralWidget(self.container)
            # 强制设置一个尺寸，防止窗口缩得太小
            self.resize(800, 600)

            # --- 诊断代码 ---
            if hasattr(self, 'nav_list'):
                print(f"检测到导航栏，共有 {self.nav_list.count()} 个项目")
            else:
                print("错误：UI 已经加载，但没找到名为 'nav_list' 的控件！")

            if hasattr(self, 'content_stack'):
                print(f"检测到内容区，共有 {self.content_stack.count()} 个页面")
            else:
                print("错误：UI 已经加载，但没找到名为 'content_stack' 的控件！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OakStore()
    window.show()
    sys.exit(app.exec())