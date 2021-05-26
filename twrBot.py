from tkinter import *
canvas = Tk()
canvas.title("TWR chatbot - by ASTIN")
canvas.geometry('600x600')
f = ('Free Mono', 25, 'normal')
def tab1():
    def tab2():
        label1.destroy()
        button1.destroy()
        label2 = Label(canvas, text = 'Welcome to TWR chatbot', font=f)
        label2.pack()
        def close():
            canvas.destroy()
        def send():
            x=0
            x+=x
            send="You => "+e.get()
            txt.insert(END,'\n'+send)
            if (e.get()== "hi"):
                txt.insert(END,'\n'+"Bot =>  Hello Before chatting with me..,"+'\n'+"please check my Hot words"+"\n"+"If checked please reply checked")
                button22 = Button(canvas, text='END', font= f,command=close)
                button22.pack(side = LEFT)
            elif (e.get()== 'checked'):
                txt.insert(END,'\n'+'Bot =>  Thanks for understanding the keywords pls tell me...'+'\n'+'How can I help You')
            elif (e.get()== 'menu'):
                txt.insert(END,'\n'+'Bot =>  Please make yourself comfortable with our Menu '+"\n"+"     a. DOSA set - Rs.25"+"\n"+"     b. CHAPATI set - Rs.30"+"\n"+"     c. MEALS - Rs.90"+"\n"+"     d. Half MEALS - Rs.50")
            elif (e.get()== 'e'):
                txt.insert(END,'\n'+'Bot =>  Police Control Room- 100'+"\n"+'Fire Control Room -101'+"\n"+"Ambulance Helpline-102"+"\n"+'Centralised Accident & Trauma Services (CATS)-1099'+"\n"+"Women's Helpline-1091"+"\n"+"Women's Helpline Anywhere in India-181"+"\n"+'Senior Citizen Helpline-1091, 1291'+"\n"+'Anti-Obscene Calls Cell -1091'+'\n'+'Anti-Stalking Cell-1091'+'\n'+'AIDS Helpline (India)-1097'+'\n'+'Medical Helpline State -108'+'\n'+'Anti-Poison-1066'+'\n'+'Fire Control Room -101')
            elif (e.get()=='r'):
                txt.insert(END,'\n'+'Bot =>  Small room - Rs.500/day'+'\n'+'Medium room - Rs.950/day'+'\n'+"King's room - Rs.1700/day")
            elif (e.get()=='p'):
                txt.insert(END,'\n'+'Bot =>  Maps show the parks locations near our hotels much clear'+"\n" +'get one from the attendant...')
            elif (e.get()=='s'):
                txt.insert(END,'\n'+"Bot =>  Swimming pools are closed due to Corona")
            else:
                txt.insert(END,'\n'+"invalid keyword")
            e.delete(0,END)
        txt = Text(canvas)
        txt.pack()
        hbar = Scrollbar(canvas,orient=VERTICAL)
        hbar.pack(side=RIGHT,fill=Y)
        hbar.config(command=txt.yview)
        txt.config(yscrollcommand=hbar.set)
        e=Entry(canvas, width=100)
        e.pack()
        button2 = Button(canvas, text = "Send", font=f, command=send)
        button2.pack()
    label1 = Label(canvas, text = 'Welcome to TWR Hotel'+'\n'+"please switch to fullscreen", font=f)
    label1.pack()
    label12 = Label(canvas, text = "The hotwords of the chatbot are given below"+'\n'+"*hi - greeting word"+'\n'+"*checked - confirmation word"+'\n'+"*menu - provides the menu"+'\n'+"*e - provides the emergency numbers"+'\n'+"*r - provides the room details"+'\n'+"*p - provides info on park"+'\n'+"*s - updates info on swimming pool")
    label12.pack()
    button1 = Button(canvas, text = "Enter", font=f, command=tab2)
    button1.pack(side=BOTTOM)
tab1()
canvas.mainloop()