import gui.tkinter


def main():
    root = gui.tkinter.Tk()
    canvas = gui.tkinter.Canvas(root)
    canvas.create_line(0, 0, 100, 100)
    canvas.create_line(0, 1, 100, 100)
    canvas.create_line(0, 2, 100, 100)
    canvas.create_arc(0, 5, 100, 100, fill="pink")
    canvas.create_rectangle(50, 100, 200, 200, fill="wheat")
    canvas.create_text(200, 40, text="Hi", font=("Times New Roman", 20))
    canvas.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
