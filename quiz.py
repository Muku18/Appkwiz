# =====================module import=================================

import time
from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("1174x650+50+0")
root.title("QUIZ APP")
root.resizable(False, False)
root.configure(bg="#074463")
from PIL import Image, ImageTk

image = Image.open("bg1.jpg")
photo = ImageTk.PhotoImage(image)
flag = Label(image=photo, bg="black")
flag.place(x=0, y=0)

image1 = Image.open("download.jpg")
photo1 = ImageTk.PhotoImage(image1)
flag1 = Label(image=photo1, bg="black")
flag1.place(x=425, y=100)

# =============COLOR FUNCTION=========================================
import random

colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']


def color():
    fg = random.choice(colors)
    Sliderlabel.config(fg=fg)
    Sliderlabel.after(2, color)


# =====================================================================


# ==============================INTRO LABEL FUNCTION===================
def introlabel():
    global count, text
    if (count >= len(Ss)):
        count = 0
        text = ''
        Sliderlabel.config(text=text)
    else:
        text = text + Ss[count]
        Sliderlabel.config(text=text)
        count = count + 1
    Sliderlabel.after(200, introlabel)


# ======================================================================

Ss = "TEST YOUR KNOWLEDGE"
text = ''
count = 0

Sliderlabel = Label(root, text=Ss, font=("new times roman", 25, "bold"), bd=5, relief=GROOVE, width=30)
Sliderlabel.pack(side=TOP, fill=X)
introlabel()
color()
AR = "PROGRAMMING PREPARATION WITH CODING GURU"
textlabel = Label(root, bd=5, relief=GROOVE, text=AR, bg="gold", font=("chillar", 20, "bold"))
textlabel.place(x=250, y=300)


# ===================================START_TEST_FUNCTION=================
def start_test():
    res = messagebox.askyesnocancel("Notification", "Do you want to start")
    if (res == True):
        labelrules.destroy()
        labelinstruction.destroy()
        textlabel.destroy()
        startbutton.destroy()
        flag.destroy()
        Sliderlabel.destroy()
        gen()
        startquiz()


# =======================================================================


startbutton = Button(root, command=start_test, activebackground="crimson", text="START", font=("chillar", 15, "bold"),
                     bg="red", bd=5, relief=GROOVE)
startbutton.place(x=525, y=380)

labelinstruction = Label(

    root,
    text="Read the instruction\n and get started by clicking the button",
    font=("chillar", 12, "bold"),
    bg="green",
    border = 4,
    relief = GROOVE,
    width = 40,
    justify="center"
)
labelinstruction.place(x=370, y=450)

rules = '1. This test consists of 20 question\n2. you can start your test after 20 seconds\n3. Total duration 20 minutes\n4. Test will get submitted automatically'

labelrules = Label(
                   root,
                   text=rules,
                   font=("new times roman", 14),
                   width=35,
                   bd=4,
                   relief=GROOVE,
                   justify="center",
                   bg="black",
                   fg="yellow",
                   )
labelrules.place(x=0, y=550, width=1174, height=100)


q1 = """
QUES1: where is function defined??"""

q2 = """
QUES2:   Which method is used to add value to the list at the end?? """

q3 = """
QUES3: which is mutable??
1.List
2.Tuple
3.string
4.Tuple and string both"""

q4 = """
QUES4: Consider A = [34,56,78]
A = A +78 ??"""

q5 = """
QUES5: which method is used to fetch key-value pairs from dictionary??
 """

q6 = """
QUES6:   Can you define as many exception block you want??"""

q7 = """
QUES7: which of the following variable name is not valid??
1.ABC23
2.1WE
3.abc2
4.Aa1
"""

q8 = """
QUES8:  Return type of Math.round() ??"""

q9 = """
QUES9: when does finally block excecute??"""

q10 = """

Ques10:  thislist = ["apple", "banana", "cherry"]
print(thislist[::-1])
output of above code??"""

radiovar = IntVar()
radiovar.set(-1)

Questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

answer_choice = [
    ["class", "Module", "another function", "All of the above"],
    ["pop()", "append()", "extend()", "add()"],
    ["Only 1", "Only 2", "Both 1&2", "All of the above"],
    ["operation performed on the list is correct", "operation performed on the list is Incorrect", "Depends on compiler ", "None of the above"],
    ["keys()", "values()", "items()", "None of the above"],
    ["yes", "No", "compiler dependent", "None of the above"],
    ["Only 1", "Only 2", "Both 1 and 3", "Both 2 and 4"],
    ["int", "float", "string", "None"],
    ["Always", "when exception occcurred", "when no exception occurred", "None"],
    [['apple', 'banana', 'cherry'], ['cherry','apple', 'banana'], ['cherry','banana','apple'], "None"]
]

user_choice = []
indexes = []
correct_answer = [3,1,0,1,2,0,1,1,0,2]


def gen():
    global indexes
    while (len(indexes) < 5):
        x = random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)



ques = 1
def soldestroy():
    finalscore.destroy()
    Labelimage.destroy()
    LabelresultText.destroy()
    solbut.destroy()



def solution():
    with open("sol.txt") as op:
        for lines in op:
            print(lines)


def newwindow(score):
    global  finalscore,Labelimage, LabelresultText,solbut,reswin
    reswin = Toplevel()
    reswin.grab_set()
    reswin.title("Quiz App")
    reswin.geometry("600x400+200+100")
    reswin.config(bg="#074463")
    reswin.resizable(False, False)

    image = Image.open("bg.jpg")
    photo = ImageTk.PhotoImage(image)
    flag = Label(reswin, image=photo, bg="black")
    flag.place(x=0, y=0)
    finalscore = Label(reswin,text=f"YOUR SCORE = {score}/25",border = 8,relief=SUNKEN,bg="black",fg="gold",font=("new times roman",16,"bold"))
    finalscore.pack(pady=10)

    Labelimage = Label(
        reswin,
        background = "black",
    )
    Labelimage.pack(pady=10)


    LabelresultText = Label(
        reswin,
        font = ("new times roman",16,"bold"),
        bg="black",
        fg = "gold",
        bd=4,
        relief = SUNKEN
    )
    LabelresultText.pack(pady=10)
    if(score>=15):

        img = PhotoImage(file = "like.png")
        Labelimage.configure(image=img)
        Labelimage.image = img
        LabelresultText.config(text="welldone!!!")
    else:
        img = PhotoImage(file="sad.png")
        Labelimage.configure(image=img)
        Labelimage.image = img
        LabelresultText.config(text="workhard!!!")

    solbut = Button(
        reswin,
        text = "SOLUTION",
        font = ("new times roman",12,"bold"),
        bd = 3,
        bg="#074463",
        fg="white",
        activebackground = "white",
        relief = SUNKEN,
        command = solution
    )
    solbut.place(x=480,y=350)


    reswin.mainloop()


def showresult(score):
    Datelabel.destroy()
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    newwindow(score)

def calc():
    global indexes,user_choice,answer_choice
    x=0
    score = 0
    for i in indexes:
        if user_choice[x] == correct_answer[i]:
            score = score +5
        x = x+1
    showresult(score)

i=1
j=0
def selected():
    global radiovar, user_choice
    global lblQuestion, r1, r2, r3, r4
    global ques,i,j
    x = radiovar.get()
    radiovar.set(-1)
    user_choice.append(x)



    if ques < 5:
        lblQuestion.config(text=Questions[indexes[ques]])
        r1['text'] = answer_choice[indexes[ques]][0]
        r2['text'] = answer_choice[indexes[ques]][1]
        r3['text'] = answer_choice[indexes[ques]][2]
        r4['text'] = answer_choice[indexes[ques]][3]

        temp = indexes[ques]
        if temp + 1 == 1:
            B1.config(bg='green', activebackground='green', relief=SUNKEN)
        elif temp + 1 == 2:
            B2.config(bg='green', activebackground='green', relief=SUNKEN)
        elif temp + 1 == 3:
            B3.config(bg='green', activebackground='green', relief=SUNKEN)
        elif temp + 1 == 4:
            B4.config(bg='green', activebackground='green', relief=SUNKEN)
        elif temp + 1 == 5:
            B5.config(bg='green', activebackground='green', relief=SUNKEN)
        elif temp + 1 == 6:
            B6.config(bg='green', activebackground='green', relief=SUNKEN)
        elif temp + 1 == 7:
            B7.config(bg='green', activebackground='green', relief=SUNKEN)
        elif temp + 1 == 8:
            B8.config(bg='green', activebackground='green', relief=SUNKEN)
        elif temp + 1 == 9:
            B9.config(bg='green', activebackground='green', relief=SUNKEN)
        else:
            B10.config(bg='green', activebackground='green', relief=SUNKEN)



        ques = ques +1
        NotaB.config(text=5-i)
        AB.config(text=j+1)
        i = i+1
        j+=1


    else:
        NotaB.config(text='0')
        AB.config(text='5')
        calc()



def ques1():
    global B1
    global lblQuestion, r1, r2, r3, r4
    B1.config(bg='green', activebackground='green', relief=SUNKEN)
    lblQuestion.config(text=Questions[0])
    r1['text'] = answer_choice[0][0]
    r2['text'] = answer_choice[0][1]
    r3['text'] = answer_choice[0][2]
    r4['text'] = answer_choice[0][3]

def ques2():
    lblQuestion.config(text=Questions[1])
    r1['text'] = answer_choice[1][0]
    r2['text'] = answer_choice[1][1]
    r3['text'] = answer_choice[1][2]
    r4['text'] = answer_choice[1][3]

def ques3():
    lblQuestion.config(text=Questions[2])
    r1['text'] = answer_choice[2][0]
    r2['text'] = answer_choice[2][1]
    r3['text'] = answer_choice[2][2]
    r4['text'] = answer_choice[2][3]

def ques4():
    lblQuestion.config(text=Questions[3])
    r1['text'] = answer_choice[3][0]
    r2['text'] = answer_choice[3][1]
    r3['text'] = answer_choice[3][2]
    r4['text'] = answer_choice[3][3]

def ques5():
    lblQuestion.config(text=Questions[4])
    r1['text'] = answer_choice[4][0]
    r2['text'] = answer_choice[4][1]
    r3['text'] = answer_choice[4][2]
    r4['text'] = answer_choice[4][3]

def ques6():
    lblQuestion.config(text=Questions[5])
    r1['text'] = answer_choice[5][0]
    r2['text'] = answer_choice[5][1]
    r3['text'] = answer_choice[5][2]
    r4['text'] = answer_choice[5][3]

def ques7():
    lblQuestion.config(text=Questions[6])
    r1['text'] = answer_choice[6][0]
    r2['text'] = answer_choice[6][1]
    r3['text'] = answer_choice[6][2]
    r4['text'] = answer_choice[6][3]

def ques8():
    lblQuestion.config(text=Questions[7])
    r1['text'] = answer_choice[7][0]
    r2['text'] = answer_choice[7][1]
    r3['text'] = answer_choice[7][2]
    r4['text'] = answer_choice[7][3]

def ques9():
    lblQuestion.config(text=Questions[8])
    r1['text'] = answer_choice[8][0]
    r2['text'] = answer_choice[8][1]
    r3['text'] = answer_choice[8][2]
    r4['text'] = answer_choice[8][3]

def ques10():
    lblQuestion.config(text=Questions[9])
    r1['text'] = answer_choice[9][0]
    r2['text'] = answer_choice[9][1]
    r3['text'] = answer_choice[9][2]
    r4['text'] = answer_choice[9][3]


def SaveNext():
    selected()




def clear():
    pass
def Prev():
    pass

def submit():
    if ques<5:
        messagebox.showinfo("showinfo", "COMPLETE THE TEST")
    else:
        selected()



# ========================================================START QUIZ============================================
def startquiz():
    global B1,B2,B3,B4,B5,B6,B7,B8,B9,B10
    global lblQuestion, r1, r2, r3, r4,Datelabel,Questionframe
    global  InitialTime
    global indexes,NotaB,AB

    Notificationframe = Frame(
        root,
        bd=4,
        relief = SUNKEN
    )
    Notificationframe.place(x=0,y=1,width=1174,height=25)

    Questionframe = LabelFrame(
        root,
        bd=4,
        relief=SUNKEN,
        fg="gold"
    )
    Questionframe.place(x=0,y=32,height=380,width=875)

    F5 = Frame(
        root,
        bd=4,
        relief=GROOVE,
    )
    F5.place(x=890, y=164, width=260, height=200)

    status_frame = Frame(
        root,
        bd=4,
        relief=GROOVE,
    ).place(x=890, y=400, width=260, height=240)




    NotaB = Button(
            status_frame
           ,bd=4,
           relief=GROOVE,
           width = 4,
        font=("new times roman", 13, "bold"),
           bg="red",
           text="5")
    NotaB.place(x=900,y=490)

    nAns = Label(
        status_frame,
        text="Not Answered",
        font = ("new times roman",13,"bold"),
        bd=4,
        width=10,
        relief=GROOVE
    ).place(x=980,y=491,width=120)

    AB = Button(
           status_frame
           , bd=4,
           relief=GROOVE,
           width=4,
        font=("new times roman", 13, "bold"),
           bg="green",
           text="0")
    AB.place(x=900, y=550)
    nAns = Label(

        status_frame,
        text="Answered",
        font=("new times roman", 13, "bold"),
        bd=4,
        width = 10,
        relief=GROOVE
    ).place(x=980, y=551, width=120)

    status_Panel = Label(

        status_frame,
        text="Status",
        bd=4,
        font=("new times roman", 14, "bold"),
        relief=GROOVE,
        width = 18
    ).place(x=900,y=420)


    Panel = Label(
        F5,
        text="Question Panel",
        bd=4,
        font=("new times roman", 14, "bold"),
        relief=GROOVE,
    ).pack(fill=X)


    scroll_y = Scrollbar(
        F5,
        orient=VERTICAL,
    )

    textarea = Text(
        F5,
        yscrollcommand=scroll_y.set,
    )
    scroll_y.pack(side=RIGHT, fill=Y)

    scroll_y.config(command=textarea.yview)
    textarea.pack(fill=BOTH, expand=1)

    B1 = Button(textarea,text="1",width=4,bd=2,command=ques1)
    B1.grid(row=0,column=0)


    B2 = Button(textarea, text="2",bd=2, width=4, command=ques2)
    B2.grid(row=0, column=1)


    B3 = Button(textarea, text="3",bd=2, width=4,command=ques3)
    B3.grid(row=0, column=2)

    B4 =  Button(textarea, text="4", bd=2,width=4,command=ques4)
    B4.grid(row=0, column=3)

    B5 = Button(textarea, text="5",bd=2, width=4,command=ques5)
    B5.grid(row=0, column=4)

    B6 = Button(textarea, text="6", bd=2,width=4,command=ques6)
    B6.grid(row=0, column=5)

    B7 = Button(textarea, text="7",bd=2, width=4,command=ques7)
    B7.grid(row=1, column=0)

    B8 = Button(textarea, text="8", bd=2,width=4,command=ques8)
    B8.grid(row=1, column=1)

    B9 = Button(textarea, text="9", bd=2,width=4,command=ques9)
    B9.grid(row=1, column=2)

    B10 = Button(textarea, text="10", bd=2,width=4,command=ques10)
    B10.grid(row=1, column=3)

    Button(textarea, text="11",bd=2, width=4).grid(row=1, column=4)

    Button(textarea, text="12",bd=2, width=4).grid(row=1, column=5)

    Button(textarea, text="13",bd=2, width=4).grid(row=2, column=0)

    Button(textarea, text="14",bd=2, width=4).grid(row=2, column=1)

    Button(textarea, text="15", bd=2,width=4).grid(row=2, column=2)

    Button(textarea, text="16",bd=2, width=4).grid(row=2, column=3)

    Button(textarea, text="17", bd=2,width=4).grid(row=2, column=4)

    Button(textarea, text="18", bd=2,width=4).grid(row=2, column=5)

    Button(textarea, text="19",bd=2, width=4).grid(row=3, column=0)

    Button(textarea, text="20",bd=2, width=4).grid(row=3, column=1)

    Button(textarea, text="21",bd=2, width=4).grid(row=3, column=2)

    Button(textarea, text="22",bd=2, width=4).grid(row=3, column=3)

    Button(textarea, text="23",bd=2, width=4).grid(row=3, column=4)

    Button(textarea, text="24",bd=2, width=4).grid(row=3, column=5)

    Button(textarea, text="25",bd=2, width=4).grid(row=4, column=0)

    Button(textarea, text="26",bd=2, width=4).grid(row=4, column=1)

    Button(textarea, text="27",bd=2, width=4).grid(row=4, column=2)

    Button(textarea, text="28",bd=2, width=4).grid(row=4, column=3)

    Button(textarea, text="29",bd=2, width=4).grid(row=4, column=4)

    Button(textarea, text="30",bd=2, width=4).grid(row=4, column=5)




    lblQuestion = Label(
        Questionframe,
        text=Questions[indexes[0]],
        font=("new times roman", 18),
        bg="white",
        fg="black"
    )
    lblQuestion.place(x=12, y=40, width=850, height=360)

    optionsframe = Frame(
        root,
        bd=4,
        relief=SUNKEN,
    )
    optionsframe.place(x=0, y = 415, width=877, height=230)



    save = Button(optionsframe, text="Save and Next",relief=SUNKEN,bd=4,bg="black",fg="gold",font=("new times roman",11,"bold"),command=SaveNext,width=14)
    save.place(x=25,y=185)

    sub = Button(optionsframe,bd=4,bg="black",fg="gold",font=("new times roman",11,"bold"), text="Submit", command=submit, width=10)
    sub.place(x=760,y=185)


    r1 = Radiobutton(
        optionsframe,
        text=answer_choice[indexes[0]][0],
        font=("new times roman", "12", "bold"),
        value=0,
        bg="white",
        bd=2,
        relief=GROOVE,
        variable=radiovar,

    )
    r1.place(x=28, y=2)

    r2 = Radiobutton(
        optionsframe,
        text=answer_choice[indexes[0]][1],
        font=("new times roman", "12", "bold"),
        value=1,
        bg="white",
        bd=2,
        relief=GROOVE,
        variable=radiovar,

    )
    r2.place(x=28, y=50)

    r3 = Radiobutton(
        optionsframe,
        text=answer_choice[indexes[0]][2],
        font=("new times roman", "12", "bold"),
        value=2,
        bd=2,
        relief=GROOVE,
        variable=radiovar,
        background= "white"
    )
    r3.place(x=28, y=96)

    r4 = Radiobutton(
        optionsframe,
        text=answer_choice[indexes[0]][3],
        font=("new times roman", "12", "bold"),
        value=3,
        bg="white",
        bd=2,
        relief=GROOVE,
        variable=radiovar,
    )
    r4.place(x=28, y=142)

    if indexes[0]+1 == 1:
        B1.config(bg='green', activebackground='green', relief=SUNKEN)
    elif indexes[0] +1 == 2:
        B2.config(bg='green', activebackground='green', relief=SUNKEN)
    elif indexes[0]+1  == 3:
        B3.config(bg='green', activebackground='green', relief=SUNKEN)
    elif indexes[0] +1 == 4:
        B4.config(bg='green', activebackground='green', relief=SUNKEN)
    elif indexes[0]+1  == 5:
        B5.config(bg='green', activebackground='green', relief=SUNKEN)
    elif indexes[0] +1 == 6:
        B6.config(bg='green', activebackground='green', relief=SUNKEN)
    elif indexes[0]+1  == 7:
        B7.config(bg='green', activebackground='green', relief=SUNKEN)
    elif indexes[0]+1  == 8:
        B8.config(bg='green', activebackground='green', relief=SUNKEN)
    elif indexes[0] +1 == 9:
        B9.config(bg='green', activebackground='green', relief=SUNKEN)
    else:
        B10.config(bg='green', activebackground='green', relief=SUNKEN)





    def tick():
        global time_string
        time_string = time.strftime("%H:%M:%S")
        date_string = time.strftime("%d/%m/%Y")
        Datelabel.config(text="Date: " + date_string + "\n" + "Time: " + time_string)
        if (time_string ==   "20:23:30"):
            messagebox.showinfo("showinfo", "Last 5 Minutes Hurry Up!!!")
        Datelabel.after(200, tick)

    Datelabel = Label(root, bg="white", fg="black", font=("new times roman", 15, "bold"), bd=5, relief=GROOVE)
    Datelabel.place(x=935, y=64)
    tick()
# =============================================================================================================





root.mainloop()