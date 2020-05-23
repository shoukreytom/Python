import gui.tkinter as tk


root = tk.Tk()
root.minsize(500, 500)


def main():
    hello = tk.Button(root, text="Hello World")
    hello.config(font=("Arial", 14))
    hello.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
