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
        self.read_from_database()

        self.ui.btn_new_task.clicked.connect(self.new_task)

    def new_task(self):
        new_tittle = self.ui.tb_new_task.text()
        new_description = self.ui.tb_new_task_dec.toPlainText()
        feedback = self.db.add_new_task(new_tittle, new_description)
        if feedback == True:
            self.read_from_database()
            self.ui.tb_new_task.setText("")
            self.ui.tb_new_task_dec.setText("")

        else:
            msg_box = QMessageBox()
            msg_box.setText("There is a problem")
            msg_box.exec()

    def read_from_database(self):
        tasks = self.db.get_tasks()

        for i in range(len(tasks)):
            new_checkbox = QCheckBox()
            new_label = QLabel()
            new_btn = QPushButton()


            new_label.setText(tasks[i][1])
            new_btn.setText("❌")

            self.ui.gl_tasks.addWidget(new_checkbox, i, 0)
            self.ui.gl_tasks.addWidget(new_label, i, 1)
            self.ui.gl_tasks.addWidget(new_btn, i, 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
