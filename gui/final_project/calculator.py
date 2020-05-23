import tkinter as tk
from tkinter import ttk
import parser


class Calculator:
    __i = 0
    __root = tk.Tk()
    __display = tk.Entry(__root)

    def __init__(self):
        self.__config()
        self.__layout()
    
    def __layout(self):
        self.__display.grid(row=1, columnspan=6, sticky=tk.W+tk.E, ipady=15, padx=2)

        ttk.Button(self.__root, text="1", command=lambda: self.__get_variables(1), width=10)\
            .grid(row=2, column=0, ipady=5, padx=2)
        ttk.Button(self.__root, text="2", command=lambda: self.__get_variables(2), width=10)\
            .grid(row=2, column=1, ipady=5, padx=2)
        ttk.Button(self.__root, text="3", command=lambda: self.__get_variables(3), width=10)\
            .grid(row=2, column=2, ipady=5, padx=2)

        ttk.Button(self.__root, text="4", command=lambda: self.__get_variables(4), width=10)\
            .grid(row=3, column=0, pady=5, ipady=5, padx=2)
        ttk.Button(self.__root, text="5", command=lambda: self.__get_variables(5), width=10)\
            .grid(row=3, column=1, ipady=5, pady=2, padx=2)
        ttk.Button(self.__root, text="6", command=lambda: self.__get_variables(6), width=10)\
            .grid(row=3, column=2, ipady=5, pady=2, padx=2)

        ttk.Button(self.__root, text="7", command=lambda: self.__get_variables(7), width=10)\
            .grid(row=4, column=0, ipady=5, pady=2, padx=2)
        ttk.Button(self.__root, text="8", command=lambda: self.__get_variables(8), width=10)\
            .grid(row=4, column=1, ipady=5, pady=2, padx=2)
        ttk.Button(self.__root, text="9", command=lambda: self.__get_variables(9), width=10)\
            .grid(row=4, column=2, ipady=5, pady=2, padx=2)
        ttk.Button(self.__root, text="AC", command=lambda: self.__clear_all(), width=10)\
            .grid(row=5, column=0, ipady=5, pady=2, padx=2)
        ttk.Button(self.__root, text="0", command=lambda: self.__get_variables(0), width=10)\
            .grid(row=5, column=1, ipady=5, pady=2, padx=2)
        ttk.Button(self.__root, text="=", command=lambda: self.__calculate(), width=10)\
            .grid(row=5, column=2, ipady=5, pady=2, padx=2)

        ttk.Button(self.__root, text="+", command=lambda: self.__get_operation("+"), width=10)\
            .grid(row=2, column=3, ipady=5, pady=2, padx=2)
        ttk.Button(self.__root, text="-", command=lambda: self.__get_operation("-"), width=10)\
            .grid(row=3, column=3, ipady=5, pady=2, padx=2)
        ttk.Button(self.__root, text="*", command=lambda: self.__get_operation("*"), width=10)\
            .grid(row=4, column=3, ipady=5, pady=2, padx=2)
        ttk.Button(self.__root, text="/", command=lambda: self.__get_operation("/"), width=10)\
            .grid(row=5, column=3, ipady=5, pady=2, padx=2)

        # adding new operations
        ttk.Button(self.__root, text="pi", command=lambda: self.__get_operation("*3.14"), width=10).\
            grid(row=2, column=4, ipady=5, pady=2, padx=2)
        ttk.Button(self.__root, text="%", command=lambda: self.__get_operation("%"), width=10)\
            .grid(row=3, column=4, ipady=5, pady=2, padx=2)
        ttk.Button(self.__root, text="(", command=lambda: self.__get_operation("("), width=10)\
            .grid(row=4, column=4, ipady=5, pady=2, padx=2)
        ttk.Button(self.__root, text="exp", command=lambda: self.__get_operation("**"), width=10)\
            .grid(row=5, column=4, ipady=5, pady=2, padx=2)

        ttk.Button(self.__root, text="<-", command=lambda: self.__undo(), width=10)\
            .grid(row=2, column=5, ipady=5, pady=2, padx=2)
        ttk.Button(self.__root, text="x!", width=10)\
            .grid(row=3, column=5, ipady=5, pady=2, padx=2)
        ttk.Button(self.__root, text=")", command=lambda: self.__get_operation(")"), width=10)\
            .grid(row=4, column=5, ipady=5, pady=2, padx=2)
        ttk.Button(self.__root, text="^2", command=lambda: self.__get_operation("**2"), width=10)\
            .grid(row=5, column=5, ipady=5, pady=2, padx=2)

    # get the user input and place it in the textfield
    def __get_variables(self, num):
        self.__display.insert(self.__i, num)
        self.__i += 1
    
    def __get_operation(self, operator):
        length = len(operator)
        self.__display.insert(self.__i, operator)
        self.__i += length
    
    def __calculate(self):
        entire_string = self.__display.get()
        try:
            a = parser.expr(entire_string).compile()
            result = eval(a)
            self.__clear_all()
            self.__display.insert(0, result)
        except SyntaxError:
            self.__clear_all()
            self.__display.insert(0, "Error")

    def __clear_all(self):
        self.__display.delete(0,tk.END)

    def __undo(self):
        entire_string = self.__display.get()
        if len(entire_string):
            new_string = entire_string[:-1]
            self.__clear_all()
            self.__display.insert(0, new_string)
        else:
            self.__clear_all()
            self.__display.insert(0, "Error")
    
    # TODO: implement Factory
    def __factory(self):
        pass

    # add configuration to the app
    def __config(self):
        self.__root.maxsize(570, 238)
        self.__root.resizable(width=False, height=False)
        self.__display.config(font=("Arial", 18))
        self.__root.title('Calculator')

    def run(self):
        self.__root.mainloop()
