import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from RinUI.core import RinUIWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    qml_path = Path(__file__).resolve().parent / "main.qml"
    if not qml_path.exists():
        raise FileNotFoundError(qml_path)

    window = RinUIWindow(str(qml_path))
    sys.exit(app.exec())