import tkinter as tk
import random
import time 

window = tk.Tk()
window.geometry('600x400')
#generating a list of five different numbers to randomize the order of questions
list_of_num = random.sample(range(1,6),5)
#start with the first number on the list
i = 0
x = list_of_num[i]

#changing the colors of the buttons when they are clicked (right=green, wrong=red)
def right_answer():
    global right_option
    global option1
    global option2
    right_option.configure(bg='Green')
    right_option.configure(state='disabled')
    option1.configure(state='disabled')
    option2.configure(state='disabled')
    delay()
   
def wrong_answer1():
    global right_option
    global option1
    global option2
    option1.configure(bg='Red')
    right_option.configure(bg='Green')
    right_option.configure(state='disabled')
    option1.configure(state='disabled')
    option2.configure(state='disabled')
    delay()
    
def wrong_answer2():
    global right_option
    global option1
    global option2
    option2.configure(bg='Red')
    right_option.configure(bg='Green')
    right_option.configure(state='disabled')
    option1.configure(state='disabled')
    option2.configure(state='disabled')
    delay()
    
def next_question():
    global i
    if i < 4:
        i += 1
        x = list_of_num[i]
        Question(x)
    else:
        # End of the quiz, display a message or close the window
        print("End of quiz")
        
def delay():
    # Delay for 3 seconds
    window.after(3000, next_question)

#putting all our questions in a function, and questions will be called when their according number is up
def Question(x):
    global option1
    global option2
    global right_option
    if x==1:
        question = tk.Label(window,text='How to read 烏丸?',font='Times 40')
        right_option = tk.Button(window,text='Karasuma',command=delay1,width=25,height=10)
        option1 = tk.Button(window,text='Kuromaru',command=wrong_answer1,width=25,height=10)
        option2 = tk.Button(window,text='Kurosuma',command=wrong_answer2,width=25,height=10)
        question.grid(row=0,column=0,columnspan=3)
        right_option.grid(row=1,column=0)
        option1.grid(row=1,column=1)
        option2.grid(row=1,column=2)
    if x==2:
        question = tk.Label(window,text='How to read 蹴上?',font='Times 40')
        right_option = tk.Button(window,text='Keage',command=right_answer,width=25,height=10)
        option1 = tk.Button(window,text='Keue',command=wrong_answer1,width=25,height=10)
        option2 = tk.Button(window,text='Kuage',command=wrong_answer2,width=25,height=10)
        question.grid(row=0,column=0,columnspan=3)
        right_option.grid(row=1,column=0)
        option1.grid(row=1,column=1)
        option2.grid(row=1,column=2)
    if x==3:
        question = tk.Label(window,text='How to read 糺の森?',font='Times 40')
        right_option = tk.Button(window,text='Tadasunomori',command=right_answer,width=25,height=10)
        option1 = tk.Button(window,text='Azananomori',command=wrong_answer1,width=25,height=10)
        option2 = tk.Button(window,text='Kyunomori',command=wrong_answer2,width=25,height=10)
        question.grid(row=0,column=0,columnspan=3)
        right_option.grid(row=1,column=0)
        option1.grid(row=1,column=1)
        option2.grid(row=1,column=2)
    if x==4:
        question = tk.Label(window,text='How to read 丸太町?',font='Times 40')
        right_option = tk.Button(window,text='Marutamachi',command=right_answer,width=25,height=10)
        option1 = tk.Button(window,text='Tamatamachi',command=wrong_answer1,width=25,height=10)
        option2 = tk.Button(window,text='Marufutomachi',command=wrong_answer2,width=25,height=10)
        question.grid(row=0,column=0,columnspan=3)
        right_option.grid(row=1,column=1)
        option1.grid(row=1,column=0)
        option2.grid(row=1,column=2)
    if x==5:
        question = tk.Label(window,text='How to read 帷子ノ辻?',font='Times 40')
        right_option = tk.Button(window,text='Katabiranotsuji',command=right_answer,width=25,height=10)
        option1 = tk.Button(window,text='Katahiranotsuji',command=wrong_answer1,width=25,height=10)
        option2 = tk.Button(window,text='Katakonotsuji',command=wrong_answer2,width=25,height=10)
        question.grid(row=0,column=0,columnspan=3)
        right_option.grid(row=1,column=2)
        option1.grid(row=1,column=1)
        option2.grid(row=1,column=0)


Question(x)


window.mainloop()