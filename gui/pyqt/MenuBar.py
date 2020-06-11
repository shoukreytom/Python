import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("MenuBar")
        self.setGeometry(50, 50, 500, 300)
        self.new = QAction("&New")
        self.open = QAction("&Open")
        self.save = QAction("&Save")
        self.save_as = QAction("Save As")
        self.quit = QAction("&Quit")
        self.undo = QAction("&Undo")
        self.redo = QAction("&Redo")
        self.copy = QAction("&Copy")
        self.cut = QAction("Cu&t")
        self.paste = QAction("&Paste")
        self.select = QAction("Select &All")
        self.toolbar = QAction("ToolBar")
        self.new_window = QAction("New Window")
        self.preferences = QAction("Preferences")
        self.about = QAction("About")
        self.setup_menu()
        self.menu_bar()

    def setup_menu(self):
        self.new.setShortcut(QKeySequence.New)
        self.open.setShortcut(QKeySequence.Open)
        self.save.setShortcut(QKeySequence.Save)
        self.save_as.setShortcut(QKeySequence.SaveAs)
        self.quit.setShortcut(QKeySequence.Quit)
        self.undo.setShortcut(QKeySequence.Undo)
        self.redo.setShortcut(QKeySequence.Redo)
        self.copy.setShortcut(QKeySequence.Copy)
        self.cut.setShortcut(QKeySequence.Cut)
        self.paste.setShortcut(QKeySequence.Paste)
        self.select.setShortcut(QKeySequence.SelectAll)
        self.toolbar.setCheckable(True)
        self.preferences.setShortcut(QKeySequence.Preferences)
        self.about.setShortcut(QKeySequence.HelpContents)

    def menu_bar(self):
        file = self.menuBar().addMenu("&File")
        file.addAction(self.new)
        file.addAction(self.open)
        file.addAction(self.save)
        file.addAction(self.save_as)
        file.addSeparator()
        file.addAction(self.quit)

        edit = self.menuBar().addMenu("&Edit")
        edit.addAction(self.undo)
        edit.addAction(self.redo)
        edit.addAction(self.copy)
        edit.addAction(self.cut)
        edit.addAction(self.paste)
        edit.addSeparator()
        edit.addAction(self.select)

        view = self.menuBar().addMenu("&View")
        view.addAction(self.toolbar)

        window = self.menuBar().addMenu("&Window")
        window.addAction(self.new_window)
        window.addAction(self.preferences)

        help_ = self.menuBar().addMenu("&Help")
        help_.addAction(self.about)

    @staticmethod
    def new_file():
        print("Hi new")


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
