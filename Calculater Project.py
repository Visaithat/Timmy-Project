from tkinter import *
root = Tk()
root.title("Calculator")


content = "" # ใช้เก็บสะมะการ
txt_input = StringVar(value = "0") # ใช้เมื่อตอนคำนวน

def deleteText():
    display.delete(0,END)
def btn(number):
    global content
    content = content + str(number)
    txt_input.set(content)
def equal():
    global content
    try:
        calculate = float(eval(content))
        txt_input.set(calculate)
        content = ""
    except ZeroDivisionError:
        txt_input.set("ไม่มีค่า")
        content = ""
    
    

# output 5 x 4
display = Entry(font=("arial",30,"bold"),fg="white",bg="green",textvariable=txt_input,justify="right")
display.grid(columnspan=4)


# รับค่าผ่านปุ่ม


#row1
btn7 = Button(fg="black",font=("arial",30,"bold"),text="7",padx=30,pady=15,command=lambda:btn(7)).grid(row=1,column=0)
btn8 = Button(fg="black",font=("arial",30,"bold"),text="8",padx=30,pady=15,command=lambda:btn(8)).grid(row=1,column=1)
btn9 = Button(fg="black",font=("arial",30,"bold"),text="9",padx=30,pady=15,command=lambda:btn(9)).grid(row=1,column=2)
btnc = Button(fg="black",font=("arial",30,"bold"),text="C",padx=30,pady=15,bg="orange",command=deleteText).grid(row=1,column=3)
#row2
btn4 = Button(fg="black",font=("arial",30,"bold"),text="4",padx=30,pady=15,command=lambda:btn(4)).grid(row=2,column=0)
btn5 = Button(fg="black",font=("arial",30,"bold"),text="5",padx=30,pady=15,command=lambda:btn(5)).grid(row=2,column=1)
btn6 = Button(fg="black",font=("arial",30,"bold"),text="6",padx=30,pady=15,command=lambda:btn(6)).grid(row=2,column=2)
btnx = Button(fg="black",font=("arial",30,"bold"),text="x",padx=35,pady=15,bg="orange",command=lambda:btn("*")).grid(row=2,column=3)
#row3
btn1 = Button(fg="black",font=("arial",30,"bold"),text="1",padx=30,pady=15,command=lambda:btn(1)).grid(row=3,column=0)
btn2 = Button(fg="black",font=("arial",30,"bold"),text="2",padx=30,pady=15,command=lambda:btn(2)).grid(row=3,column=1)
btn3 = Button(fg="black",font=("arial",30,"bold"),text="3",padx=30,pady=15,command=lambda:btn(3)).grid(row=3,column=2)
btnplus = Button(fg="black",font=("arial",30,"bold"),text="+",padx=35,pady=15,bg="orange",command=lambda:btn("+")).grid(row=3,column=3)
#row4
btndot = Button(fg="black",font=("arial",30,"bold"),text=".",padx=35,pady=15,bg="orange",command=lambda:btn(".")).grid(row=4,column=0)
btn0 = Button(fg="black",font=("arial",30,"bold"),text="0",padx=30,pady=15,command=lambda:btn(0)).grid(row=4,column=1)
btnหาร = Button(fg="black",font=("arial",30,"bold"),text="/",padx=35,pady=15,bg="orange",command=lambda:btn("/")).grid(row=4,column=2)
btnminus = Button(fg="black",font=("arial",30,"bold"),text="-",padx=40,pady=15,bg="orange",command=lambda:btn("-")).grid(row=4,column=3)
#row5
btnequal = Button(fg="black",font=("arial",30,"bold"),text="=",padx=90,pady=15,bg="orange",command=equal).grid(row=5,column=0,columnspan=2)
btnopen = Button(fg="black",font=("arial",30,"bold"),text="(",padx=35,pady=15,bg="orange",command=lambda:btn("(")).grid(row=5,column=2)
btnclose = Button(fg="black",font=("arial",30,"bold"),text=")",padx=40,pady=15,bg="orange",command=lambda:btn(")")).grid(row=5,column=3)

root.mainloop()