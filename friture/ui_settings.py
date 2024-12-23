# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings_Dialog(object):
    def setupUi(self, Settings_Dialog):
        Settings_Dialog.setObjectName("Settings_Dialog")
        Settings_Dialog.resize(459, 369)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images-src/tools.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Settings_Dialog.setWindowIcon(icon)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Settings_Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.inputGroup = QtWidgets.QGroupBox(Settings_Dialog)
        self.inputGroup.setObjectName("inputGroup")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.inputGroup)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_inputType_2 = QtWidgets.QLabel(self.inputGroup)
        self.label_inputType_2.setObjectName("label_inputType_2")
        self.verticalLayout_6.addWidget(self.label_inputType_2)
        self.comboBox_inputDevice = QtWidgets.QComboBox(self.inputGroup)
        self.comboBox_inputDevice.setObjectName("comboBox_inputDevice")
        self.verticalLayout_6.addWidget(self.comboBox_inputDevice)
        self.label_inputType_3 = QtWidgets.QLabel(self.inputGroup)
        self.label_inputType_3.setObjectName("label_inputType_3")
        self.verticalLayout_6.addWidget(self.label_inputType_3)
        
        # Add horizontal layout for QLineEdit and buttons
        self.horizontalLayout_file = QtWidgets.QHBoxLayout()
        self.fileBox_compensation = QtWidgets.QPushButton("Browse", self.inputGroup)
        self.fileBox_compensation.setObjectName("fileButton")
        self.horizontalLayout_file.addWidget(self.fileBox_compensation)
        self.clearButton = QtWidgets.QPushButton("Clear", self.inputGroup)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_file.addWidget(self.clearButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_file)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.label_inputType = QtWidgets.QLabel(self.inputGroup)
        self.label_inputType.setObjectName("label_inputType")
        self.verticalLayout_3.addWidget(self.label_inputType)
        self.radioButton_single = QtWidgets.QRadioButton(self.inputGroup)
        self.radioButton_single.setChecked(True)
        self.radioButton_single.setObjectName("radioButton_single")
        self.inputTypeButtonGroup = QtWidgets.QButtonGroup(Settings_Dialog)
        self.inputTypeButtonGroup.setObjectName("inputTypeButtonGroup")
        self.inputTypeButtonGroup.addButton(self.radioButton_single)
        self.verticalLayout_3.addWidget(self.radioButton_single)
        self.radioButton_duo = QtWidgets.QRadioButton(self.inputGroup)
        self.radioButton_duo.setObjectName("radioButton_duo")
        self.inputTypeButtonGroup.addButton(self.radioButton_duo)
        self.verticalLayout_3.addWidget(self.radioButton_duo)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_first = QtWidgets.QGroupBox(self.inputGroup)
        self.groupBox_first.setObjectName("groupBox_first")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_first)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox_firstChannel = QtWidgets.QComboBox(self.groupBox_first)
        self.comboBox_firstChannel.setObjectName("comboBox_firstChannel")
        self.verticalLayout.addWidget(self.comboBox_firstChannel)
        self.verticalLayout_4.addWidget(self.groupBox_first)
        self.groupBox_second = QtWidgets.QGroupBox(self.inputGroup)
        self.groupBox_second.setEnabled(False)
        self.groupBox_second.setObjectName("groupBox_second")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_second)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox_secondChannel = QtWidgets.QComboBox(self.groupBox_second)
        self.comboBox_secondChannel.setObjectName("comboBox_secondChannel")
        self.verticalLayout_2.addWidget(self.comboBox_secondChannel)
        self.verticalLayout_4.addWidget(self.groupBox_second)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addWidget(self.inputGroup)
        self.playbackGroup = QtWidgets.QGroupBox(Settings_Dialog)
        self.playbackGroup.setMinimumSize(QtCore.QSize(0, 0))
        self.playbackGroup.setObjectName("playbackGroup")
        self.formLayout_2 = QtWidgets.QFormLayout(self.playbackGroup)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_showPlayback = QtWidgets.QLabel(self.playbackGroup)
        self.label_showPlayback.setObjectName("label_showPlayback")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_showPlayback)
        self.checkbox_showPlayback = QtWidgets.QCheckBox(self.playbackGroup)
        self.checkbox_showPlayback.setText("")
        self.checkbox_showPlayback.setObjectName("checkbox_showPlayback")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.checkbox_showPlayback)
        self.label_historyLength = QtWidgets.QLabel(self.playbackGroup)
        self.label_historyLength.setObjectName("label_historyLength")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_historyLength)
        self.spinBox_historyLength = QtWidgets.QSpinBox(self.playbackGroup)
        self.spinBox_historyLength.setMinimum(1)
        self.spinBox_historyLength.setMaximum(600)
        self.spinBox_historyLength.setProperty("value", 30)
        self.spinBox_historyLength.setObjectName("spinBox_historyLength")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_historyLength)
        self.verticalLayout_5.addWidget(self.playbackGroup)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)

        self.retranslateUi(Settings_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Settings_Dialog)

    def retranslateUi(self, Settings_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Settings_Dialog.setWindowTitle(_translate("Settings_Dialog", "Settings"))
        self.inputGroup.setTitle(_translate("Settings_Dialog", "Input"))
        self.label_inputType_2.setText(_translate("Settings_Dialog", "Select the input device :"))
        self.label_inputType_3.setText(_translate("Settings_Dialog", "Select the compensation file:"))
        self.label_inputType.setText(_translate("Settings_Dialog", "Select the type of input :"))
        self.radioButton_single.setText(_translate("Settings_Dialog", "Single channel"))
        self.radioButton_duo.setText(_translate("Settings_Dialog", "Two channels"))
        self.groupBox_first.setTitle(_translate("Settings_Dialog", "First channel"))
        self.groupBox_second.setTitle(_translate("Settings_Dialog", "Second channel"))
        self.playbackGroup.setTitle(_translate("Settings_Dialog", "Playback"))
        self.label_showPlayback.setText(_translate("Settings_Dialog", "Show Playback Controls"))
        self.label_historyLength.setText(_translate("Settings_Dialog", "History Length"))
        self.spinBox_historyLength.setSuffix(_translate("Settings_Dialog", " s"))
from . import friture_rc
