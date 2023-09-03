from tkinter import *
import turtle, time, pyttsx3
from selenium import webdriver
import tkinter.ttk as tyu
from csv import *
from deep_translator import GoogleTranslator

# e1, e2,e0,e3 = None, None,None,None
r = Tk()
r.geometry("700x700")
r.title("Web automation")
#r.configure(background="red")
imge = PhotoImage(file=r'G:\c1.png')
lim = Label(r, image=imge)
lim.place(x=0, y=0)
frame1=Frame(r)
frame1.pack(pady=20)
l = Label(r, text="Welcome to the web automation\n", font=25).pack(pady=20)

def selenium():
    PATH = r"G:\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()

    driver.get("https://www.google.com/")
    driver.find_element_by_xpath('//*[@id="gb"]/div/div[2]/a').click()
    driver.implicitly_wait(15)

    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(Username)
    driver.find_element_by_xpath('//*[@id ="identifierNext"]').click()
    driver.find_element_by_xpath('//*[@id ="password"]/div[1]/div / div[1]/input').send_keys(Password)
    driver.find_element_by_xpath('//*[@id ="passwordNext"]').click()

    driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("google classroom")
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]').click()
    #driver.find_element_by_xpath('//*[@id="rso"]/div[2]/div/div/div[1]/div/a/h3').click()
    driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/h3').click()

    time.sleep(7)
    engine = pyttsx3.init()

    # engine.setProperty("rate", 178)
    engine.say("Please click the class you want to join")

    engine.runAndWait()
    time.sleep(10)
    engine = pyttsx3.init()
    engine.say("Click the join button")
    engine.runAndWait()
def Meet_joiner1():
    global Username
    global Password
    Username = e1.get()
    Password = e2.get()
    selenium()
    file1 = open("database.csv", "w", newline='\n')
    csvo = writer(file1)
    csvo.writerow(["Name", "Gmail id", "Password"])
    csvo.writerow([str(e0.get()), str(e1.get()), str(e2.get())])
    file1.close()


def Meet_joiner2():
    file1 = open("database.csv", "r", newline='\n')
    csvo = reader(file1)
    c4 = 0
    for i in csvo:
        if str(e3.get()) == i[0]:
            global Username
            global Password
            Username = i[1]
            Password = i[2]
            selenium()
            break
    if c4 == 0:
        gf = Toplevel(r)
        gf.title("ERROR WINDOW")
        gf.configure(background="red")
        lmao = Label(gf, text="No such user name found").pack()

    file1.close()


def meet():
    f = Toplevel(r)
    f.title("Google meet joiner")
    f.configure(background="yellow")
    f.geometry("700x700")
    l12 = Label(f, text="NAME", font=20).pack()
    global e0
    e0 = Entry(f, width=50)
    e0.pack(pady=20)
    l2 = Label(f, text="GMAIL ID:", font=20).pack()
    global e1
    e1 = Entry(f, width=50)
    e1.pack(pady=20)
    l3 = Label(f, text="PASSWORD:", font=20).pack(pady=10)
    global e2
    e2 = Entry(f, width=50)
    e2.pack(pady=10)
    b3 = Button(f, text="JOIN", padx=80, pady=20, command=Meet_joiner1)
    b3.pack(pady=20)


# new/existing
def exist():
    f2 = Toplevel(r)
    f2.title("EXISTING ACCOUNT")
    f2.geometry('700x700')
    f2.configure(background="black")
    global e3
    lna = Label(f2, text="NAME", font=20).pack()
    e3 = Entry(f2, width=50)
    e3.pack(pady=20)
    b3 = Button(f2, text="JOIN", padx=80, pady=20, command=Meet_joiner2)
    b3.pack(pady=20)


def newex():
    f1 = Toplevel(r)
    f1.configure(background='red')
    f1.title("ACCOUNT")
    f1.geometry('700x700')
    but1 = Button(f1, text="NEW ACCOUNT", padx=20, pady=20, command=meet).pack(pady=10)
    but2 = Button(f1, text="EXISTING ACCOUNT", padx=20, pady=20, command=exist).pack(pady=10)


b1 = Button(r, text="Google meet joiner", padx=20, pady=20, command=newex).pack(pady=10)

engine = pyttsx3.init()


def eye_Ex():
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)  # MAXIMISE THE SCREEN
    turtle.bgcolor("black")
    # SET POSITION OF THE CURSOR
    turtle.up()
    turtle.sety(400)
    turtle.down()

    # CIRCLE - CLOCKWISE AND ANTI-CLOCKWISE
    def rotation():
        m = 0
        while m <= 9:
            if m <= 4:
                turtle.color(colours[m])
                for i in range(360):
                    turtle.speed(0)  # MAXIMUM SPEED
                    turtle.pensize(6)  # THICKNESS OF THE CURSOR
                    turtle.forward(6)
                    turtle.right(1)

            elif m == 5:
                turtle.clear()  # CLEARS THE DRAWING
                engine.say("RELAX ")
                engine.runAndWait()
                time.sleep(10)  # BREAK FOR 10 SECS
            else:
                turtle.color(colours[m])
                for i in range(360):
                    turtle.speed(0)
                    turtle.pensize(6)
                    turtle.backward(7)
                    turtle.left(1)
            m += 1

    colours = ("red", "pink", "aqua", "yellow", "white", "red", "pink", "aqua", "yellow", "white")
    rotation()
    turtle.clear()
    engine.say("RELAX ")
    engine.runAndWait()
    time.sleep(10)

    turtle.up()
    turtle.setx(-700)
    turtle.sety(100)
    turtle.down()

    # LINE - LEFT TO RIGHT AND VICE-VERSA
    def straight():
        m = 1
        while m <= 10:
            turtle.speed(1)  # MINIMUM SPEED
            turtle.pensize(10)
            if m % 2 != 0:
                turtle.color("red")
                turtle.forward(1400)
            else:
                turtle.color("white")
                turtle.backward(1400)
            m += 1
        engine.say("RELAX ")
        engine.runAndWait()
        time.sleep(10)

    straight()

    turtle.clear()
    turtle.done()


def eye_ex_instr():
    new_win = Toplevel(r)
    new_win.title("INSTRUCTIONS")
    new_win.geometry('700x700')
    new_win.configure(background="blue")
    label1 = Label(new_win,
                   text="Instructions\n\n1.Remove the spectacles (if wearing)\n\n2.Keep your hands in Chin Mudra\n\n3.Stay away from distractions (or) disturbances\n\n4.Close your eyes for 10 seconds after each exercise",
                   font=25).pack()
    start = Button(new_win, text="START", padx=20, pady=20, command=eye_Ex).pack(pady=20)


b2 = Button(r, text="Eye exercise", padx=38, pady=20, command=eye_ex_instr).pack(pady=10)


def translator():
    new_win = Toplevel(r)
    new_win.title("Translator")
    new_win.configure(background="blue")
    Lab = Label(new_win, text="SELECT INPUT LANGUAGE", font=25).pack()
    l = ["SELECT LANGUAGE", "TAMIL", "TELUGU", "SPANISH", "PUNJABI", "ENGLISH", "MALAYALAM", "LATIN", "ITALIAN",
         "HINDI", "GERMAN", "FRENCH", "DUTCH"]
    O1 = tyu.Combobox(new_win, value=l, font=20)
    O1.current(0)
    O1.pack(pady=20)
    Lab = Label(new_win, text="ENTER INPUT CONTENT", font=25).pack()
    ed = Entry(new_win, width=50)
    ed.pack(pady=20)
    Lab = Label(new_win, text="SELECT OUTPUT LANGUAGE", font=25).pack()
    O2 = tyu.Combobox(new_win, value=l, font=20)
    O2.current(0)
    O2.pack(pady=20)
    dicti = {"TAMIL": "ta", "TELUGU": "te", "SPANISH": "es", "PUNJABI": "pa", "MALAYALAM": "ml", "LATIN": "la",
             "HINDI": "hi", "GERMAN": "de",
             "FRENCH": "fr", "ENGLISH": "en", "DUTCH": "nl", "ITALIAN": "it"}

    def translate():
        newwin = Toplevel(r)
        newwin.title("OUTPUT WINDOW")
        newwin.configure(background="green")
        newwin.geometry('500x500')
        output = O2.get()
        input1 = O1.get()
        content = ed.get()
        for i in dicti:
            if str(output) == i:
                translated = GoogleTranslator(source=dicti[input1], target=dicti[i]).translate(content)
        lb2 = Label(newwin, text=str(translated), font=30).pack()

    b4 = Button(new_win, text="TRANSLATE", padx=35, pady=20, command=translate).pack(pady=10)


B3 = Button(r, text="Translator", padx=38, pady=20, command=translator).pack(pady=10)
r.mainloop()

