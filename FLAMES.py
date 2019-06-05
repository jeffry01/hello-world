

    
def task1():
    
    page_3.tkraise()
    task2()
def task2():

    global entry1,entry2
    s1=(entry_1.get()).strip()
    s2=(entry_2.get()).strip()
    o=list(s1)
    p=list(s2)


    # logic for removing similar characters

    
    for i in range(0,len(o)):
        for j in range(0,len(p)):
            try:
                if o[i]==p[j]:
                    o.remove(o[i])
                    p.remove(p[j])
                    break
            except IndexError:
                pass
    list1= o+p
    x=len(list1)

    
    #loop for FLAMES
    
    word='FLAMES'
    y=list(word)
    z=6
    while(z!=1):
        rem=x%z
        if rem==0:
            y.remove(y[len(y)-1])
        else:
            y.remove(y[rem-1])
            
        z=z-1

    #switch condition using dictionary in python
    d=''.join(y)
    dict={'F':'Friends','L':'Love','A':'Affection','M':'Marriage','E':'Enemy','S':'Supportive'}
    Ans=dict[d]

    #page 3

    
    label_4=Label(page_3,text=Ans)
    label_4.pack(side=TOP)

from tkinter import *
window=Tk()

window.geometry('275x450')
page_1=Frame(window)
page_2=Frame(window)
page_3=Frame(window)

for frame in (page_1,page_2,page_3):
      frame.grid(row=0,column=0,sticky='news')

      
#page 1

      
label_1=Label(page_1,text='WELCOME TO \nFLAMES')
label_1.pack()
photo=PhotoImage(file='a.png')
label_5=Label(page_1,image=photo)
label_5.pack(side=TOP)
button_1=Button(page_1,text='click here to start',command=lambda:page_2.tkraise())

text=Label(page_1,text="What is FlamesGame?\nFlamesGame is a relationship calculating algorithm \nfamous between the youngsters.\n At the time of graduation everyone might heard\n about this and many of them tried\n out this secretly. Some took this as\n very serious also. So what FLAMES stance for? \nF - Friendship\n L - Love \nA - Affection\n M - Marriage\n E - Enemy\n S - Sister (Sibling) ")
text.pack()
button_1.pack()

#page 2


label_2=Label(page_2,text='Enter your Name')
label_3=Label(page_2,text="Enter your partner's name")
button_2=Button(page_2,text='Try your luck!',command=task1)
entry_1=Entry(page_2)
entry_2=Entry(page_2)
label_2.grid(row=0,column=0)
label_3.grid(row=1,column=0)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)
button_2.grid(columnspan=2)

page_1.tkraise()


window.mainloop()

