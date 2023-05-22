import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_main_window import Ui_MainWindow
from database import Database


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = Database()
        tasks = self.db.get_tasks()

        for i in range(len(tasks)):
            new_checkbox = QCheckBox()
            new_lable = QLabel()
            new_lable.setText(tasks[i][1])
            self.ui.gl_tasks.addWidget(new_checkbox, i, 0)
            self.ui.gl_tasks.addWidget(new_lable, i, 1)

            # new_lable_2 = QLabel()
            # new_lable_2.setText(str(tasks[i][2]))
            # self.ui.gl_tasks.addWidget(new_lable_2, i, 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
