import tkinter as tk
import tkinter.messagebox as tkm


def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "AC":

        entry.delete(0, tk.END)
        entry.insert(tk.END, res)
    if num =="=":
        siki = entry.get() 
        res = eval(siki) 
        entry.delete(0, tk.END) 
        entry.insert(tk.END, res)
    else:
    
        entry.insert(tk.END, num)


root = tk.Tk()
root.geometry("400x600")


entry = tk.Entry(root, justify="right", width=10, font=("",40))
entry.grid(row=0, column=0, columnspan=4)

r,c=1,1
operators2 = ["AC","**","."]
for ope2 in operators2:
    button = tk.Button(root, text=f"{ope2}", width=4, height=2, font=("",30))
    button.grid(row=r,column=c)
    button.bind("<1>", button_click)
    c+=1

r,c=5,3
operators3 =["=","00"]
for ope3 in operators3:
    button = tk.Button(root, text=f"{ope3}", width=4, height=2, font=("",30))
    button.grid(row=r,column=c)
    button.bind("<1>", button_click)
    c-=2


r ,c = 2, 3
for num in range(9, -1, -1):
    button = tk.Button(root, text=f"{num}", width=4, height=2, font=("",30))
    button.grid(row=r,column=c)
    button.bind("<1>", button_click)
    c-=1
    if c==0:
        r+=1
        c=3
        if r==5:
            c=2


r, c=1, 4
operators = ["","/","*","+","-",]
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("",30))
    button.grid(row=r,column=c)
    button.bind("<1>", button_click)
    c+=1
    if c%1==0:
        r+=1
        c=4

root.mainloop()