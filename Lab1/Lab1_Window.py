# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lab1_Window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from PyQt5.QtGui import QPixmap
import cv2
import numpy as np
from PyQt5.QtWidgets import QFileDialog, QComboBox

from Lab1.Lab1_Interpolation import Ui_Lab1_Interpolation

def addDisc(self):
    # créer une image transparente comme intermédiaire juste pour l'affichage des formes
    img_height, img_width = self.label_2.height(), self.label_2.width()
    n_channels = 4
    image = np.zeros((img_height - 2, img_width - 2, n_channels), dtype="uint8")
    # paramètres du cercle
    center_coordinates = (int(img_width/2), int(img_height/2))
    radius = int(img_height/2) - 120 #ne doit pas dépasser min(img_height, img_width)/2
    #valeurs initiales des couleurs R G B
    color = (self.R, self.G, self.B, 255) #r g b alpha
    thickness = -1  #remplir la forme géométrique par la couleur
    cv2.circle(image, center_coordinates, radius, color, thickness)

    img = Image.fromarray(image, 'RGBA')
    img.save('my.png')
    pixmap = QPixmap('my.png')
    self.label_2.setPixmap(pixmap)
    self.pushButton_9.setEnabled(True)#activer le bouton Color
    self.whichForm = False

def addRectangle(self):
    # créer une image transparente comme intermédiaire juste pour l'affichage des formes
    img_height, img_width = self.label_2.height(), self.label_2.width()
    n_channels = 4
    image = np.zeros((img_height - 2, img_width - 2, n_channels), dtype="uint8")
    # paramètres du rectangle
    start_point = (int(img_width/2) - 300, int(img_height/2) - 200) #top left corner
    end_point = (int(img_width/2) + 300, int(img_height/2) + 200) #bottom right corner, ne doit pas dépasser (img_width, img_height)
    color = (self.R, self.G, self.B, 255) #r g b alpha
    thickness = 3
    cv2.rectangle(image, start_point, end_point, color, thickness)

    img = Image.fromarray(image, 'RGBA')
    img.save('my.png')
    pixmap = QPixmap('my.png')
    self.label_2.setPixmap(pixmap)
    self.pushButton_9.setEnabled(True) # activer le bouton Color
    self.whichForm = True


def openImage(self):
    # read image from file dialog window
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(self.centralwidget, "Open Image", "", "Images (*.jpg);;Images (*.png);;All Files (*)", options=options)
    if fileName:
        print(fileName)
        src = cv2.imread(fileName, cv2.IMREAD_UNCHANGED)
        #afficher l'image originale
        pixmap = QPixmap(fileName)
        self.label_10.setPixmap(pixmap)
        # afficher l'image R
        red_channel = src[:, :, 2] #extract red channel
        cv2.imwrite('red_img.jpg', red_channel)
        pixmap = QPixmap('red_img.jpg')
        self.label_7.setPixmap(pixmap)

        # afficher l'image G
        green_channel = src[:, :, 1]  # extract green channel
        cv2.imwrite('green_img.jpg', green_channel)
        pixmap = QPixmap('green_img.jpg')
        self.label_8.setPixmap(pixmap)

        # afficher l'image B
        blue_channel = src[:, :, 0]  # extract blue channel
        cv2.imwrite('blue_img.jpg', blue_channel)
        pixmap = QPixmap('blue_img.jpg')
        self.label_9.setPixmap(pixmap)

        # Convert to CMYK
        cmyk_img = Image.fromarray(src).convert('CMYK')
        cmyk_img = np.array(cmyk_img)

        # afficher l'image C
        c_channel = cmyk_img[:, :, 2]  # extract Cyan channel
        cv2.imwrite('cyan_channel.jpg', c_channel)

        # afficher l'image M
        m_channel = cmyk_img[:, :, 1]  # extract magenta channel
        cv2.imwrite('m_channel.jpg', m_channel)

        # afficher l'image Y
        y_channel = cmyk_img[:, :, 0]  # extract yellow channel
        cv2.imwrite('y_channel.jpg', y_channel)

        # convert to HSV
        hsv_img = Image.fromarray(src).convert('HSV')
        hsv_img = np.array(hsv_img)

        # afficher l'image H
        h_channel = hsv_img[:, :, 0]  # extract hue channel
        cv2.imwrite('hue_img.jpg', h_channel)

        # afficher l'image S
        s_channel = hsv_img[:, :, 1]  # extract saturation channel
        cv2.imwrite('saturation_img.jpg', s_channel)

        # afficher l'image v
        v_channel = hsv_img[:, :, 2]  # extract value channel
        cv2.imwrite('value_img.jpg', v_channel)

        # convert to Lab
        lab_img = Image.fromarray(src).convert('LAB')
        lab_img = np.array(lab_img)

        # afficher l'image L
        l_channel = lab_img[:, :, 0]  # extract lightness channel
        cv2.imwrite('lightness_img.jpg', l_channel)

        # afficher l'image A
        rg_channel = lab_img[:, :, 2]  # extract Red to Green value channel
        cv2.imwrite('red_green_img.jpg', rg_channel)

        # afficher l'image B
        by_channel = lab_img[:, :, 1]  # extract blue to yellow value channel
        cv2.imwrite('blue_yellow_img.jpg', by_channel)

        # enable combobox
        self.combobox.setDisabled(False)
        # reset combox
        self.combobox.setCurrentIndex(0)
        self.label_4.setText('R')
        self.label_5.setText('G')
        self.label_6.setText('B')

def closeWindow(self):
    pass

class Ui_Lab1_Window(object):
   R = 255
   G = 0
   B = 0
   whichForm = False  # false : disc est affiché, true : rectangle est affiché
   def openWindowInterpolation(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Lab1_Interpolation()
        self.ui.my_signal.connect(self.changeFormColor) #récupérer les valeurs R G B de l'autre fenêtre
        self.ui.setupUi(self.window, self.R, self.G, self.B)
        self.window.show()
   def setupUi(self, Lab1_Window):
        Lab1_Window.setObjectName("Lab1_Window")
        Lab1_Window.setEnabled(True)
        Lab1_Window.setMinimumSize(QtCore.QSize(1300, 900))
        Lab1_Window.setMaximumSize(QtCore.QSize(1300, 900))
        self.centralwidget = QtWidgets.QWidget(Lab1_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        self.tabWidget.blockSignals(True)  # just for not showing the initial message
        self.tabWidget.currentChanged.connect(self.onChange)  # changed!

        self.partie1 = QtWidgets.QWidget()
        self.partie1.setObjectName("partie1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.partie1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.partie1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(300, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setObjectName("pushButton_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton_9)
        self.horizontalLayout_10.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.frame)
        self.label_2 = QtWidgets.QLabel(self.partie1)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.tabWidget.addTab(self.partie1, "")
        self.partie2 = QtWidgets.QWidget()
        self.partie2.setObjectName("partie2")
        self.gridLayout = QtWidgets.QGridLayout(self.partie2)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_6 = QtWidgets.QFrame(self.partie2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame_6)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_7.setScaledContents(True)
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_6)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_8.setScaledContents(True)
        self.verticalLayout_2.addWidget(self.label_8)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_6)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_9.setScaledContents(True)
        self.verticalLayout_4.addWidget(self.label_9)
        self.horizontalLayout.addWidget(self.frame_4)
        self.gridLayout.addWidget(self.frame_6, 1, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.partie2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_2.addWidget(self.frame_8, 0, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.label_10 = QtWidgets.QLabel(self.frame_7)
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_10.setScaledContents(True)
        self.verticalLayout_5.addWidget(self.label_10)
        self.gridLayout_2.addWidget(self.frame_7, 0, 1, 1, 1)
        self.frame_9 = QtWidgets.QFrame(self.frame_5)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_2.addWidget(self.frame_9, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.partie2, "")
        self.partie3 = QtWidgets.QWidget()
        self.partie3.setObjectName("partie3")
        self.tabWidget.addTab(self.partie3, "")
        self.verticalLayout_6.addWidget(self.tabWidget)
        Lab1_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Lab1_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAdd = QtWidgets.QMenu(self.menubar)
        self.menuAdd.setObjectName("menuAdd")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Lab1_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Lab1_Window)
        self.statusbar.setObjectName("statusbar")
        Lab1_Window.setStatusBar(self.statusbar)
        self.actionDis = QtWidgets.QAction(Lab1_Window)
        self.actionDis.setObjectName("actionDis")
        self.actionRectangle = QtWidgets.QAction(Lab1_Window)
        self.actionRectangle.setObjectName("actionRectangle")
        self.actionImage = QtWidgets.QAction(Lab1_Window)
        self.actionImage.setObjectName("actionImage")
        self.actionExit = QtWidgets.QAction(Lab1_Window)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(Lab1_Window)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionExit)
        self.menuAdd.addAction(self.actionDis)
        self.menuAdd.addAction(self.actionRectangle)
        self.menuAdd.addAction(self.actionImage)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAdd.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        # edit start
        self.combobox = QtWidgets.QComboBox(self.partie2)
        self.combobox.addItems(['RGB', 'CMYK', 'HSV', 'Lab'])
        self.combobox.setObjectName("combobox")
        #edit end

        #valeurs initiales r, g et b pour l'affichage des formes : (255, 0, 0)

        self.actionDis.setDisabled(False)
        self.actionRectangle.setDisabled(False)
        self.actionImage.setDisabled(True)
        self.actionDis.triggered.connect(lambda: addDisc(self))
        self.actionRectangle.triggered.connect(lambda: addRectangle(self))
        self.actionImage.triggered.connect(lambda: openImage(self))
        self.actionExit.triggered.connect(lambda: closeWindow(self))
        self.pushButton_9.clicked.connect(self.openWindowInterpolation)
        self.tabWidget.blockSignals(False)  # now listen the currentChanged signal

        #comboBox disabled until an image is displayed
        self.combobox.setDisabled(True)
        self.combobox.activated.connect(self.activated)

        self.retranslateUi(Lab1_Window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Lab1_Window)

   def activated(self, index):
        # change the display if combobox is activated
        if index == 3:
            self.label_4.setText('L')
            self.label_5.setText('a')
            self.label_6.setText('b')
            pixmap = QPixmap('lightness_img.jpg')
            self.label_7.setPixmap(pixmap)
            pixmap = QPixmap('red_green_img.jpg')
            self.label_8.setPixmap(pixmap)
            pixmap = QPixmap('blue_yellow_img.jpg')
            self.label_9.setPixmap(pixmap)
        elif index == 2:
            self.label_4.setText('H')
            self.label_5.setText('S')
            self.label_6.setText('V')
            pixmap = QPixmap('hue_img.jpg')
            self.label_7.setPixmap(pixmap)
            pixmap = QPixmap('saturation_img.jpg')
            self.label_8.setPixmap(pixmap)
            pixmap = QPixmap('value_img.jpg')
            self.label_9.setPixmap(pixmap)
        elif index == 1:
            self.label_4.setText('C')
            self.label_5.setText('M')
            self.label_6.setText('Y')
            pixmap = QPixmap('cyan_channel.jpg')
            self.label_7.setPixmap(pixmap)
            pixmap = QPixmap('m_channel.jpg')
            self.label_8.setPixmap(pixmap)
            pixmap = QPixmap('y_channel.jpg')
            self.label_9.setPixmap(pixmap)
        else:
            self.label_4.setText('R')
            self.label_5.setText('G')
            self.label_6.setText('B')
            pixmap = QPixmap('red_img.jpg')
            self.label_7.setPixmap(pixmap)
            pixmap = QPixmap('green_img.jpg')
            self.label_8.setPixmap(pixmap)
            pixmap = QPixmap('blue_img.jpg')
            self.label_9.setPixmap(pixmap)

   def changeFormColor(self, r, g, b, boolbutton):
        if boolbutton:
            self.R = r
            self.G = g
            self.B = b
            if self.whichForm :
                addRectangle(self)
            else :
                addDisc(self)
        self.window.close()

   def onChange(self, i):  # changed!
       if (self.tabWidget.currentIndex() == 1):
           self.actionDis.setDisabled(True)
           self.actionRectangle.setDisabled(True)
           self.actionImage.setDisabled(False)
       if (self.tabWidget.currentIndex() == 0):
           self.actionDis.setDisabled(False)
           self.actionRectangle.setDisabled(False)
           self.actionImage.setDisabled(True)

   def retranslateUi(self, Lab1_Window):
        _translate = QtCore.QCoreApplication.translate
        Lab1_Window.setWindowTitle(_translate("Lab1_Window", "Lab1_Window"))
        self.label.setText(_translate("Lab1_Window", "Selected Object Color"))
        self.pushButton_9.setText(_translate("Lab1_Window", "Color"))
        self.pushButton_9.setEnabled(False)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.partie1), _translate("Lab1_Window", "Color Interpolation"))
        self.label_4.setText(_translate("Lab1_Window", "R Image"))
        self.label_5.setText(_translate("Lab1_Window", "G Image"))
        self.label_6.setText(_translate("Lab1_Window", "B Image"))
        self.label_3.setText(_translate("Lab1_Window", "Original Image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.partie2), _translate("Lab1_Window", "Image Decomposition"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.partie3), _translate("Lab1_Window", "Contrast and Brightness"))
        self.menuFile.setTitle(_translate("Lab1_Window", "File"))
        self.menuAdd.setTitle(_translate("Lab1_Window", "Add"))
        self.menuHelp.setTitle(_translate("Lab1_Window", "Help"))
        self.actionDis.setText(_translate("Lab1_Window", "Disc"))
        self.actionRectangle.setText(_translate("Lab1_Window", "Rectangle"))
        self.actionImage.setText(_translate("Lab1_Window", "Image"))
        self.actionExit.setText(_translate("Lab1_Window", "Exit"))
        self.actionAbout.setText(_translate("Lab1_Window", "About"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Lab1_Window = QtWidgets.QMainWindow()
    ui = Ui_Lab1_Window()
    ui.setupUi(Lab1_Window)
    Lab1_Window.show()
    sys.exit(app.exec_())
