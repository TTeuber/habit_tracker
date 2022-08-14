# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(924, 691)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(200, 0))
        self.sidebar_layout = QVBoxLayout(self.widget)
        self.sidebar_layout.setObjectName(u"sidebar_layout")
        self.habits_select_button = QPushButton(self.widget)
        self.habits_select_button.setObjectName(u"habits_select_button")
        self.habits_select_button.setMinimumSize(QSize(0, 100))

        self.sidebar_layout.addWidget(self.habits_select_button)

        self.charts_select_button = QPushButton(self.widget)
        self.charts_select_button.setObjectName(u"charts_select_button")
        self.charts_select_button.setMinimumSize(QSize(0, 100))

        self.sidebar_layout.addWidget(self.charts_select_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.sidebar_layout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setMinimumSize(QSize(600, 600))
        self.habit_page = QWidget()
        self.habit_page.setObjectName(u"habit_page")
        self.habit_page_layout = QVBoxLayout(self.habit_page)
        self.habit_page_layout.setObjectName(u"habit_page_layout")
        self.label = QLabel(self.habit_page)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(64)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.habit_page_layout.addWidget(self.label)

        self.scrollArea = QScrollArea(self.habit_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scroll_area_widget = QWidget()
        self.scroll_area_widget.setObjectName(u"scroll_area_widget")
        self.scroll_area_widget.setGeometry(QRect(0, 0, 664, 347))
        self.scroll_area_layout = QVBoxLayout(self.scroll_area_widget)
        self.scroll_area_layout.setObjectName(u"scroll_area_layout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.scroll_area_layout.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scroll_area_widget)

        self.habit_page_layout.addWidget(self.scrollArea)

        self.widget_2 = QWidget(self.habit_page)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(200, 200))
        self.item_entry_layout = QHBoxLayout(self.widget_2)
        self.item_entry_layout.setObjectName(u"item_entry_layout")
        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.item_entry_layout.addWidget(self.lineEdit)

        self.new_button = QPushButton(self.widget_2)
        self.new_button.setObjectName(u"new_button")

        self.item_entry_layout.addWidget(self.new_button)


        self.habit_page_layout.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.habit_page)
        self.graph_page = QWidget()
        self.graph_page.setObjectName(u"graph_page")
        self.verticalLayout = QVBoxLayout(self.graph_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(self.graph_page)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.widget_3.setMinimumSize(QSize(0, 100))
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bar_chart_button = QPushButton(self.widget_3)
        self.bar_chart_button.setObjectName(u"bar_chart_button")

        self.horizontalLayout.addWidget(self.bar_chart_button)

        self.line_plot_button = QPushButton(self.widget_3)
        self.line_plot_button.setObjectName(u"line_plot_button")

        self.horizontalLayout.addWidget(self.line_plot_button)


        self.verticalLayout.addWidget(self.widget_3)

        self.graph_stack = QStackedWidget(self.graph_page)
        self.graph_stack.setObjectName(u"graph_stack")
        self.bar_chart_page = QWidget()
        self.bar_chart_page.setObjectName(u"bar_chart_page")
        self.graph_stack.addWidget(self.bar_chart_page)
        self.line_plot_page = QWidget()
        self.line_plot_page.setObjectName(u"line_plot_page")
        self.graph_stack.addWidget(self.line_plot_page)

        self.verticalLayout.addWidget(self.graph_stack)

        self.stackedWidget.addWidget(self.graph_page)

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(1)
        self.graph_stack.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.habits_select_button.setText(QCoreApplication.translate("Form", u"Habits", None))
        self.charts_select_button.setText(QCoreApplication.translate("Form", u"Charts", None))
        self.label.setText(QCoreApplication.translate("Form", u"Habits", None))
        self.new_button.setText(QCoreApplication.translate("Form", u"New", None))
        self.bar_chart_button.setText(QCoreApplication.translate("Form", u"Chart 1", None))
        self.line_plot_button.setText(QCoreApplication.translate("Form", u"Chart 2", None))
    # retranslateUi

