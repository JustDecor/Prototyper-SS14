import sys

from PySide6.QtWidgets import QApplication, QLabel


def main() -> int:
    app = QApplication(sys.argv)
    label = QLabel("Prototyper-SS14")
    label.resize(320, 120)
    label.show()
    return app.exec()


if __name__ == "__main__":
    raise sys.exit(main())
