from PyQt5 import QtCore, QtGui, QtWidgets
from speedometer import Speedometer

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 485)
        MainWindow.setStyleSheet("background-color:rgb(33, 33, 33)")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.icons = self.load_icons()
        self.create_frame()
        self.create_labels()
        self.create_buttons()
        self.create_frames()
        self.create_speedometer()
        self.create_speaker_bar()
        self.create_left_buttons()
        self.create_centre_buttons()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def load_icons(self):
        return {
            "bluetooth": "bluetooth.png",
            "apps": "apps (1).png",
            "location": "location.png",
            "music": "music-alt.png",
            "speaker": "volume (1).png",
            "phone": "phone-call.png",
            "settings": "settings.png",
            "light": "pngegg.png",
            "mobile": "icons8-smartphone-64 (2).png",
            "battery": "battery (1).png",
            "automobile": "automobile.png",
            "home": "home selected.png",
            "dipper": "light_lamp_car_automobile_headlight-128.webp",
            "lock": "pngegg (1).png",
            "seat": "seat.png",
            "air-condition": "air-condition (1).png",
        }
    
    def create_frame(self):
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 300, 500))
        self.frame.setStyleSheet("background-color:rgb(33, 33, 33)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.left_frame = QtWidgets.QFrame(self.centralwidget)
        self.left_frame.setGeometry(QtCore.QRect(0, 0, 40, 500))
        self.left_frame.setStyleSheet("background-color:rgb(94, 94, 94)")
        self.left_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_frame.setObjectName("left_frame")
    

        self.logo = QtWidgets.QLabel(self.frame)
        self.logo.setGeometry(QtCore.QRect(50, 10, 200, 100))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("pngwing.com (2).png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        
        self.text = QtWidgets.QLabel(self.frame)
        self.text.setGeometry(QtCore.QRect(10, 120, 280, 40))
        self.text.setStyleSheet("font: 22pt \"Franklin Gothic Demi Cond\";\ncolor:rgb(193, 193, 193)")
        self.text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text.setFrameShadow(QtWidgets.QFrame.Raised)
        self.text.setText("Tesla Model 3")
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setObjectName("text")

    def create_labels(self):
        labels = {
            "km_label": (50, 210, 21, 21, "font: 75 12pt \"MS Shell Dlg 2\";\ncolor:white", "12", False),
            "fuel": (230, 230, 51, 20, "font: 75 italic 12pt \"Calibri\";\ncolor:white", "Fuel", False),
            "whkm": (170, 210, 51, 16, "font: 75 italic 12pt \"Calibri\";\ncolor:white", "wh/km", False),
            "average_label": (140, 210, 21, 21, "font: 75 12pt \"MS Shell Dlg 2\";\ncolor:white", "12", False),
            "fuel_label": (230, 210, 21, 21, "font: 75 12pt \"MS Shell Dlg 2\";\ncolor:white", "12", False),
            "km": (80, 210, 21, 16, "font: 75 italic 12pt \"Calibri\";\ncolor:white", "km", False),
            "average": (140, 230, 61, 20, "font: 75 italic 12pt \"Calibri\";\ncolor:white", "Average", False),
            "remaining": (50, 230, 81, 20, "font: 75 italic 12pt \"Calibri\";\ncolor:white", "Remaining", False),
            "kwh": (250, 210, 31, 16, "font: 75 italic 12pt \"Calibri\";\ncolor:white", "kWh", False),
        }

        for name, (x, y, w, h, style, text, is_image) in labels.items():
            label = QtWidgets.QLabel(self.frame)
            label.setGeometry(QtCore.QRect(x, y, w, h))
            label.setStyleSheet(style)
            label.setObjectName(name)
            if is_image:
                label.setPixmap(QtGui.QPixmap(text))
                label.setScaledContents(True)
            else:
                label.setText(text)

    def create_buttons(self):
        buttons = {
            "home": (50, 350, "home", 51, 51),
            "bluthooth": (110, 410, "bluetooth", 51, 51),
            "battery": (230, 410, "battery", 51, 51),
            "gear": (50, 410, "automobile", 51, 51),
            "air": (110, 350, "air-condition", 51, 51),
            "dipper": (230, 350, "dipper", 51, 51),
            "lock": (170, 350, "lock", 51, 51),
            "seat": (170, 410, "seat", 51, 51),
        }

        for name, (x, y, icon_name, w, h) in buttons.items():
            button = QtWidgets.QPushButton(self.frame)
            button.setGeometry(QtCore.QRect(x, y, w, h))
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            button.setStyleSheet("border: 2px solid #000000; border-radius: 25px; background-color:rgb(211, 211, 211)")
            button.setIcon(QtGui.QIcon(QtGui.QPixmap(self.icons[icon_name])))
            button.setIconSize(QtCore.QSize(25, 25))
            button.setObjectName(name)
            # Set the button as an attribute
            setattr(self, f"{name}_button", button)

            # Connect the button to its action method
            action_method = getattr(self, f"{name}_action", self.default_action)
            button.clicked.connect(action_method)

    def create_centre_buttons(self):
        centre_buttons = {
            "reverse": (40, 160, "R", 61, 51),
            "park": (100, 160, "P", 61, 51),
            "neutral": (160, 160, "N", 61, 51),
            "sports": (200, 160, "S", 61, 51),
        }

        for name, (x, y, text, w, h) in centre_buttons.items():
            button = QtWidgets.QPushButton(self.frame)
            button.setGeometry(QtCore.QRect(x, y, w, h))
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            button.setStyleSheet("font: 18pt 'MS Shell Dlg 2'; color: white; background-color: rgb(33, 33, 33); border: none;")
            button.setText(text)
            button.setObjectName(name)
            # Set the button as an attribute
            setattr(self, f"{name}_button", button)

            # Connect the button to its action method
            action_method = getattr(self, f"{name}_action", self.default_action)
            button.clicked.connect(action_method)

    def create_left_buttons(self):
        left_buttons = {
            "apps": (0, 50, "apps", 41, 41),
            "location": (0, 100, "location", 41, 41),
            "music": (0, 200, "music", 41, 41),
            "speaker": (0, 260, "speaker", 41, 41),
            "phone": (0, 350, "phone", 41, 41),
            "settings": (0, 400, "settings", 41, 41),
            "light": (0, 150, "light", 41, 41),
            "mobile": (0, 300, "mobile", 41, 61),
        }

        for name, (x, y, icon_name, w, h) in left_buttons.items():
            left_button = QtWidgets.QPushButton(self.left_frame)
            left_button.setGeometry(QtCore.QRect(x, y, w, h))
            left_button.setStyleSheet("QPushButton { border: none; background: none; }")
            left_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            left_button.setIcon(QtGui.QIcon(QtGui.QPixmap(self.icons[icon_name])))
            left_button.setIconSize(QtCore.QSize(25, 25))
            left_button.setObjectName(name)
            # Set the button as an attribute
            setattr(self, f"{name}_button", left_button)

            # Connect the button to its action method
            action_method = getattr(self, f"{name}_action", self.default_action)
            left_button.clicked.connect(action_method)

    def create_frames(self):
        frames = [
            (40, 260, 120, 80, [("tyre", 10, 10, "font: 75 16pt \"MS Shell Dlg 2\";\nborder-color:rgb(211, 211, 211)", "83"),
                                ("tyre_condition", 10, 40, "font: 75 italic 12pt \"Calibri\";\nborder-color:rgb(211, 211, 211)", "Tyre Condition"),
                                ("tyre_percent", 40, 10, "font: 75 italic 12pt \"Calibri\";\nborder-color:rgb(211, 211, 211)", "%")]),
            (160, 260, 120, 80, [("pressure", 10, 10, "font: 75 16pt \"MS Shell Dlg 2\";\nborder-color:rgb(211, 211, 211)", "83"),
                                 ("tyre_pressure", 10, 40, "font: 75 italic 12pt \"Calibri\";\nborder-color:rgb(211, 211, 211)", "Tyre Pressure"),
                                 ("tyre_psi", 40, 10, "font: 75 italic 12pt \"Calibri\";\nborder-color:rgb(211, 211, 211)", "psi")]),
        ]

        for x, y, w, h, labels in frames:
            frame = QtWidgets.QFrame(self.frame)
            frame.setGeometry(QtCore.QRect(x, y, w, h))
            frame.setStyleSheet("border: 2px solid #000000; border-radius: 13px; background-color:rgb(211, 211, 211)")
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            for name, lx, ly, style, text in labels:
                label = QtWidgets.QLabel(frame)
                label.setGeometry(QtCore.QRect(lx, ly, 101, 41))
                label.setStyleSheet(style)
                label.setText(text)
                label.setObjectName(name)

    def create_speedometer(self):
        self.speedometer_frame = QtWidgets.QFrame(self.centralwidget)
        self.speedometer_frame.setGeometry(QtCore.QRect(300, 0, 608, 484))
        self.speedometer_frame.setStyleSheet("border: none;")
        self.speedometer_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.speedometer_frame.setObjectName("speedometer_frame")
        
        self.layout = QtWidgets.QHBoxLayout(self.speedometer_frame)
        self.speedometer = Speedometer(100)
        self.layout.addWidget(self.speedometer)

    def create_speaker_bar(self):
        self.speaker_bar = QtWidgets.QSlider(self.centralwidget)
        self.speaker_bar.setGeometry(QtCore.QRect(875, 40, 20, 400))
        self.speaker_bar.setOrientation(QtCore.Qt.Vertical)
        self.speaker_bar.setMinimum(0)
        self.speaker_bar.setMaximum(100)
        self.speaker_bar.setValue(50)
        self.speaker_bar.setVisible(False)
        self.speaker_bar.setObjectName("speaker_bar")
        
    def toggle_speaker_bar(self):
        self.speaker_bar.setVisible(not self.speaker_bar.isVisible())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        # Update text of labels
        self.centralwidget.findChild(QtWidgets.QLabel, "km_label").setText(_translate("MainWindow", "25"))
        self.centralwidget.findChild(QtWidgets.QLabel, "average_label").setText(_translate("MainWindow", "12"))
        self.centralwidget.findChild(QtWidgets.QLabel, "fuel_label").setText(_translate("MainWindow", "12"))
        self.centralwidget.findChild(QtWidgets.QLabel, "tyre").setText(_translate("MainWindow", "82"))
        self.centralwidget.findChild(QtWidgets.QLabel, "pressure").setText(_translate("MainWindow", "12"))
    
    def default_action(self):
        print("Default action for undefined button")

    # Define action methods for each button
    def home_action(self):
        print("Home button clicked")

    def bluetooth_action(self):
        print("Bluetooth button clicked")

    def battery_action(self):
        print("Battery button clicked")

    def gear_action(self):
        print("Gear button clicked")

    def air_action(self):
        print("Air button clicked")

    def dipper_action(self):
        print("Dipper button clicked")

    def lock_action(self):
        print("Lock button clicked")

    def seat_action(self):
        print("Seat button clicked")

    def apps_action(self):
        print("Apps button clicked")

    def location_action(self):
       print("location button is clicked")

    def music_action(self):
        print("Music button clicked")

    def speaker_action(self):
        self.toggle_speaker_bar()

    def phone_action(self):
        print("Phone button clicked")

    def settings_action(self):
        print("Settings button clicked")

    def light_action(self):
        print("Light button clicked")

    def mobile_action(self):
        print("Mobile button clicked")

    def reverse_action(self):
        print("Reverse button clicked")

    def park_action(self):
        print("Park button clicked")

    def neutral_action(self):
        print("Neutral button clicked")

    def sports_action(self):
        print("Sports button clicked")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
