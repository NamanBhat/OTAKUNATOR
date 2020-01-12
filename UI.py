from twentyQ import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
a=0
o=0
import pyttsx3
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QMessageBox
from PyQt5.QtMultimedia import QSound
import PyQt5.QtMultimedia as M
def dialog():
    global o,a
    o+=1
    a=1
def dialog1():
    global o,a
    o+=1
    a=0
def dialog2():
    global o,a
    o+=1
    a=0.5

class UI:
    def __init__(self):
        self.game = twentyQ()
        

    def playGame(self):
        global o
        keepPlaying = True
        app = QApplication(sys.argv)
        w = QWidget()

        w.showMaximized()
        w.setWindowTitle("Otakunator")
        l = QLabel(w)
        pixmap = QPixmap("homescreen.jpg")
        l.setPixmap(pixmap)
        l.move(400,-300)
        l.resize(10000, 1500)
        l.show()
        l2 = QLabel(w)
        pixmap=QPixmap("cloud3.png")
        l2.setPixmap(pixmap)
        l2.move(400,50)
        l2.resize(700,400)
        l2.setScaledContents(True)
        l2.setSizePolicy(QtWidgets.QSizePolicy.Ignored,QtWidgets.QSizePolicy.Ignored)
        l2.hide()
        simg = QtGui.QImage("background.png").scaled(w.maximumSize())
        pallette = QtGui.QPalette()
        pallette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(simg))
        w.setPalette(pallette)

        label = QLabel(w)
        label.move(110, 530)
        label.resize(900, 80)

        engine=pyttsx3.init()
        engine.setProperty('voice', engine.getProperty('voices')[0].id)
        engine.setProperty('rate', 200)
        engine.say("Hello I am Otaah kunator. Think about a character fro Narutoverse and I will guess it.  So, are you ready to challenge me")
        engine.runAndWait()
        btn = QPushButton(w)
        btn.setText("Next")
        btn.move(900, 840)
        btn.show()
        btn.clicked.connect(dialog)
        o=0
        while o == 0:
            QtCore.QCoreApplication.processEvents()
        o=0
        l.move(300, 100)
        btn.move(510, 600)
        l2.show()
        btn2 = QPushButton(w)
        btn3 = QPushButton(w)
        btn.setText("Yes")
        btn2.setText("No")
        btn3.setText("Maybe")
        btn.move(500,500)
        btn2.move(500,650)
        btn3.move(500,800)
        btn.resize(510,100)
        btn2.resize(510,100)
        btn3.resize(510,100)
        btn.setStyleSheet('QPushButton {background-color: #005296; color: white; font-size: 18pt; font-weight: bold} ')
        btn2.setStyleSheet('QPushButton {background-color: #0BB5FF; color: white; font-size: 18pt; font-weight: bold}')
        btn3.setStyleSheet('QPushButton {background-color: #AFC1DA; color: white; font-size: 18pt; font-weight: bold}')
        btn.show()
        btn2.show()
        btn3.show()


        simg = QtGui.QImage("background.png").scaled(w.size())
        pallette = QtGui.QPalette()
        pallette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(simg))
        w.setPalette(pallette)
        l.resize(300,500)



        url = QtCore.QUrl.fromLocalFile("./narutos-theme-song.wav")
        content = M.QMediaContent(url)
        playlist=M.QMediaPlaylist()
        playlist.addMedia(content)
        url = QtCore.QUrl.fromLocalFile("./naruto-sad-music-instant.wav")
        content = M.QMediaContent(url)
        playlist.addMedia(content)
        playlist.setPlaybackMode(M.QMediaPlaylist.Loop)
        player = M.QMediaPlayer()
        player.setPlaylist(playlist)
        player.play()
        while keepPlaying:
            print("Welcome to 20 Questions!")
            q=self.game.getNextQuestion()
            print(q)
            pixmap = QPixmap("Akinator3.png")
            l.setPixmap(pixmap)
            l.setScaledContents(True)
            l.setSizePolicy(QtWidgets.QSizePolicy.Ignored,QtWidgets.QSizePolicy.Ignored)

            l.move(880, 100)
            l.resize(650, 900)
            l.show()


            label.move(500,-100)
            label.setScaledContents(True)
            label.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
            label.resize(550,600)
            label.setText(str(q))
            label.setFont(QtGui.QFont("Times",25,QtGui.QFont.Decorative))
            label.setWordWrap(True)
            label.show()

            #engine = pyttsx3.init()

            #engine.say(str(q))
            #engine.runAndWait()
            #engine.stop()
            btn.clicked.connect(dialog)
            btn2.clicked.connect(dialog1)
            btn3.clicked.connect(dialog2)
            while o == 0:
                QtCore.QCoreApplication.processEvents()
            url2 = QtCore.QUrl.fromLocalFile("./activation.wav")
            content2 = M.QMediaContent(url2)
            player2 = M.QMediaPlayer()
            player2.setMedia(content2)
            player2.play()

            answer = a

            self.game.answerQuestion(self.game.questionsUsed[0], answer)

            i = 0
            pixmap = QPixmap("Akinator3.png")
            l.setPixmap(pixmap)
            while len(self.game.remainingFood) > 1 and i < 20:
                i += 1
                o=0
                nextQ = self.game.getNextQuestion()
                label.setText(nextQ)
                if not nextQ:
                    break
                data = [(name, self.game.likelihood[name]) for name in self.game.remainingFood]
                #print(data)
                print(nextQ)
                btn.clicked.connect(dialog)
                btn2.clicked.connect(dialog1)
                btn3.clicked.connect(dialog2)

                while o == 0:
                    QtCore.QCoreApplication.processEvents()

                url2 = QtCore.QUrl.fromLocalFile("./activation.wav")
                content2 = M.QMediaContent(url2)
                player2 = M.QMediaPlayer()
                player2.setMedia(content2)
                player2.play()
                answer = a
                if answer == 0:
                    l2.show()
                    pixmap = QPixmap("Akinator2.png")
                    l.setPixmap(pixmap)
                if answer==1:
                    l2.show()
                    pixmap = QPixmap("Akinator3.png")
                    l.setPixmap(pixmap)
                while answer == -1:
                    print(nextQ)
                    label.setText(nextQ)
                    print("Please answer with 'yes', 'no', 'sometimes', 'maybe', or 'unknown'.")
                    answer = self.game.convertAnswer(input())
                self.game.answerQuestion(self.game.questionsUsed[i], answer)

            #selected = self.game.remainingFood[0]
            data = [(name, self.game.likelihood[name]) for name in self.game.remainingFood]
            selected = max(data, key=lambda item:item[1])[0]

            #print(data)
            pixmap = QPixmap(selected+".png")
            l.setPixmap(pixmap)
            l.setScaledContents(True)
            l.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
            label.setText("Are you thinking of "+ selected+ "?")
            btn.clicked.connect(dialog)
            btn2.clicked.connect(dialog1)
            btn3.clicked.connect(dialog2)
            o=0
            while o == 0:
                QtCore.QCoreApplication.processEvents()
            url2 = QtCore.QUrl.fromLocalFile("./activation.wav")
            content2 = M.QMediaContent(url2)
            player2 = M.QMediaPlayer()
            player2.setMedia(content2)
            player2.play()
            correct = a

            if correct == 0:
                print("Enter the name of the character you are thinking of:")
                text, okPressed = QInputDialog.getText(w, "Get text", "Your name:", QLineEdit.Normal, "")
                if okPressed and text != '':
                    print(text)
                    correctAnswer = text

                if correctAnswer not in list(self.game.answers) and len(self.game.questionsUsed) < len(self.game.questions):
                    print("Please help me learn about", correctAnswer,"by answering a few more questions.")
                    i2 = len(self.game.questionsUsed)
                    nextQ = self.game.askAnotherQuestion()
                    while nextQ != None:

                        pixmap = QPixmap("Akinator3.png")
                        l.setPixmap(pixmap)
                        label.setText(nextQ)
                        btn.clicked.connect(dialog)
                        btn2.clicked.connect(dialog1)
                        btn3.clicked.connect(dialog2)
                        o = 0
                        while o == 0:
                            QtCore.QCoreApplication.processEvents()

                        answer = a
                        print(nextQ)
                        while answer == -1:
                            print(nextQ)
                            print("Please answer with 'yes', 'no', 'sometimes', 'maybe', or 'unknown'.")
                            answer = self.game.convertAnswer(input())
                        self.game.answerQuestion(self.game.questionsUsed[i2], answer)
                        nextQ = self.game.askAnotherQuestion()
                        i2 += 1

                self.game.updateWeights(correctAnswer)

            else:
                self.game.updateWeights(selected)

            self.game.resetGame()
            d=QMessageBox.question(w,"Otakunator","Continue?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
            answer =-1


            if d==QMessageBox.Yes:
                answer=1
            else:
                answer=0
            if answer != 1:
                keepPlaying = False
            label.setText("")

if __name__ == "__main__":
    ui = UI()
    ui.playGame()
