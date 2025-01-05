# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomCheckBox import QCustomCheckBox
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1179, 699)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(1179, 699))
        self.widget.setMaximumSize(QSize(1179, 699))
        self.horizontalLayout_10 = QHBoxLayout(self.widget)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.globale_screen = QStackedWidget(self.widget)
        self.globale_screen.setObjectName(u"globale_screen")
        self.globale_screen.setMinimumSize(QSize(1179, 699))
        self.globale_screen.setMaximumSize(QSize(1179, 699))
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.login.setMinimumSize(QSize(0, 699))
        self.login.setMaximumSize(QSize(16777215, 699))
        self.verticalLayout = QVBoxLayout(self.login)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.login)
        self.header.setObjectName(u"header")
        self.horizontalLayout_6 = QHBoxLayout(self.header)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(100, 5, 5, 0)
        self.notificationSlide = QCustomSlideMenu(self.header)
        self.notificationSlide.setObjectName(u"notificationSlide")
        self.notificationSlide.setMaximumSize(QSize(800, 16777215))
        self.horizontalLayout_7 = QHBoxLayout(self.notificationSlide)
        self.horizontalLayout_7.setSpacing(7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.frame_9 = QFrame(self.notificationSlide)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMinimumSize(QSize(678, 29))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setSpacing(3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.notificationTxt = QLabel(self.frame_9)
        self.notificationTxt.setObjectName(u"notificationTxt")
        self.notificationTxt.setMinimumSize(QSize(150, 0))
        font = QFont()
        font.setPointSize(10)
        self.notificationTxt.setFont(font)
        self.notificationTxt.setAlignment(Qt.AlignCenter)
        self.notificationTxt.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.notificationTxt)


        self.horizontalLayout_7.addWidget(self.frame_9)

        self.closeNotification = QPushButton(self.notificationSlide)
        self.closeNotification.setObjectName(u"closeNotification")
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/check.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeNotification.setIcon(icon)

        self.horizontalLayout_7.addWidget(self.closeNotification, 0, Qt.AlignRight)


        self.horizontalLayout_6.addWidget(self.notificationSlide)

        self.close_window_button = QPushButton(self.header)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setMinimumSize(QSize(24, 24))
        self.close_window_button.setMaximumSize(QSize(24, 24))
        self.close_window_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_window_button.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.close_window_button, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header)

        self.main_body = QWidget(self.login)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.main_body)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 15, 0, 0)
        self.index_stack = QCustomQStackedWidget(self.main_body)
        self.index_stack.setObjectName(u"index_stack")
        self.index_stack.setStyleSheet(u"")
        self.welcome_login_pg = QWidget()
        self.welcome_login_pg.setObjectName(u"welcome_login_pg")
        self.welcome_login_pg.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.welcome_login_pg)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.welcome_login_pg)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777210))

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.to_signup = QPushButton(self.frame)
        self.to_signup.setObjectName(u"to_signup")
        self.to_signup.setMinimumSize(QSize(150, 35))
        self.to_signup.setMaximumSize(QSize(150, 35))
        self.to_signup.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.to_signup, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.index_stack.addWidget(self.welcome_login_pg)
        self.welcome_signup_pg = QWidget()
        self.welcome_signup_pg.setObjectName(u"welcome_signup_pg")
        self.verticalLayout_8 = QVBoxLayout(self.welcome_signup_pg)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_5 = QFrame(self.welcome_signup_pg)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 16777210))

        self.verticalLayout_7.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_9)

        self.to_login = QPushButton(self.frame_5)
        self.to_login.setObjectName(u"to_login")
        self.to_login.setMinimumSize(QSize(150, 35))
        self.to_login.setMaximumSize(QSize(150, 35))
        self.to_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.to_login, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.frame_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.index_stack.addWidget(self.welcome_signup_pg)

        self.horizontalLayout_2.addWidget(self.index_stack)

        self.form_stack = QCustomQStackedWidget(self.main_body)
        self.form_stack.setObjectName(u"form_stack")
        self.login_pg = QWidget()
        self.login_pg.setObjectName(u"login_pg")
        self.verticalLayout_4 = QVBoxLayout(self.login_pg)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.login_pg)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 16777210))

        self.verticalLayout_6.addWidget(self.label_4)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(200, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.usernameInput = QLineEdit(self.frame_3)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setMinimumSize(QSize(250, 35))
        self.usernameInput.setMaximumSize(QSize(250, 35))

        self.verticalLayout_5.addWidget(self.usernameInput)

        self.passwordInput = QLineEdit(self.frame_3)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setMinimumSize(QSize(250, 35))
        self.passwordInput.setMaximumSize(QSize(250, 35))
        self.passwordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout_5.addWidget(self.passwordInput)

        self.rest = QPushButton(self.frame_3)
        self.rest.setObjectName(u"rest")
        self.rest.setMinimumSize(QSize(250, 35))
        self.rest.setMaximumSize(QSize(250, 35))

        self.verticalLayout_5.addWidget(self.rest)

        self.siginBtn = QPushButton(self.frame_3)
        self.siginBtn.setObjectName(u"siginBtn")
        self.siginBtn.setMinimumSize(QSize(250, 35))
        self.siginBtn.setMaximumSize(QSize(250, 35))
        self.siginBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.siginBtn.setCheckable(False)
        self.siginBtn.setAutoRepeat(True)

        self.verticalLayout_5.addWidget(self.siginBtn)


        self.verticalLayout_6.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.google = QPushButton(self.frame_4)
        self.google.setObjectName(u"google")
        self.google.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/font_awesome_brands/icons/font_awesome/brands/google-plus-g.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.google.setIcon(icon2)
        self.google.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.google)

        self.facebook = QPushButton(self.frame_4)
        self.facebook.setObjectName(u"facebook")
        self.facebook.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/font_awesome_brands/icons/font_awesome/brands/facebook-f.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.facebook.setIcon(icon3)
        self.facebook.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.facebook)

        self.twitter = QPushButton(self.frame_4)
        self.twitter.setObjectName(u"twitter")
        self.twitter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/font_awesome_brands/icons/font_awesome/brands/square-x-twitter.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.twitter.setIcon(icon4)
        self.twitter.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.twitter)

        self.github = QPushButton(self.frame_4)
        self.github.setObjectName(u"github")
        self.github.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/font_awesome_brands/icons/font_awesome/brands/github.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.github.setIcon(icon5)
        self.github.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.github)


        self.verticalLayout_6.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame_2, 0, Qt.AlignVCenter)

        self.form_stack.addWidget(self.login_pg)
        self.Rest_pwd = QWidget()
        self.Rest_pwd.setObjectName(u"Rest_pwd")
        self.horizontalLayout_28 = QHBoxLayout(self.Rest_pwd)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.frame_21 = QFrame(self.Rest_pwd)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_21)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_21)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 16777210))

        self.verticalLayout_40.addWidget(self.label_14)

        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(200, 0))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_22)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.usernameInput_3 = QLineEdit(self.frame_22)
        self.usernameInput_3.setObjectName(u"usernameInput_3")
        self.usernameInput_3.setMinimumSize(QSize(250, 35))
        self.usernameInput_3.setMaximumSize(QSize(250, 35))

        self.verticalLayout_39.addWidget(self.usernameInput_3)

        self.passwordInput_3 = QLineEdit(self.frame_22)
        self.passwordInput_3.setObjectName(u"passwordInput_3")
        self.passwordInput_3.setMinimumSize(QSize(250, 35))
        self.passwordInput_3.setMaximumSize(QSize(250, 35))
        self.passwordInput_3.setEchoMode(QLineEdit.Password)

        self.verticalLayout_39.addWidget(self.passwordInput_3)

        self.confirmInput_2 = QLineEdit(self.frame_22)
        self.confirmInput_2.setObjectName(u"confirmInput_2")
        self.confirmInput_2.setMinimumSize(QSize(250, 35))
        self.confirmInput_2.setMaximumSize(QSize(250, 35))
        self.confirmInput_2.setEchoMode(QLineEdit.Password)
        self.confirmInput_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_39.addWidget(self.confirmInput_2)

        self.restbtn = QPushButton(self.frame_22)
        self.restbtn.setObjectName(u"restbtn")
        self.restbtn.setMinimumSize(QSize(250, 35))
        self.restbtn.setMaximumSize(QSize(250, 35))
        self.restbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_39.addWidget(self.restbtn, 0, Qt.AlignHCenter)


        self.verticalLayout_40.addWidget(self.frame_22, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_28.addWidget(self.frame_21, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.form_stack.addWidget(self.Rest_pwd)
        self.signup_pg = QWidget()
        self.signup_pg.setObjectName(u"signup_pg")
        self.verticalLayout_11 = QVBoxLayout(self.signup_pg)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_6 = QFrame(self.signup_pg)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 16777210))

        self.verticalLayout_9.addWidget(self.label_10)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(200, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.usernameInput_2 = QLineEdit(self.frame_7)
        self.usernameInput_2.setObjectName(u"usernameInput_2")
        self.usernameInput_2.setMinimumSize(QSize(250, 35))
        self.usernameInput_2.setMaximumSize(QSize(250, 35))

        self.verticalLayout_10.addWidget(self.usernameInput_2)

        self.passwordInput_2 = QLineEdit(self.frame_7)
        self.passwordInput_2.setObjectName(u"passwordInput_2")
        self.passwordInput_2.setMinimumSize(QSize(250, 35))
        self.passwordInput_2.setMaximumSize(QSize(250, 35))
        self.passwordInput_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_10.addWidget(self.passwordInput_2)

        self.confirmInput = QLineEdit(self.frame_7)
        self.confirmInput.setObjectName(u"confirmInput")
        self.confirmInput.setMinimumSize(QSize(250, 35))
        self.confirmInput.setMaximumSize(QSize(250, 35))
        self.confirmInput.setEchoMode(QLineEdit.Password)
        self.confirmInput.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.confirmInput)

        self.signupBtn = QPushButton(self.frame_7)
        self.signupBtn.setObjectName(u"signupBtn")
        self.signupBtn.setMinimumSize(QSize(250, 35))
        self.signupBtn.setMaximumSize(QSize(250, 35))
        self.signupBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.signupBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.frame_7, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_12)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.google_2 = QPushButton(self.frame_8)
        self.google_2.setObjectName(u"google_2")
        self.google_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.google_2.setIcon(icon2)
        self.google_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.google_2)

        self.facebook_2 = QPushButton(self.frame_8)
        self.facebook_2.setObjectName(u"facebook_2")
        self.facebook_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.facebook_2.setIcon(icon3)
        self.facebook_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.facebook_2)

        self.twitter_2 = QPushButton(self.frame_8)
        self.twitter_2.setObjectName(u"twitter_2")
        self.twitter_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.twitter_2.setIcon(icon4)
        self.twitter_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.twitter_2)

        self.github_2 = QPushButton(self.frame_8)
        self.github_2.setObjectName(u"github_2")
        self.github_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.github_2.setIcon(icon5)
        self.github_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.github_2)


        self.verticalLayout_9.addWidget(self.frame_8)


        self.verticalLayout_11.addWidget(self.frame_6, 0, Qt.AlignVCenter)

        self.form_stack.addWidget(self.signup_pg)

        self.horizontalLayout_2.addWidget(self.form_stack)


        self.verticalLayout.addWidget(self.main_body)

        self.footer = QFrame(self.login)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, 0, 0, 20)
        self.checkBox_2 = QCustomCheckBox(self.footer)
        self.checkBox_2.setObjectName(u"checkBox_2")
        icon6 = QIcon()
        icon6.addFile(u":/font_awesome_solid/icons/font_awesome/solid/palette.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.checkBox_2.setIcon(icon6)

        self.horizontalLayout_5.addWidget(self.checkBox_2)

        self.checkBox = QCustomCheckBox(self.footer)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_5.addWidget(self.checkBox, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.footer)

        self.globale_screen.addWidget(self.login)
        self.acceuil = QWidget()
        self.acceuil.setObjectName(u"acceuil")
        self.horizontalLayout_8 = QHBoxLayout(self.acceuil)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.icon_only_widget = QFrame(self.acceuil)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(90, 699))
        self.icon_only_widget.setMaximumSize(QSize(80, 699))
        self.icon_only_widget.setStyleSheet(u"  background-color: #008080;\n"
"")
        self.icon_only_widget.setFrameShape(QFrame.StyledPanel)
        self.icon_only_widget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(15, 0, 0, 0)
        self.frame_17 = QFrame(self.icon_only_widget)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(50, 0))
        self.frame_17.setMaximumSize(QSize(50, 16777215))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_17)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 10)
        self.pushButton_4 = QPushButton(self.frame_17)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(60, 60))
        self.pushButton_4.setMaximumSize(QSize(60, 60))
        self.pushButton_4.setStyleSheet(u"  background-color: transparent;")
        icon7 = QIcon()
        icon7.addFile(u":/font_awesome_brands/icons/font_awesome/brands/battle-net.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon7)
        self.pushButton_4.setIconSize(QSize(40, 40))

        self.verticalLayout_20.addWidget(self.pushButton_4)

        self.frame_15 = QFrame(self.frame_17)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_15)
        self.verticalLayout_19.setSpacing(20)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.to_packet_2 = QPushButton(self.frame_15)
        self.to_packet_2.setObjectName(u"to_packet_2")
        self.to_packet_2.setMinimumSize(QSize(50, 50))
        self.to_packet_2.setMaximumSize(QSize(50, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.to_packet_2.setFont(font1)
        self.to_packet_2.setStyleSheet(u"  background-color: transparent;\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/feather/icons/feather/cast.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.to_packet_2.setIcon(icon8)
        self.to_packet_2.setIconSize(QSize(24, 24))

        self.verticalLayout_19.addWidget(self.to_packet_2)

        self.to_menace_2 = QPushButton(self.frame_15)
        self.to_menace_2.setObjectName(u"to_menace_2")
        self.to_menace_2.setMinimumSize(QSize(0, 50))
        self.to_menace_2.setFont(font)
        self.to_menace_2.setStyleSheet(u"  background-color: transparent;\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/feather/icons/feather/alert-octagon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.to_menace_2.setIcon(icon9)
        self.to_menace_2.setIconSize(QSize(24, 24))

        self.verticalLayout_19.addWidget(self.to_menace_2)

        self.to_profil_2 = QPushButton(self.frame_15)
        self.to_profil_2.setObjectName(u"to_profil_2")
        self.to_profil_2.setMinimumSize(QSize(0, 50))
        self.to_profil_2.setFont(font)
        self.to_profil_2.setStyleSheet(u"  background-color: transparent;\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/feather/icons/feather/user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.to_profil_2.setIcon(icon10)
        self.to_profil_2.setIconSize(QSize(24, 23))

        self.verticalLayout_19.addWidget(self.to_profil_2)

        self.to_alert_2 = QPushButton(self.frame_15)
        self.to_alert_2.setObjectName(u"to_alert_2")
        self.to_alert_2.setMinimumSize(QSize(0, 50))
        self.to_alert_2.setFont(font)
        self.to_alert_2.setStyleSheet(u"  background-color: transparent;\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/feather/icons/feather/bell.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.to_alert_2.setIcon(icon11)
        self.to_alert_2.setIconSize(QSize(24, 24))

        self.verticalLayout_19.addWidget(self.to_alert_2)

        self.to_visual_2 = QPushButton(self.frame_15)
        self.to_visual_2.setObjectName(u"to_visual_2")
        self.to_visual_2.setMinimumSize(QSize(50, 50))
        self.to_visual_2.setFont(font)
        self.to_visual_2.setStyleSheet(u"  background-color: transparent;\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/font_awesome_brands/icons/font_awesome/brands/trello.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.to_visual_2.setIcon(icon12)
        self.to_visual_2.setIconSize(QSize(24, 24))

        self.verticalLayout_19.addWidget(self.to_visual_2)


        self.verticalLayout_20.addWidget(self.frame_15)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_2)

        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_18)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 8)
        self.Setting_2 = QPushButton(self.frame_18)
        self.Setting_2.setObjectName(u"Setting_2")
        self.Setting_2.setMinimumSize(QSize(50, 50))
        self.Setting_2.setFont(font)
        self.Setting_2.setStyleSheet(u"  background-color: transparent;\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/feather/icons/feather/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Setting_2.setIcon(icon13)
        self.Setting_2.setIconSize(QSize(30, 24))

        self.verticalLayout_23.addWidget(self.Setting_2)

        self.logout_2 = QPushButton(self.frame_18)
        self.logout_2.setObjectName(u"logout_2")
        self.logout_2.setMinimumSize(QSize(50, 50))
        self.logout_2.setFont(font)
        self.logout_2.setStyleSheet(u"  background-color: transparent;\n"
"")
        icon14 = QIcon()
        icon14.addFile(u":/feather/icons/feather/power.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logout_2.setIcon(icon14)
        self.logout_2.setIconSize(QSize(24, 24))

        self.verticalLayout_23.addWidget(self.logout_2)


        self.verticalLayout_20.addWidget(self.frame_18)


        self.verticalLayout_21.addWidget(self.frame_17)


        self.horizontalLayout_8.addWidget(self.icon_only_widget)

        self.icon_text_widget_3 = QWidget(self.acceuil)
        self.icon_text_widget_3.setObjectName(u"icon_text_widget_3")
        self.icon_text_widget_3.setMinimumSize(QSize(200, 699))
        self.icon_text_widget_3.setMaximumSize(QSize(200, 699))
        self.verticalLayout_18 = QVBoxLayout(self.icon_text_widget_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_39 = QFrame(self.icon_text_widget_3)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"background-color:transparent;")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_39)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 10)
        self.frame_11 = QFrame(self.frame_39)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_13 = QLabel(self.frame_11)
        self.label_13.setObjectName(u"label_13")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label_13.setFont(font2)

        self.horizontalLayout_16.addWidget(self.label_13, 0, Qt.AlignTop)


        self.verticalLayout_14.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.frame_40 = QFrame(self.frame_39)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy1)
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_40)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_40)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_13)
        self.verticalLayout_16.setSpacing(19)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.to_packet = QPushButton(self.frame_13)
        self.to_packet.setObjectName(u"to_packet")
        self.to_packet.setMinimumSize(QSize(0, 50))
        self.to_packet.setFont(font1)
        self.to_packet.setStyleSheet(u"padding: 10px 5px; \n"
"text-align:left;\n"
"")
        self.to_packet.setIcon(icon8)
        self.to_packet.setIconSize(QSize(24, 24))

        self.verticalLayout_16.addWidget(self.to_packet)

        self.to_menace = QPushButton(self.frame_13)
        self.to_menace.setObjectName(u"to_menace")
        self.to_menace.setMinimumSize(QSize(0, 50))
        self.to_menace.setFont(font)
        self.to_menace.setStyleSheet(u"padding: 5px; \n"
"text-align:left;")
        self.to_menace.setIcon(icon9)
        self.to_menace.setIconSize(QSize(24, 24))

        self.verticalLayout_16.addWidget(self.to_menace)

        self.to_profil = QPushButton(self.frame_13)
        self.to_profil.setObjectName(u"to_profil")
        self.to_profil.setMinimumSize(QSize(0, 50))
        self.to_profil.setFont(font)
        self.to_profil.setStyleSheet(u"padding: 5px; \n"
"text-align:left;")
        self.to_profil.setIcon(icon10)
        self.to_profil.setIconSize(QSize(24, 23))

        self.verticalLayout_16.addWidget(self.to_profil)

        self.to_alert = QPushButton(self.frame_13)
        self.to_alert.setObjectName(u"to_alert")
        self.to_alert.setMinimumSize(QSize(0, 50))
        self.to_alert.setFont(font)
        self.to_alert.setStyleSheet(u"padding: 5px; \n"
"text-align:left;")
        self.to_alert.setIcon(icon11)
        self.to_alert.setIconSize(QSize(24, 24))

        self.verticalLayout_16.addWidget(self.to_alert)

        self.to_visual = QPushButton(self.frame_13)
        self.to_visual.setObjectName(u"to_visual")
        self.to_visual.setMinimumSize(QSize(0, 50))
        self.to_visual.setFont(font)
        self.to_visual.setStyleSheet(u"padding: 5px; \n"
"text-align:left;")
        self.to_visual.setIcon(icon12)
        self.to_visual.setIconSize(QSize(24, 24))

        self.verticalLayout_16.addWidget(self.to_visual)


        self.verticalLayout_15.addWidget(self.frame_13, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer)

        self.frame_14 = QFrame(self.frame_40)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_14)
        self.verticalLayout_17.setSpacing(19)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.Setting = QPushButton(self.frame_14)
        self.Setting.setObjectName(u"Setting")
        self.Setting.setFont(font)
        self.Setting.setStyleSheet(u"padding: 5px; \n"
"text-align:left;")
        self.Setting.setIcon(icon13)
        self.Setting.setIconSize(QSize(24, 24))

        self.verticalLayout_17.addWidget(self.Setting)

        self.logout = QPushButton(self.frame_14)
        self.logout.setObjectName(u"logout")
        self.logout.setFont(font)
        self.logout.setStyleSheet(u"padding: 5px; \n"
"text-align:left;")
        self.logout.setIcon(icon14)
        self.logout.setIconSize(QSize(24, 24))

        self.verticalLayout_17.addWidget(self.logout)


        self.verticalLayout_15.addWidget(self.frame_14, 0, Qt.AlignBottom)


        self.verticalLayout_14.addWidget(self.frame_40)


        self.verticalLayout_18.addWidget(self.frame_39)


        self.horizontalLayout_8.addWidget(self.icon_text_widget_3)

        self.screen = QFrame(self.acceuil)
        self.screen.setObjectName(u"screen")
        self.screen.setFrameShape(QFrame.StyledPanel)
        self.screen.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.screen)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.header_widget = QWidget(self.screen)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(0, 80))
        self.header_widget.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_15 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.header_widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(10, 0, 0, 0)
        self.menuBtn_3 = QPushButton(self.widget_4)
        self.menuBtn_3.setObjectName(u"menuBtn_3")
        icon15 = QIcon()
        icon15.addFile(u":/feather/icons/feather/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn_3.setIcon(icon15)
        self.menuBtn_3.setIconSize(QSize(24, 24))
        self.menuBtn_3.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.menuBtn_3, 0, Qt.AlignLeft)

        self.appHeader = QLabel(self.widget_4)
        self.appHeader.setObjectName(u"appHeader")
        self.appHeader.setFont(font2)
        self.appHeader.setStyleSheet(u"color: #008080;")

        self.horizontalLayout_14.addWidget(self.appHeader, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_15.addWidget(self.widget_4, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.widget_2 = QWidget(self.header_widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.searchFrame = QFrame(self.widget_2)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setMinimumSize(QSize(250, 40))
        self.searchFrame.setMaximumSize(QSize(0, 0))
        self.searchFrame.setStyleSheet(u"border-radius:10px;\n"
"border: 2px solid  rgb(0, 128, 128);")
        self.searchFrame.setFrameShape(QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.searchFrame)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(5, 0, 0, 0)
        self.label_11 = QLabel(self.searchFrame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(30, 30))
        self.label_11.setMaximumSize(QSize(30, 30))
        self.label_11.setStyleSheet(u"border: none;")
        self.label_11.setPixmap(QPixmap(u":/feather/icons/feather/search.png"))
        self.label_11.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.label_11)

        self.lineEdit = QLineEdit(self.searchFrame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 30))
        self.lineEdit.setStyleSheet(u"border: 2px solide #000;\n"
"background-color: transparent;\n"
"")

        self.horizontalLayout_12.addWidget(self.lineEdit, 0, Qt.AlignRight)


        self.horizontalLayout_11.addWidget(self.searchFrame, 0, Qt.AlignTop)


        self.horizontalLayout_15.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_13.addWidget(self.header_widget)

        self.main_screen = QWidget(self.screen)
        self.main_screen.setObjectName(u"main_screen")
        self.horizontalLayout_9 = QHBoxLayout(self.main_screen)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pages_screen = QStackedWidget(self.main_screen)
        self.pages_screen.setObjectName(u"pages_screen")
        self.packet = QWidget()
        self.packet.setObjectName(u"packet")
        self.verticalLayout_26 = QVBoxLayout(self.packet)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.cardsFrame = QWidget(self.packet)
        self.cardsFrame.setObjectName(u"cardsFrame")
        self.horizontalLayout_13 = QHBoxLayout(self.cardsFrame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.card1 = QFrame(self.cardsFrame)
        self.card1.setObjectName(u"card1")
        self.card1.setMinimumSize(QSize(0, 55))
        self.card1.setMaximumSize(QSize(16777215, 55))
        font3 = QFont()
        font3.setBold(True)
        self.card1.setFont(font3)
        self.card1.setStyleSheet(u"border-radius:20px;\n"
"border: 1px solid #008080;\n"
"")
        self.card1.setFrameShape(QFrame.StyledPanel)
        self.card1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.card1)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.to_capture = QPushButton(self.card1)
        self.to_capture.setObjectName(u"to_capture")
        self.to_capture.setMinimumSize(QSize(35, 55))
        self.to_capture.setMaximumSize(QSize(16777215, 55))
        self.to_capture.setStyleSheet(u"border:none;")
        icon16 = QIcon()
        icon16.addFile(u":/feather/icons/feather/package.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.to_capture.setIcon(icon16)
        self.to_capture.setIconSize(QSize(40, 40))
        self.to_capture.setCheckable(True)
        self.to_capture.setFlat(False)

        self.horizontalLayout_17.addWidget(self.to_capture)


        self.horizontalLayout_13.addWidget(self.card1)

        self.card2 = QFrame(self.cardsFrame)
        self.card2.setObjectName(u"card2")
        self.card2.setStyleSheet(u"border-radius:20px;\n"
"border: 1px  solid #008080;")
        self.card2.setFrameShape(QFrame.StyledPanel)
        self.card2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.card2)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.to_filtrer = QPushButton(self.card2)
        self.to_filtrer.setObjectName(u"to_filtrer")
        self.to_filtrer.setMinimumSize(QSize(35, 55))
        self.to_filtrer.setMaximumSize(QSize(16777215, 55))
        self.to_filtrer.setStyleSheet(u"border: none;")
        icon17 = QIcon()
        icon17.addFile(u":/feather/icons/feather/filter.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.to_filtrer.setIcon(icon17)
        self.to_filtrer.setIconSize(QSize(30, 30))
        self.to_filtrer.setCheckable(True)

        self.verticalLayout_24.addWidget(self.to_filtrer)


        self.horizontalLayout_13.addWidget(self.card2)


        self.verticalLayout_26.addWidget(self.cardsFrame)

        self.frame_16 = QFrame(self.packet)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.packets = QStackedWidget(self.frame_16)
        self.packets.setObjectName(u"packets")
        self.capture = QWidget()
        self.capture.setObjectName(u"capture")
        self.verticalLayout_25 = QVBoxLayout(self.capture)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_19 = QFrame(self.capture)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"background-color : transparent;\n"
"")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(150, 10, 150, 10)
        self.start = QPushButton(self.frame_19)
        self.start.setObjectName(u"start")
        self.start.setMinimumSize(QSize(150, 40))
        self.start.setStyleSheet(u"border-radius:10px;\n"
"border: 1px solid #008080;\n"
"background-color: #008080;\n"
"color: #ffffff;")
        self.start.setCheckable(True)

        self.horizontalLayout_20.addWidget(self.start, 0, Qt.AlignLeft)

        self.stop = QPushButton(self.frame_19)
        self.stop.setObjectName(u"stop")
        self.stop.setMinimumSize(QSize(150, 40))
        self.stop.setStyleSheet(u"border-radius:10px;\n"
"border: 1px solid #008080;\n"
"background-color: #008080;\n"
"color: #ffffff;")
        self.stop.setCheckable(True)

        self.horizontalLayout_20.addWidget(self.stop, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_25.addWidget(self.frame_19)

        self.tableWidget = QTableWidget(self.capture)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_25.addWidget(self.tableWidget)

        self.frame_20 = QFrame(self.capture)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.clear_sniffing = QPushButton(self.frame_20)
        self.clear_sniffing.setObjectName(u"clear_sniffing")
        self.clear_sniffing.setMinimumSize(QSize(150, 40))
        self.clear_sniffing.setMaximumSize(QSize(150, 40))
        self.clear_sniffing.setStyleSheet(u"border-radius:10px;\n"
"border: 1px solid #008080;\n"
"background-color: #008080;\n"
"color: #ffffff;")

        self.horizontalLayout_27.addWidget(self.clear_sniffing)


        self.verticalLayout_25.addWidget(self.frame_20)

        self.packets.addWidget(self.capture)
        self.filtrer = QWidget()
        self.filtrer.setObjectName(u"filtrer")
        self.verticalLayout_38 = QVBoxLayout(self.filtrer)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.scrollArea_2 = QScrollArea(self.filtrer)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 716, 622))
        self.verticalLayout_31 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_30 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 600))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_30)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 400))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_31)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_33 = QFrame(self.frame_31)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 200))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_33)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.ip_src = QLineEdit(self.frame_33)
        self.ip_src.setObjectName(u"ip_src")
        self.ip_src.setMinimumSize(QSize(150, 30))

        self.verticalLayout_37.addWidget(self.ip_src)

        self.ip_dest = QLineEdit(self.frame_33)
        self.ip_dest.setObjectName(u"ip_dest")
        self.ip_dest.setMinimumSize(QSize(150, 30))

        self.verticalLayout_37.addWidget(self.ip_dest)

        self.port_src = QLineEdit(self.frame_33)
        self.port_src.setObjectName(u"port_src")
        self.port_src.setMinimumSize(QSize(150, 30))

        self.verticalLayout_37.addWidget(self.port_src)

        self.port_dest = QLineEdit(self.frame_33)
        self.port_dest.setObjectName(u"port_dest")
        self.port_dest.setMinimumSize(QSize(0, 30))

        self.verticalLayout_37.addWidget(self.port_dest)

        self.protocol = QComboBox(self.frame_33)
        self.protocol.addItem("")
        self.protocol.addItem("")
        self.protocol.addItem("")
        self.protocol.addItem("")
        self.protocol.addItem("")
        self.protocol.addItem("")
        self.protocol.addItem("")
        self.protocol.setObjectName(u"protocol")
        self.protocol.setMinimumSize(QSize(0, 30))

        self.verticalLayout_37.addWidget(self.protocol)

        self.frame_12 = QFrame(self.frame_33)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.start_filter = QPushButton(self.frame_12)
        self.start_filter.setObjectName(u"start_filter")
        self.start_filter.setMinimumSize(QSize(120, 40))
        self.start_filter.setMaximumSize(QSize(150, 16777215))
        self.start_filter.setStyleSheet(u"border-radius:10px;\n"
"border: 1px solid #008080;\n"
"background-color: #008080;\n"
"color: #ffffff;")

        self.horizontalLayout_23.addWidget(self.start_filter)

        self.clear_filter_button = QPushButton(self.frame_12)
        self.clear_filter_button.setObjectName(u"clear_filter_button")
        self.clear_filter_button.setMinimumSize(QSize(120, 40))
        self.clear_filter_button.setMaximumSize(QSize(150, 16777215))
        self.clear_filter_button.setStyleSheet(u"border-radius:10px;\n"
"border: 1px solid #008080;\n"
"background-color: #008080;\n"
"color: #ffffff;")

        self.horizontalLayout_23.addWidget(self.clear_filter_button)


        self.verticalLayout_37.addWidget(self.frame_12)


        self.verticalLayout_36.addWidget(self.frame_33)


        self.verticalLayout_35.addWidget(self.frame_31)

        self.frame_34 = QFrame(self.frame_30)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_34)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.tableWidget_2 = QTableWidget(self.frame_34)
        if (self.tableWidget_2.columnCount() < 10):
            self.tableWidget_2.setColumnCount(10)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, __qtablewidgetitem19)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_27.addWidget(self.tableWidget_2)


        self.verticalLayout_35.addWidget(self.frame_34)


        self.verticalLayout_31.addWidget(self.frame_30)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_38.addWidget(self.scrollArea_2)

        self.packets.addWidget(self.filtrer)

        self.horizontalLayout_19.addWidget(self.packets)


        self.verticalLayout_26.addWidget(self.frame_16)

        self.pages_screen.addWidget(self.packet)
        self.alert = QWidget()
        self.alert.setObjectName(u"alert")
        self.verticalLayout_41 = QVBoxLayout(self.alert)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.alert_list = QListWidget(self.alert)
        self.alert_list.setObjectName(u"alert_list")

        self.verticalLayout_41.addWidget(self.alert_list)

        self.pages_screen.addWidget(self.alert)
        self.menace = QWidget()
        self.menace.setObjectName(u"menace")
        self.widget_3 = QWidget(self.menace)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(180, 260, 120, 80))
        self.pages_screen.addWidget(self.menace)
        self.profil = QWidget()
        self.profil.setObjectName(u"profil")
        self.verticalLayout_30 = QVBoxLayout(self.profil)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.cardsFrame_2 = QWidget(self.profil)
        self.cardsFrame_2.setObjectName(u"cardsFrame_2")
        self.horizontalLayout_21 = QHBoxLayout(self.cardsFrame_2)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.card1_2 = QFrame(self.cardsFrame_2)
        self.card1_2.setObjectName(u"card1_2")
        self.card1_2.setMinimumSize(QSize(0, 55))
        self.card1_2.setMaximumSize(QSize(16777215, 55))
        self.card1_2.setFont(font3)
        self.card1_2.setStyleSheet(u"border-radius:20px;\n"
"border: 1px solid #008080;\n"
"")
        self.card1_2.setFrameShape(QFrame.StyledPanel)
        self.card1_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.card1_2)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.editbtn = QPushButton(self.card1_2)
        self.editbtn.setObjectName(u"editbtn")
        self.editbtn.setMinimumSize(QSize(35, 55))
        icon18 = QIcon()
        icon18.addFile(u":/material_design/icons/material_design/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editbtn.setIcon(icon18)
        self.editbtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_22.addWidget(self.editbtn)


        self.horizontalLayout_21.addWidget(self.card1_2)

        self.card2_2 = QFrame(self.cardsFrame_2)
        self.card2_2.setObjectName(u"card2_2")
        self.card2_2.setMinimumSize(QSize(0, 55))
        self.card2_2.setMaximumSize(QSize(16777215, 55))
        self.card2_2.setStyleSheet(u"border-radius:20px;\n"
"border: 1px  solid #008080;")
        self.card2_2.setFrameShape(QFrame.StyledPanel)
        self.card2_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.card2_2)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.deletbtn = QPushButton(self.card2_2)
        self.deletbtn.setObjectName(u"deletbtn")
        self.deletbtn.setMinimumSize(QSize(35, 55))
        self.deletbtn.setStyleSheet(u"border: none;")
        icon19 = QIcon()
        icon19.addFile(u":/material_design/icons/material_design/restore_from_trash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.deletbtn.setIcon(icon19)
        self.deletbtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_18.addWidget(self.deletbtn)


        self.horizontalLayout_21.addWidget(self.card2_2)


        self.verticalLayout_30.addWidget(self.cardsFrame_2)

        self.frame_23 = QFrame(self.profil)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.profil_edit = QStackedWidget(self.frame_23)
        self.profil_edit.setObjectName(u"profil_edit")
        self.edit_form = QWidget()
        self.edit_form.setObjectName(u"edit_form")
        self.horizontalLayout_25 = QHBoxLayout(self.edit_form)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.scrollArea = QScrollArea(self.edit_form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 317, 622))
        self.verticalLayout_29 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_25 = QFrame(self.scrollAreaWidgetContents)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 600))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_25)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(0, 400))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_27)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 120))
        self.frame_28.setMaximumSize(QSize(16777215, 120))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.label_17 = QLabel(self.frame_28)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(270, 10, 100, 100))
        self.label_17.setMinimumSize(QSize(100, 100))
        self.label_17.setMaximumSize(QSize(80, 80))
        self.label_17.setPixmap(QPixmap(u":/feather/icons/feather/user.png"))
        self.label_17.setScaledContents(True)
        self.pushButton_2 = QPushButton(self.frame_28)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(340, 70, 40, 40))
        self.pushButton_2.setMinimumSize(QSize(40, 40))
        self.pushButton_2.setMaximumSize(QSize(40, 40))
        self.pushButton_2.setIcon(icon18)
        self.pushButton_2.setIconSize(QSize(35, 35))

        self.verticalLayout_34.addWidget(self.frame_28)

        self.frame_26 = QFrame(self.frame_27)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(0, 200))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_26)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.lineEdit_6 = QLineEdit(self.frame_26)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(150, 30))

        self.verticalLayout_33.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.frame_26)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(150, 30))

        self.verticalLayout_33.addWidget(self.lineEdit_7)

        self.lineEdit_5 = QLineEdit(self.frame_26)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(150, 30))

        self.verticalLayout_33.addWidget(self.lineEdit_5)

        self.dateEdit_2 = QDateEdit(self.frame_26)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setMinimumSize(QSize(0, 30))
        self.dateEdit_2.setProperty(u"showGroupSeparator", False)
        self.dateEdit_2.setCalendarPopup(True)

        self.verticalLayout_33.addWidget(self.dateEdit_2)


        self.verticalLayout_34.addWidget(self.frame_26)


        self.verticalLayout_32.addWidget(self.frame_27)

        self.frame_29 = QFrame(self.frame_25)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.stop_2 = QPushButton(self.frame_29)
        self.stop_2.setObjectName(u"stop_2")
        self.stop_2.setMinimumSize(QSize(120, 40))
        self.stop_2.setMaximumSize(QSize(120, 16777215))
        self.stop_2.setStyleSheet(u"border-radius:10px;\n"
"border: 1px solid #008080;\n"
"background-color: #008080;\n"
"color: #ffffff;")

        self.horizontalLayout_26.addWidget(self.stop_2)

        self.start_2 = QPushButton(self.frame_29)
        self.start_2.setObjectName(u"start_2")
        self.start_2.setMinimumSize(QSize(120, 40))
        self.start_2.setMaximumSize(QSize(120, 16777215))
        self.start_2.setStyleSheet(u"border-radius:10px;\n"
"border: 1px solid #008080;\n"
"background-color: #008080;\n"
"color: #ffffff;")

        self.horizontalLayout_26.addWidget(self.start_2)


        self.verticalLayout_32.addWidget(self.frame_29)


        self.verticalLayout_29.addWidget(self.frame_25)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_25.addWidget(self.scrollArea)

        self.profil_edit.addWidget(self.edit_form)
        self.delate = QWidget()
        self.delate.setObjectName(u"delate")
        self.verticalLayout_28 = QVBoxLayout(self.delate)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_10 = QFrame(self.delate)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(400, 250))
        self.frame_10.setMaximumSize(QSize(16777215, 250))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.lineEdit_3 = QLineEdit(self.frame_10)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(250, 30))
        self.lineEdit_3.setMaximumSize(QSize(250, 30))

        self.verticalLayout_22.addWidget(self.lineEdit_3, 0, Qt.AlignHCenter)

        self.lineEdit_4 = QLineEdit(self.frame_10)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(250, 30))
        self.lineEdit_4.setMaximumSize(QSize(250, 30))
        self.lineEdit_4.setEchoMode(QLineEdit.Password)

        self.verticalLayout_22.addWidget(self.lineEdit_4, 0, Qt.AlignHCenter)

        self.lineEdit_11 = QLineEdit(self.frame_10)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(250, 30))
        self.lineEdit_11.setMaximumSize(QSize(250, 30))
        self.lineEdit_11.setEchoMode(QLineEdit.Password)

        self.verticalLayout_22.addWidget(self.lineEdit_11, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.frame_10)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(250, 30))
        self.pushButton.setMaximumSize(QSize(250, 30))

        self.verticalLayout_22.addWidget(self.pushButton, 0, Qt.AlignHCenter)


        self.verticalLayout_28.addWidget(self.frame_10)

        self.profil_edit.addWidget(self.delate)

        self.horizontalLayout_24.addWidget(self.profil_edit)


        self.verticalLayout_30.addWidget(self.frame_23)

        self.pages_screen.addWidget(self.profil)
        self.visual = QWidget()
        self.visual.setObjectName(u"visual")
        self.label_18 = QLabel(self.visual)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(450, 300, 55, 16))
        self.pages_screen.addWidget(self.visual)

        self.horizontalLayout_9.addWidget(self.pages_screen)


        self.verticalLayout_13.addWidget(self.main_screen)


        self.horizontalLayout_8.addWidget(self.screen)

        self.globale_screen.addWidget(self.acceuil)

        self.horizontalLayout_10.addWidget(self.globale_screen)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menuBtn_3.toggled.connect(self.icon_only_widget.setVisible)
        self.menuBtn_3.toggled.connect(self.icon_text_widget_3.setHidden)

        self.globale_screen.setCurrentIndex(1)
        self.index_stack.setCurrentIndex(0)
        self.form_stack.setCurrentIndex(0)
        self.pages_screen.setCurrentIndex(0)
        self.packets.setCurrentIndex(1)
        self.profil_edit.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.notificationTxt.setText(QCoreApplication.translate("MainWindow", u"Notification message. Click \"X\"  to hide.", None))
        self.closeNotification.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.close_window_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Hi, Welcome !!</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enter your details to login or login with social media apps.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Not regidtred ? Click below to register.", None))
        self.to_signup.setText(QCoreApplication.translate("MainWindow", u"Sign Up ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Hi, Welcome !!</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Enter your details to register. You can also rigester using social media apps.", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Already regidtred ? Click below to login.", None))
        self.to_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Sign In </span></p></body></html>", None))
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.rest.setText(QCoreApplication.translate("MainWindow", u"Forgot your password ?", None))
        self.siginBtn.setText(QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Or Login with social media", None))
        self.google.setText("")
        self.facebook.setText("")
        self.twitter.setText("")
        self.github.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Rest Password</span></p></body></html>", None))
        self.usernameInput_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.passwordInput_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.confirmInput_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm password", None))
        self.restbtn.setText(QCoreApplication.translate("MainWindow", u"Rest password", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Sign Up</span></p></body></html>", None))
        self.usernameInput_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.passwordInput_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.confirmInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm password", None))
        self.signupBtn.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Or Register with social media", None))
        self.google_2.setText("")
        self.facebook_2.setText("")
        self.twitter_2.setText("")
        self.github_2.setText("")
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Remember me", None))
        self.pushButton_4.setText("")
        self.to_packet_2.setText("")
        self.to_menace_2.setText("")
        self.to_profil_2.setText("")
        self.to_alert_2.setText("")
        self.to_visual_2.setText("")
        self.Setting_2.setText("")
        self.logout_2.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt;\">FlowCaptor</span></p></body></html>", None))
        self.to_packet.setText(QCoreApplication.translate("MainWindow", u"   Packets", None))
        self.to_menace.setText(QCoreApplication.translate("MainWindow", u"   Menaces", None))
        self.to_profil.setText(QCoreApplication.translate("MainWindow", u"   Profil ", None))
        self.to_alert.setText(QCoreApplication.translate("MainWindow", u"    Alerts", None))
        self.to_visual.setText(QCoreApplication.translate("MainWindow", u"    Visualisation", None))
        self.Setting.setText(QCoreApplication.translate("MainWindow", u"   Settings", None))
        self.logout.setText(QCoreApplication.translate("MainWindow", u"   Log Out", None))
        self.menuBtn_3.setText("")
        self.appHeader.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_11.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.to_capture.setText(QCoreApplication.translate("MainWindow", u"Capturer", None))
        self.to_filtrer.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"Start Sniffing", None))
        self.stop.setText(QCoreApplication.translate("MainWindow", u"Stop Sniffing", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"TIME", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Source MAC", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Destination MAC", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Source IP", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Destination IP", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Protocol", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Length", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Source Port", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Destination Port", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Packet Type ", None));
        self.clear_sniffing.setText(QCoreApplication.translate("MainWindow", u"Clear ", None))
        self.ip_src.setText("")
        self.ip_src.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IP Source Adresse", None))
        self.ip_dest.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IP Destination Adresse", None))
        self.port_src.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Port Source", None))
        self.port_dest.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Port Destionation", None))
        self.protocol.setItemText(0, QCoreApplication.translate("MainWindow", u"Selectionn\u00e9e Protocole", None))
        self.protocol.setItemText(1, QCoreApplication.translate("MainWindow", u"UDP", None))
        self.protocol.setItemText(2, QCoreApplication.translate("MainWindow", u"TCP", None))
        self.protocol.setItemText(3, QCoreApplication.translate("MainWindow", u"ICMP", None))
        self.protocol.setItemText(4, QCoreApplication.translate("MainWindow", u"ARP", None))
        self.protocol.setItemText(5, QCoreApplication.translate("MainWindow", u"IPV4", None))
        self.protocol.setItemText(6, QCoreApplication.translate("MainWindow", u"IPV6", None))

        self.start_filter.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.clear_filter_button.setText(QCoreApplication.translate("MainWindow", u"Clear ", None))
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"TIME", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Source MAC", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Destination MAC", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Source IP", None));
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Destination IP", None));
        ___qtablewidgetitem15 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Protocol", None));
        ___qtablewidgetitem16 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Length", None));
        ___qtablewidgetitem17 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Source Port", None));
        ___qtablewidgetitem18 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Destination Port", None));
        ___qtablewidgetitem19 = self.tableWidget_2.horizontalHeaderItem(9)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Packet Type ", None));
        self.editbtn.setText(QCoreApplication.translate("MainWindow", u"Modifier Profil", None))
        self.deletbtn.setText(QCoreApplication.translate("MainWindow", u"Supprimer Compte", None))
        self.label_17.setText("")
        self.pushButton_2.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First  Name", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email", None))
        self.dateEdit_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u" dd/MM/yyyy  ", None))
        self.stop_2.setText(QCoreApplication.translate("MainWindow", u"Annuler ", None))
        self.start_2.setText(QCoreApplication.translate("MainWindow", u"Sauvgarder ", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UserName", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirme Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Supprimer Conmpte", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"visual", None))
    # retranslateUi

