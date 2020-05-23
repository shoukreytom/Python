import gui.tkinter as tk
import gui.tkinter.messagebox as messagebox


root = tk.Tk()


def exitapplication():
    res = messagebox.askquestion("Exit", "Do you want exit?")
    if res == "yes":
        print("Exiting this application")
        exit()
    else:
        messagebox.showinfo("Thanks", "Thanks for your good decision")


def openfile():
    messagebox.showerror("Open File", "Ooops! something went wrong")


def createmenu():
    menu_bar = tk.Menu(root)

    file_menu = tk.Menu(menu_bar, tearoff=False)
    file_menu.add_command(label="Open", command=openfile)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exitapplication)

    menu_bar.add_cascade(label="File", menu=file_menu)

    return menu_bar


def main():
    root.config(menu=createmenu())
    root.mainloop()


if __name__ == "__main__":
    main()
