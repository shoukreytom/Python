import gui.tkinter as tk


def main():
    root = tk.Tk()
    status = tk.Label(root, text="Status:", bd=1, relief=tk.GROOVE, anchor=tk.W)
    status.pack(side=tk.BOTTOM, fill=tk.X)
    root.minsize(600, 400)
    root.mainloop()


if __name__ == '__main__':
    main()
