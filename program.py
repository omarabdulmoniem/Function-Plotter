import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Function Plotter')
root.geometry("1200x600")


# Error handling function
def error():
    # equation check
    exp = "+-*/^"
    temp = str(func.get())
    wrong = ""
    wrong_repeat = ""
    for i in range(len(temp)):
        if ((not (temp[i].isdigit())) and (temp[i] != 'x' and temp[i] != '+' and temp[i] != '-' and temp[i] != '*' and temp[i] != '/' and temp[i] != '^')) :
            wrong+= "'"+ temp[i] + "'" +' '
        elif i != len(temp)-1 and temp[i] in exp and temp[i+1] in exp:
            if temp[i] == temp[i+1] :
                wrong_repeat+= "'repetition of "+"'"+ temp[i] + "''" +' '
            else:
                wrong+= "'"+ temp[i] + temp[i+1] + "'"
    
    # limits of x check
    minlimit = str(xmin.get())
    maxlimit = str(xmax.get())
    wrong_min = ""
    wrong_max = ""
    for i in range(len(minlimit)):
        if not minlimit[i].isdigit() and minlimit[i] != '-':
            wrong_min+= "'"+minlimit[i]+"'"+' '
    
    for i in range(len(maxlimit)):
        if not maxlimit[i].isdigit() and maxlimit[i] != '-' :
            wrong_max+= "'" + maxlimit[i] + "'" +' '

    # Displaying error messages
    if len(wrong) != 0:
        messagebox.showerror("Error","Invalid input " + wrong + " ! Please make sure your equation is in terms of x and written correctly!")
    if len(wrong_repeat) != 0:
        messagebox.showerror("Error","Invalid input " + wrong_repeat + " ! Please make sure your equation is in terms of x and written correctly!")
    if len(wrong_min) != 0:
        messagebox.showerror("Error","Invalid minimum limit " + wrong_min + " ! Please enter a valid number!")
    if len(wrong_max) != 0:
        messagebox.showerror("Error","Invalid maximum limit " + wrong_max + " ! Please enter a valid number!")
        


# Plotting function
def plot():

    try:
        # Creating vectors X and Y
        x = np.linspace(float(xmin.get()), float(xmax.get()), 200)
        temp = str(func.get()).replace('^','**')

        y = eval(temp)


        fig = plt.figure(figsize = (10, 5))
        # Create the plot
        func_exp = 'y = ' + str(func.get())
        plt.plot(x, y)

        # configuring axies limits and labels
        leftlim = float(xmin.get())
        rightlim = float(xmax.get())
        leftlim-=2
        rightlim+=2

        ylimits = [leftlim*2,rightlim*2]

        plt.xlim([leftlim , rightlim])
        plt.ylim(ylimits)

        plt.title(func_exp)

        plt.xlabel('x axis')
        plt.ylabel('y axis')

        # Add a grid
        plt.grid(alpha =.6, linestyle ='-')

        
        # Show the plot
        plt.show()
    except:
        error()


# Main window 

# Main label
wel_label = Label(root,text='Please Enter the function here',font='Arial')
wel_label.place(anchor = CENTER, relx = .5, rely = .1)

#  supported operations 
op_label = Label(root,text='Supported operations: + , - , / , * , ^',font=('Arial',9))
op_label.place(anchor = CENTER, relx = .5, rely = .15)

# Function entry
func = Entry(root,width=50,fg='black',font=('Arial',18))
func.place(anchor = CENTER, relx = .5, rely = .2)

# Getting minimum value of x
xmin_label = Label(root,text='Minimum value of x ',font=('Arial',12))
xmin_label.place(anchor = CENTER, relx = .25, rely = .3)

xmin = Entry(root,width=20,fg='black',font=('Arial',12))
xmin.place(anchor = CENTER, relx = .4, rely = .3)

# Getting maximum value of x
xmax_label = Label(root,text='Maximum value of x ',font=('Arial',12))
xmax_label.place(anchor = CENTER, relx = .6, rely = .3)

xmax = Entry(root,width=20,fg='black',font=('Arial',12))
xmax.place(anchor = CENTER, relx = .75, rely = .3)

# Plot button
but = Button(root,text="Plot",padx=10,pady=10,bg='white',fg='black',command=plot)
but.place(anchor = CENTER, relx = .45, rely = .5)

# Exit button
exit_button = Button(root,text="Exit",padx=10,pady=10,bg='white',fg='red',command= root.quit)
exit_button.place(anchor = CENTER, relx = .55, rely = .5)


root.mainloop()
