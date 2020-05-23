import gui.tkinter as tk
from gui.tkinter import ttk


class App:

    __root = tk.Tk()

    def __init__(self):
        self.__config()
        self.__toolbar().pack(side=tk.TOP, fill=tk.X)
    
    def __toolbar(self):
        main_bar = tk.Frame(self.__root, bd=1, relief=tk.SUNKEN)

        # TooBar for File menu
        file_bar = tk.Frame(main_bar)

        # ToolBar for Edit menu
        edit_bar = tk.Frame(main_bar)

        # adding elements to File Bar
        new_button = tk.Button(file_bar, text="New")
        new_button.pack(side=tk.LEFT)
        open_button = tk.Button(file_bar, text="Open")
        open_button.pack(side=tk.LEFT)
        save_button = tk.Button(file_bar, text="Save")
        save_button.pack(side=tk.LEFT)
        save_all_button = tk.Button(file_bar, text="Save All")
        save_all_button.pack(side=tk.LEFT)

        # adding elements to Edit Bar
        undo_button = tk.Button(edit_bar, text="Undo")
        undo_button.pack(side=tk.LEFT)
        redo_button = tk.Button(edit_bar, text="Redo")
        redo_button.pack(side=tk.LEFT)
        cut_button = tk.Button(edit_bar, text="Cut")
        cut_button.pack(side=tk.LEFT)
        copy_button = tk.Button(edit_bar, text="Copy")
        copy_button.pack(side=tk.LEFT)
        paste_button = tk.Button(edit_bar, text="Paste")
        paste_button.pack(side=tk.LEFT)

        file_bar.pack(side=tk.LEFT)
        edit_bar.pack(side=tk.LEFT, padx=10)

        return main_bar
    
    def __createmenu(self):
        # MenuBar
        menu_bar = tk.Menu(self.__root)

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
        self.__root.config(menu=self.__createmenu())
    
    def run(self):
        self.__root.mainloop()


def main():
    app = App()
    app.run()


if __name__ == '__main__':
    main()
