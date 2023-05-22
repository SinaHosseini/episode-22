import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect("todo_list.db")
        self.cursor = self.con.cursor()

    def get_tasks(self):
        query = "SELECT * FROM tasks"
        result = self.cursor.execute(query)
        tasks = result.fetchall()
        return tasks

    def add_new_task(self):
        ...
