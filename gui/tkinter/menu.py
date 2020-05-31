import tkinter as tk


class App(tk.Tk):

    def __init__(self):
        super(App, self).__init__()
        self.__config()
    
    def __create_menu(self):
        # MenuBar
        menu_bar = tk.Menu(self)

        # File Menu
        file_menu = tk.Menu(menu_bar, tearoff=False)

        # Edit Menu
        edit_menu = tk.Menu(menu_bar, tearoff=False)

        # Help Menu
        help_menu = tk.Menu(menu_bar, tearoff=False)

        # adding elements to file menu
        file_menu.add_command(label="New")
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Save As")
        file_menu.add_separator()
        file_menu.add_command(label="Exit")

        # adding elements to edit menu
        edit_menu.add_command(label="Undo")
        edit_menu.add_command(label="Redo")
        edit_menu.add_command(label="Cut")
        edit_menu.add_command(label="Copy")
        edit_menu.add_command(label="Paste")
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All")

        # adding elements to help_menu
        help_menu.add_command(label="Help")
        help_menu.add_command(label="About us")

        # adding menus to menu bar
        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        return menu_bar
    
    def __config(self):
        self.config(menu=self.__create_menu())
    
    def run(self):
        self.mainloop()


def main():
    app = App()
    app.run()


if __name__ == '__main__':
    main()
