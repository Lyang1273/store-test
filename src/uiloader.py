import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QObject, QIODevice
from PySide6.QtWidgets import QMainWindow, QWidget

class UIHandler(QObject):
    def __init__(self):
        super().__init__()
        self.loader = QUiLoader()
        # 获取项目根目录 (store-test)
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def load_and_setup(self, main_instance, ui_filename):
        """
        加载指定的 UI 文件并绑定导航逻辑
        :param ui_filename: 如 "main_window_classic.ui"
        """
        ui_path = os.path.join(self.base_dir, "ui_pages", ui_filename)
        file = QFile(ui_path)
        if not file.open(QIODevice.ReadOnly):
            print(f"[错误] 找不到文件: {ui_path}")
            return None

        # 加载 UI 窗口对象（不传 parent，让 loader 建立原始层次）
        ui_obj = self.loader.load(file)
        file.close()

        if ui_obj is None:
            print(f"[错误] UI 加载失败: {ui_path}")
            return None

        # 如果顶层是 QMainWindow，则提取其 centralwidget 作为容器
        container = ui_obj
        if isinstance(ui_obj, QMainWindow):
            central = ui_obj.findChild(QWidget, "centralwidget")
            if central is not None:
                # 重新父级，不必显示原来的 QMainWindow
                central.setParent(main_instance)
                container = central
            else:
                print("[警告] 加载的 QMainWindow 中未找到名为 'centralwidget' 的控件，使用整个 UI 对象作为容器。")

        # 1. 自动化映射：将 UI 里的控件（如 nav_list）直接变成 main_instance 的属性
        for widget in container.findChildren(QObject):
            name = widget.objectName()
            if name:
                setattr(main_instance, name, widget)

        # 2. 绑定核心联动逻辑
        if hasattr(main_instance, 'nav_list') and hasattr(main_instance, 'content_stack'):
            # 连接：左侧行号改变 -> 右侧页面索引改变
            main_instance.nav_list.currentRowChanged.connect(
                main_instance.content_stack.setCurrentIndex
            )
            # 默认启动时选中第一行
            main_instance.nav_list.setCurrentRow(0)

        return container
