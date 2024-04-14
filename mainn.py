from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


root = Tk()
root.title('Water Balance~')
root.geometry("720x350+570+150")

#-----------------------------------------------------------------------------------------------------------------------
# Функции

count = 0

def get_number():
    global count
    count += 1
    number = norma2 / 250
    masmd = 100 / number
    progressbara.step(masmd)
    if count > number:
        progressbara.pack_forget()
        showinfo(title="Water balance", message="Вы выпили дневную норму!")
    else:
        pass







def get_norma():
    global norma2
    norma1 = int(e_question.get())
    norma2 = norma1 * 30
    l_water2.config(text=norma2)





#-----------------------------------------------------------------------------------------------------------------------
# Вкладки

tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Water balance')
tab_control.add(tab2, text='Ваши данные')

tab_control.pack(expand = 1, fill='both')


#-----------------------------------------------------------------------------------------------------------------------
#Виджеты вторая вкладка

label_question1 = Label(tab2,text='Введите ваш вес')
label_question1.pack(pady=10)

e_question = Entry(tab2)
e_question.pack(pady=10)

btn_question = Button(tab2, text='~', command=get_norma)
btn_question.pack(pady=10)

label_question3 = Label(tab2,text='Норма воды в сутки вычисляется по формуле')
label_question4 = Label(tab2,text='На 1 кг веса * 30 мл воды')

label_question3.pack(pady=10)
label_question4.pack(pady=10)



#-----------------------------------------------------------------------------------------------------------------------
# Виджеты первая вкладка

l_water1 = Label(tab1,text='Ваша норма воды')
l_water1.pack()
l_water2 = Label(tab1,text='-')
l_water2.pack(pady=10)


value_var = IntVar(value=0)

progressbara = ttk.Progressbar(tab1, orient="horizontal", length=650, variable=value_var,mode='determinate')
progressbara.pack(pady=10)


btn = Button(tab1,text = 'UwU',command=get_number)
btn.pack(pady=10)


#-----------------------------------------------------------------------------------------------------------------------
# Вывод
root.mainloop()