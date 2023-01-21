# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lab1_Interpolation.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QThread


class Ui_Lab1_Interpolation(QThread):
    # Lines Added
    R = 0
    G = 0
    B = 0
    okClicked = False
    my_signal = pyqtSignal(int, int, int, bool)  # signal OK ou Cancel
    # ^ Lines Added

    def setupUi(self, Lab1_Interpolation, current_r, current_g, current_b):
        Lab1_Interpolation.setObjectName("Lab1_Interpolation")
        Lab1_Interpolation.resize(350, 220)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Lab1_Interpolation.sizePolicy().hasHeightForWidth())
        Lab1_Interpolation.setSizePolicy(sizePolicy)
        Lab1_Interpolation.setMinimumSize(QtCore.QSize(350, 220))
        Lab1_Interpolation.setMaximumSize(QtCore.QSize(350, 220))
        self.centralwidget = QtWidgets.QWidget(Lab1_Interpolation)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.R_Slider = QtWidgets.QSlider(self.tab)
        self.R_Slider.setStyleSheet("selection-background-color: rgb(85, 255, 0);")
        self.R_Slider.setMaximum(255)
        self.R_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.R_Slider.setObjectName("R_Slider")
        self.horizontalLayout_2.addWidget(self.R_Slider)
        self.label_4 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(20, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.G_Slider = QtWidgets.QSlider(self.tab)
        self.G_Slider.setMaximum(255)
        self.G_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.G_Slider.setObjectName("G_Slider")
        self.horizontalLayout_3.addWidget(self.G_Slider)
        self.label_5 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(20, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.B_Slider = QtWidgets.QSlider(self.tab)
        self.B_Slider.setMaximum(255)
        self.B_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.B_Slider.setObjectName("B_Slider")
        self.horizontalLayout_4.addWidget(self.B_Slider)
        self.label_6 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(20, 0))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.OK_Button = QtWidgets.QPushButton(self.centralwidget)
        self.OK_Button.setObjectName("OK_Button")
        self.horizontalLayout.addWidget(self.OK_Button)
        self.Cancel_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Cancel_Button.setObjectName("Cancel_Button")
        self.horizontalLayout.addWidget(self.Cancel_Button)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        Lab1_Interpolation.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Lab1_Interpolation)
        self.statusbar.setObjectName("statusbar")
        Lab1_Interpolation.setStatusBar(self.statusbar)

        # Lines Added
        self.OK_Button.clicked.connect(lambda: self.Button_clicked(self.OK_Button))
        self.Cancel_Button.clicked.connect(lambda: self.Button_clicked(self.Cancel_Button))
        # ^ Lines Added

        self.retranslateUi(Lab1_Interpolation)
        self.tabWidget.setCurrentIndex(0)
        self.R_Slider.valueChanged['int'].connect(self.label_4.setNum)
        self.G_Slider.valueChanged['int'].connect(self.label_5.setNum)
        self.B_Slider.valueChanged['int'].connect(self.label_6.setNum)

        # Lines Added
        self.R_Slider.valueChanged['int'].connect(self.slider_R_ValueChanged)
        self.G_Slider.valueChanged['int'].connect(self.slider_G_ValueChanged)
        self.B_Slider.valueChanged['int'].connect(self.slider_B_ValueChanged)
        self.R_Slider.setValue(current_r)
        self.G_Slider.setValue(current_g)
        self.B_Slider.setValue(current_b)

        self.slider_R_ValueChanged()
        self.slider_B_ValueChanged()
        self.slider_G_ValueChanged()
        # ^ Lines Added

        QtCore.QMetaObject.connectSlotsByName(Lab1_Interpolation)

    def slider_R_ValueChanged(self):
        # update green
        # update blue
        background_b = np.zeros((22, 267, 4), dtype="uint8")
        background_g = np.zeros((22, 267, 4), dtype="uint8")
        width = 267
        height = 22

        for i in range(width):
            new_green = int((i / width) * 255)
            new_blue = int((i / width) * 255)

            for j in range(height):
                background_b[j, i] = [new_blue, self.G_Slider.value(), self.R_Slider.value(), 255]
                background_g[j, i] = [self.B_Slider.value(), new_green, self.R_Slider.value(), 255]

        cv2.imwrite('b_slider_background.jpg', background_b)
        cv2.imwrite('g_slider_background.jpg', background_g)
        self.G_Slider.setStyleSheet("QSlider {background-image: url(g_slider_background.jpg);}")
        self.B_Slider.setStyleSheet("QSlider {background-image: url(b_slider_background.jpg);}")

    def slider_G_ValueChanged(self):
        # update red
        # update blue
        background_b = np.zeros((22, 267, 4), dtype="uint8")
        background_r = np.zeros((22, 267, 4), dtype="uint8")
        width = 267
        height = 22

        for i in range(width):
            new_red = int((i / width) * 255)
            new_blue = int((i / width) * 255)

            for j in range(height):
                background_b[j, i] = [new_blue, self.G_Slider.value(), self.R_Slider.value(), 255]
                background_r[j, i] = [self.B_Slider.value(), self.G_Slider.value(), new_red, 255]

        cv2.imwrite('b_slider_background.jpg', background_b)
        cv2.imwrite('r_slider_background.jpg', background_r)
        self.R_Slider.setStyleSheet("QSlider {background-image: url(r_slider_background.jpg);}")
        self.B_Slider.setStyleSheet("QSlider {background-image: url(b_slider_background.jpg);}")

    def slider_B_ValueChanged(self):
        background_g = np.zeros((22, 267, 4), dtype="uint8")
        background_r = np.zeros((22, 267, 4), dtype="uint8")
        width = 267
        height = 22

        for i in range(width):
            new_red = int((i / width) * 255)
            new_green = int((i / width) * 255)

            for j in range(height):
                background_g[j, i] = [self.B_Slider.value(), new_green, self.R_Slider.value(), 255]
                background_r[j, i] = [self.B_Slider.value(), self.G_Slider.value(), new_red, 255]

        cv2.imwrite('g_slider_background.jpg', background_g)
        cv2.imwrite('r_slider_background.jpg', background_r)
        self.R_Slider.setStyleSheet("QSlider {background-image: url(r_slider_background.jpg);}")
        self.G_Slider.setStyleSheet("QSlider {background-image: url(g_slider_background.jpg);}")

    def Button_clicked(self, b):
        if b.text() == "OK": self.okClicked = True
        self.R = self.R_Slider.value()
        self.G = self.G_Slider.value()
        self.B = self.B_Slider.value()
        self.my_signal.emit(self.R, self.G, self.B, self.okClicked)

    def retranslateUi(self, Lab1_Interpolation):
        _translate = QtCore.QCoreApplication.translate
        Lab1_Interpolation.setWindowTitle(_translate("Lab1_Interpolation", "Color Interpolation"))
        self.label.setText(_translate("Lab1_Interpolation", "R"))
        self.label_4.setText(_translate("Lab1_Interpolation", "0"))
        self.label_2.setText(_translate("Lab1_Interpolation", "G"))
        self.label_5.setText(_translate("Lab1_Interpolation", "0"))
        self.label_3.setText(_translate("Lab1_Interpolation", "B"))
        self.label_6.setText(_translate("Lab1_Interpolation", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Lab1_Interpolation", "RGB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Lab1_Interpolation", "CMYK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Lab1_Interpolation", "HSV"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Lab1_Interpolation", "Lab"))
        self.OK_Button.setText(_translate("Lab1_Interpolation", "OK"))
        self.Cancel_Button.setText(_translate("Lab1_Interpolation", "Cancel"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Lab1_Interpolation = QtWidgets.QMainWindow()
    ui = Ui_Lab1_Interpolation()
    ui.setupUi(Lab1_Interpolation)
    Lab1_Interpolation.show()
    sys.exit(app.exec_())
