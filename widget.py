# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QWidget, QCheckBox, QSizePolicy, QHBoxLayout, QPushButton
from interface import Ui_Form
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas


class Chart(FigureCanvas):
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        # three important lines for transparency
        self.figure.patch.set_facecolor("None")
        self.ax.set_facecolor("None")
        self.setStyleSheet("background-color:transparent;")

        self.setParent(parent)

    def make_bar(self):
        self.ax.clear()
        with sqlite3.connect('habit_data.sql') as conn:
            c = conn.cursor()
            b = c.execute("SELECT * FROM Habit_Info")
            d = b.fetchall()
            x = [x[0] for x in d]
            y = [y[1] for y in d]
            self.ax.bar(x, y)
            self.draw()

    def make_line_plot(self):
        self.ax.clear()
        with sqlite3.connect('habit_data.sql') as conn:
            c = conn.cursor()
            b = c.execute("SELECT DISTINCT day, sum(complete) FROM Habits GROUP BY day")
            d = b.fetchall()
            x = [x[0] for x in d]
            y = [y[1] for y in d]
            self.ax.plot(x, y)
            self.draw()


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.new_button = self.ui.new_button
        self.ui.new_button.clicked.connect(lambda: self.add_item(self.ui.lineEdit.text()))

        self.ui.habits_select_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.charts_select_button.clicked.connect(self.chart_select_function)

        self.start()

        self.bar_chart = Chart(self.ui.bar_chart_page)
        self.bar_chart.make_bar()
        self.ui.bar_chart_button.clicked.connect(lambda: self.ui.graph_stack.setCurrentIndex(0))

        self.line_plot = Chart(self.ui.line_plot_page)
        self.line_plot.make_line_plot()
        self.ui.line_plot_button.clicked.connect(lambda: self.ui.graph_stack.setCurrentIndex(1))

    def start(self):
        with sqlite3.connect('habit_data.sql') as conn:
            c = conn.cursor()
            habits = c.execute("SELECT habit FROM Habit_Info")
            for habit in habits.fetchall():
                self.add_habit_widget(habit[0])

    def add_item(self, text):
        if self.ui.lineEdit.text() == '':
            raise Exception("Must have info")
        with sqlite3.connect('habit_data.sql') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO Habit_Info VALUES (?, 0)", (text,))
        self.add_habit_widget(text)

    def add_habit_widget(self, text):
        font = QFont()
        font.setPointSize(48)
        temp_widget = QWidget(self.ui.scroll_area_widget)
        size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(temp_widget.sizePolicy().hasHeightForWidth())
        temp_widget.setSizePolicy(size_policy)
        temp_widget.setMinimumSize(QSize(0, 55))
        temp_horizontal_layout = QHBoxLayout(temp_widget)
        temp_checkbox = QCheckBox(temp_widget)
        temp_checkbox.setFont(font)
        temp_checkbox.setText(text)
        temp_checkbox.stateChanged.connect(lambda: self.update_db(temp_checkbox.text(), temp_checkbox.isChecked()))

        temp_horizontal_layout.addWidget(temp_checkbox)

        temp_button = QPushButton(temp_widget)
        size_policy_2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        size_policy_2.setHorizontalStretch(0)
        size_policy_2.setVerticalStretch(0)
        size_policy_2.setHeightForWidth(temp_button.sizePolicy().hasHeightForWidth())
        temp_button.setSizePolicy(size_policy_2)
        temp_button.setAutoFillBackground(True)
        temp_button.setFlat(True)
        temp_button.setText("X")
        temp_button.clicked.connect(lambda: self.remove_item(temp_widget, temp_checkbox.text()))

        temp_horizontal_layout.addWidget(temp_button)

        count = self.ui.scroll_area_layout.count()

        self.ui.scroll_area_layout.insertWidget(count - 1, temp_widget)

    def remove_item(self, widget, name):
        with sqlite3.connect('habit_data.sql') as conn:
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys = ON")
            c.execute("DELETE FROM Habit_Info WHERE habit=?", (name,))
        widget.close()

    def update_db(self, habit, complete):
        with sqlite3.connect('habit_data.sql') as conn:
            c = conn.cursor()
            c.execute(
                """INSERT OR REPLACE INTO Habits VALUES (date('now'), ?, ?)""", (habit, complete)
            )
            if complete:
                c.execute("UPDATE Habit_Info SET total = (total + 1) WHERE habit = ?", (habit,))
            else:
                c.execute("UPDATE Habit_Info SET total = (total - 1) WHERE habit = ?", (habit,))

    def chart_select_function(self):
        self.bar_chart.make_bar()
        self.line_plot.make_line_plot()
        self.ui.stackedWidget.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication([])
    window = Widget()
    window.show()
    sys.exit(app.exec())
