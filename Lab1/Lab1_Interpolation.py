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
    R = 255
    G = 0
    B = 0

    C = 0
    M = 50
    Y = 23
    K = 42

    okClicked = False
    my_signal = pyqtSignal(int, int, int, bool)  # signal OK ou Cancel
    my_signal_2 = pyqtSignal(int, int, int, int, bool)  # signal OK ou Cancel
    # ^ Lines Added

    def setupUi(self, Lab1_Interpolation, current_r, current_g, current_b, current_c, current_m, current_y, current_k ):
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

        # CMYK
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 321, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.C_Slider = QtWidgets.QSlider(self.layoutWidget)
        self.C_Slider.setStyleSheet("selection-background-color: rgb(85, 255, 0);")
        self.C_Slider.setMaximum(100)
        self.C_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.C_Slider.setObjectName("C_Slider")
        self.horizontalLayout_5.addWidget(self.C_Slider)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(20, 0))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 40, 321, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.M_Slider = QtWidgets.QSlider(self.layoutWidget_2)
        self.M_Slider.setStyleSheet("selection-background-color: rgb(85, 255, 0);")
        self.M_Slider.setMaximum(100)
        self.M_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.M_Slider.setObjectName("M_Slider")
        self.horizontalLayout_6.addWidget(self.M_Slider)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(20, 0))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 70, 321, 24))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.Y_Slider = QtWidgets.QSlider(self.layoutWidget_3)
        self.Y_Slider.setStyleSheet("selection-background-color: rgb(85, 255, 0);")
        self.Y_Slider.setMaximum(100)
        self.Y_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Y_Slider.setObjectName("Y_Slider_4")
        self.horizontalLayout_7.addWidget(self.Y_Slider)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(20, 0))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.layoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_4.setGeometry(QtCore.QRect(0, 93, 321, 31))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.K_Slider = QtWidgets.QSlider(self.layoutWidget_4)
        self.K_Slider.setStyleSheet("selection-background-color: rgb(85, 255, 0);")
        self.K_Slider.setMaximum(100)
        self.K_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.K_Slider.setObjectName("K_Slider_5")
        self.horizontalLayout_8.addWidget(self.K_Slider)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(20, 0))
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_8.addWidget(self.label_14)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget_5 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 10, 311, 24))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_9.addWidget(self.label_15)
        self.H_Slider_2 = QtWidgets.QSlider(self.layoutWidget_5)
        self.H_Slider_2.setStyleSheet("selection-background-color: rgb(85, 255, 0);")
        self.H_Slider_2.setMaximum(255)
        self.H_Slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.H_Slider_2.setObjectName("H_Slider_2")
        self.horizontalLayout_9.addWidget(self.H_Slider_2)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QtCore.QSize(20, 0))
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_9.addWidget(self.label_16)
        self.layoutWidget_6 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_6.setGeometry(QtCore.QRect(10, 50, 311, 24))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_10.addWidget(self.label_17)
        self.S_Slider_3 = QtWidgets.QSlider(self.layoutWidget_6)
        self.S_Slider_3.setStyleSheet("selection-background-color: rgb(85, 255, 0);")
        self.S_Slider_3.setMaximum(255)
        self.S_Slider_3.setOrientation(QtCore.Qt.Horizontal)
        self.S_Slider_3.setObjectName("S_Slider_3")
        self.horizontalLayout_10.addWidget(self.S_Slider_3)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QtCore.QSize(20, 0))
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_10.addWidget(self.label_18)
        self.layoutWidget_7 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_7.setGeometry(QtCore.QRect(10, 90, 311, 24))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_7)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_11.addWidget(self.label_19)
        self.V_Slider_4 = QtWidgets.QSlider(self.layoutWidget_7)
        self.V_Slider_4.setStyleSheet("selection-background-color: rgb(85, 255, 0);")
        self.V_Slider_4.setMaximum(255)
        self.V_Slider_4.setOrientation(QtCore.Qt.Horizontal)
        self.V_Slider_4.setObjectName("V_Slider_4")
        self.horizontalLayout_11.addWidget(self.V_Slider_4)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMinimumSize(QtCore.QSize(20, 0))
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_11.addWidget(self.label_20)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.layoutWidget_8 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget_8.setGeometry(QtCore.QRect(10, 10, 311, 24))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_8)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_12.addWidget(self.label_21)
        self.L_Slider_2 = QtWidgets.QSlider(self.layoutWidget_8)
        self.L_Slider_2.setStyleSheet("selection-background-color: rgb(85, 255, 0);")
        self.L_Slider_2.setMaximum(255)
        self.L_Slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.L_Slider_2.setObjectName("L_Slider_2")
        self.horizontalLayout_12.addWidget(self.L_Slider_2)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QtCore.QSize(20, 0))
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_12.addWidget(self.label_22)
        self.layoutWidget_9 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget_9.setGeometry(QtCore.QRect(10, 50, 311, 24))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_23 = QtWidgets.QLabel(self.layoutWidget_9)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_13.addWidget(self.label_23)
        self.A_Slider_3 = QtWidgets.QSlider(self.layoutWidget_9)
        self.A_Slider_3.setStyleSheet("selection-background-color: rgb(85, 255, 0);")
        self.A_Slider_3.setMaximum(255)
        self.A_Slider_3.setOrientation(QtCore.Qt.Horizontal)
        self.A_Slider_3.setObjectName("A_Slider_3")
        self.horizontalLayout_13.addWidget(self.A_Slider_3)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMinimumSize(QtCore.QSize(20, 0))
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_13.addWidget(self.label_24)
        self.layoutWidget_10 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget_10.setGeometry(QtCore.QRect(10, 90, 311, 24))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_25 = QtWidgets.QLabel(self.layoutWidget_10)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_14.addWidget(self.label_25)
        self.B_Slider_LAB = QtWidgets.QSlider(self.layoutWidget_10)
        self.B_Slider_LAB.setStyleSheet("selection-background-color: rgb(85, 255, 0);")
        self.B_Slider_LAB.setMaximum(255)
        self.B_Slider_LAB.setOrientation(QtCore.Qt.Horizontal)
        self.B_Slider_LAB.setObjectName("B_Slider_LAB")
        self.horizontalLayout_14.addWidget(self.B_Slider_LAB)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMinimumSize(QtCore.QSize(20, 0))
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_14.addWidget(self.label_26)
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
        # Lines Added
        self.R_Slider.valueChanged['int'].connect(self.label_4.setNum)
        self.G_Slider.valueChanged['int'].connect(self.label_5.setNum)
        self.B_Slider.valueChanged['int'].connect(self.label_6.setNum)


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

        # CMYK
        self.C_Slider.valueChanged['int'].connect(self.label_8.setNum)
        self.M_Slider.valueChanged['int'].connect(self.label_10.setNum)
        self.Y_Slider.valueChanged['int'].connect(self.label_12.setNum)
        self.K_Slider.valueChanged['int'].connect(self.label_14.setNum)

        self.C_Slider.setValue(current_c)
        self.M_Slider.setValue(current_m)
        self.Y_Slider.setValue(current_y)
        self.K_Slider.setValue(current_k)

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

    def slider_C_ValueChanged(self):
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
                background_b[j, i] = [new_blue, self.C_Slider.value(), self.R_Slider.value(), 255]
                background_g[j, i] = [self.C_Slider.value(), new_green, self.R_Slider.value(), 255]

        cv2.imwrite('b_slider_background.jpg', background_b)
        cv2.imwrite('g_slider_background.jpg', background_g)
        self.G_Slider.setStyleSheet("QSlider {background-image: url(g_slider_background.jpg);}")
        self.B_Slider.setStyleSheet("QSlider {background-image: url(b_slider_background.jpg);}")

    def Button_clicked(self, b):
        if b.text() == "OK": self.okClicked = True

        # RGB
        if self.tabWidget.currentIndex() == 0:
            self.R = self.R_Slider.value()
            self.G = self.G_Slider.value()
            self.B = self.B_Slider.value()
            self.my_signal.emit(self.R, self.G, self.B, self.okClicked)

        # CMYK
        if self.tabWidget.currentIndex() == 1:
            self.C = self.C_Slider.value()
            self.M = self.M_Slider.value()
            self.Y = self.Y_Slider.value()
            self.K = self.K_Slider.value()
            self.my_signal_2.emit(self.C, self.M, self.Y, self.K, self.okClicked)

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
        self.label_7.setText(_translate("Lab1_Interpolation", "C"))
        self.label_8.setText(_translate("Lab1_Interpolation", "0"))
        self.label_9.setText(_translate("Lab1_Interpolation", "M"))
        self.label_10.setText(_translate("Lab1_Interpolation", "0"))
        self.label_11.setText(_translate("Lab1_Interpolation", "Y"))
        self.label_12.setText(_translate("Lab1_Interpolation", "0"))
        self.label_13.setText(_translate("Lab1_Interpolation", "K"))
        self.label_14.setText(_translate("Lab1_Interpolation", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Lab1_Interpolation", "CMYK"))
        self.label_15.setText(_translate("Lab1_Interpolation", "H"))
        self.label_16.setText(_translate("Lab1_Interpolation", "0"))
        self.label_17.setText(_translate("Lab1_Interpolation", "S"))
        self.label_18.setText(_translate("Lab1_Interpolation", "0"))
        self.label_19.setText(_translate("Lab1_Interpolation", "V"))
        self.label_20.setText(_translate("Lab1_Interpolation", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Lab1_Interpolation", "HSV"))
        self.label_21.setText(_translate("Lab1_Interpolation", "L"))
        self.label_22.setText(_translate("Lab1_Interpolation", "0"))
        self.label_23.setText(_translate("Lab1_Interpolation", "a"))
        self.label_24.setText(_translate("Lab1_Interpolation", "0"))
        self.label_25.setText(_translate("Lab1_Interpolation", "b"))
        self.label_26.setText(_translate("Lab1_Interpolation", "0"))
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
