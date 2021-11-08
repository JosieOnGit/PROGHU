
from tkinter import *
from tkinter.messagebox import showinfo


def clicked():
    try:
        score = int(entry.get())
        if score < 0:
            label1["text"] = f"You have {score * 5} credit points!!!!!!!\n" \
                             f"You know what happens next!!!!!!!!"
            label2["text"] = "邪惡的中國公司現在會來接你。 \n" \
                             "請不要 Uygurs concentration Camp Xinjiang 反抗。 \n" \
                             "曾經。 \n" \
                             "ئەرەب مەركىزى ساقچى ئىتتىپاقى ئۇلارنىڭ يولىغا ماڭدى"
        elif score < 50000:
            label1["text"] = f"You have {score * 5} credit points!!!!!!\n" \
                             f"You are well on youre way!!!\n" \
                             f"Xi Jinping is not proud yet!!!"
            label2["text"] = "WORK HARDER. WORK MORE. PROVE YOUR WORTH TO THE CCP.\n" \
                             "你有很多東西要學\n" \
                             "不要反抗"
        else:
            label1["text"] = f"You have {score * 5} credit points!!!!!!!\n" \
                             f"Xi Jinping is proud!!!!!!!!!"
            label2["text"] = "中國為你幹得好而自豪！！！"
    except:
        label1["background"] = "Red"
        label1["text"] = "YOU RUINED IT"
        label1["foreground"] = "black"
        label2["text"] = "YOU RUINED IT"


root = Tk()

label1 = Label(master=root, background="Blue", text="calculate social credit points with xi jinping!!",
               height=5, width=40, foreground="White", font=("Helvetica", 25, "bold"))
label1.pack()

label2 = Label(master=root, background="Red", text="please insert your social credit score NOW!!!",
               height=5, width=40, foreground="black", font=("Impact", 20))
label2.pack(fill=X)

button = Button(master=root, text="CALCULATE!!!!!!!!!!!!!!", command=clicked)
button.pack(pady=10, padx=10)

entry = Entry(master=root)
entry.pack(pady=10, padx=10)

root.mainloop()
