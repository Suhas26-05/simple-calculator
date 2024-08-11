# Python program to create a simple GUI 
# calculator using Tkinter 

# import everything from tkinter module 
from tkinter import *

# globally declare the expression variable 
# This will store the expression entered by the user
expression = "" 


# Function to update the expression 
# in the text entry box 
def press(num): 
    # point out the global expression variable 
    global expression 

    # concatenation of string 
    # Append the pressed button's value to the expression string
    expression = expression + str(num) 

    # update the expression by using set method 
    # Update the entry box to show the current expression
    equation.set(expression) 


# Function to evaluate the final expression 
def equalpress(): 
    # Try and except statement is used 
    # for handling errors like zero 
    # division error etc. 

    try: 
        global expression 

        # eval function evaluates the expression 
        # and str function converts the result 
        # into string 
        total = str(eval(expression)) 

        # Display the result in the entry box
        equation.set(total) 

        # Reset the expression variable 
        expression = "" 

    # Handle errors like division by zero
    except: 
        # If an error occurs, show an error message
        equation.set(" error ") 
        expression = "" 


# Function to clear the contents 
# of the text entry box 
def clear(): 
    global expression 
    # Clear the expression
    expression = "" 
    # Clear the entry box
    equation.set("") 


# Driver code 
if __name__ == "__main__": 
    # create a GUI window 
    gui = Tk() 

    # set the background color of the GUI window 
    gui.configure(background="Black") 

    # set the title of the GUI window 
    gui.title("Simple Calculator") 

    # set the size/configuration of the GUI window 
    gui.geometry("550x400") 

    # StringVar() is the variable class 
    # We create an instance of this class 
    equation = StringVar() 

    # create the text entry box for 
    # showing the expression 
    expression_field = Entry(gui, textvariable=equation) 

    # Use grid method to place widgets 
    # at respective positions in a table-like structure 
    expression_field.grid(columnspan=10, ipadx=200, pady=10, padx=10)

    # create Buttons and place them at particular 
    # locations inside the window. 
    # when user presses a button, the command or 
    # function associated with that button is executed. 
    button1 = Button(gui, text=' 1 ', fg='black', bg='white', 
                    command=lambda: press(1), height=4, width=15) 
    button1.grid(row=2, column=0, padx=10) 

    button2 = Button(gui, text=' 2 ', fg='black', bg='white', 
                    command=lambda: press(2), height=4, width=15) 
    button2.grid(row=2, column=1, padx=10) 

    button3 = Button(gui, text=' 3 ', fg='black', bg='white', 
                    command=lambda: press(3), height=4, width=15) 
    button3.grid(row=2, column=2, padx=10) 

    button4 = Button(gui, text=' 4 ', fg='black', bg='white', 
                    command=lambda: press(4), height=4, width=15) 
    button4.grid(row=3, column=0, padx=10) 

    button5 = Button(gui, text=' 5 ', fg='black', bg='white', 
                    command=lambda: press(5), height=4, width=15) 
    button5.grid(row=3, column=1, padx=10) 

    button6 = Button(gui, text=' 6 ', fg='black', bg='white', 
                    command=lambda: press(6), height=4, width=15) 
    button6.grid(row=3, column=2, padx=10) 

    button7 = Button(gui, text=' 7 ', fg='black', bg='white', 
                    command=lambda: press(7), height=4, width=15) 
    button7.grid(row=4, column=0, padx=10) 

    button8 = Button(gui, text=' 8 ', fg='black', bg='white', 
                    command=lambda: press(8), height=4, width=15) 
    button8.grid(row=4, column=1, padx=10) 

    button9 = Button(gui, text=' 9 ', fg='black', bg='white', 
                    command=lambda: press(9), height=4, width=15) 
    button9.grid(row=4, column=2, padx=10) 

    button0 = Button(gui, text=' 0 ', fg='black', bg='white', 
                    command=lambda: press(0), height=4, width=15) 
    button0.grid(row=5, column=1, padx=10) 

    plus = Button(gui, text=' + ', fg='black', bg='white', 
                command=lambda: press("+"), height=4, width=15) 
    plus.grid(row=2, column=3, padx=10) 

    minus = Button(gui, text=' - ', fg='black', bg='white', 
                command=lambda: press("-"), height=4, width=15) 
    minus.grid(row=3, column=3, padx=10) 

    multiply = Button(gui, text=' * ', fg='black', bg='white', 
                    command=lambda: press("*"), height=4, width=15) 
    multiply.grid(row=4, column=3, padx=10) 

    divide = Button(gui, text=' / ', fg='black', bg='white', 
                    command=lambda: press("/"), height=4, width=15) 
    divide.grid(row=5, column=3, padx=10) 

    equal = Button(gui, text=' = ', fg='black', bg='white', 
                command=equalpress, height=4, width=15) 
    equal.grid(row=5, column=2, padx=10) 

    clear = Button(gui, text='Clear', fg='black', bg='white', 
                command=clear, height=4, width=15) 
    clear.grid(row=7, column='1', padx=10) 

    Decimal = Button(gui, text='.', fg='black', bg='white', 
                    command=lambda: press('.'), height=4, width=15) 
    Decimal.grid(row=5, column=0, padx=10) 

    # start the GUI event loop 
    gui.mainloop() 
