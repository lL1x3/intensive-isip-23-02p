from tkinter import *
from tkinter import ttk
import tkinter as tk



#-----------------------------------------------------------------------------------------------------------------------
# Мейн окно
root = Tk()
root.geometry('750x475+575+250')
root.title('pomogite')
root.configure(bg='#e8dccc')
root.resizable(width=False,height=False)


# Главная строчка кода
print('pomogite')


#-----------------------------------------------------------------------------------------------------------------------
# Функция для второго окна
def second_win():

    second_window = tk.Toplevel(root)
    second_window.geometry('350x350+800+200')
    second_window.configure(bg='#373234')

    l1 = Label(second_window,font = 'inter 15 bold',text= 'Продукт',background='#f3ece4')
    l1.pack(pady=25)
    e1 = ttk.Entry(second_window)
    e1.pack()


    l2 = Label(second_window,font = 'inter 15 bold', text= 'Калории',background='#f3ece4')
    l2.pack(pady=25)
    e2 = ttk.Entry(second_window)
    e2.pack()


    def get_text():
        name_todo = e1.get()
        data_deadline = e2.get()

        todo_and_deadline = [name_todo,data_deadline]
        tree.insert("", "end", values=(todo_and_deadline))

    btn1 = Button(second_window,text= 'Добавить',font = 'inter 15 bold', command=get_text,background='#f3ece4').pack(pady = 25)

#-----------------------------------------------------------------------------------------------------------------------
# Функция для третьего окна
def third_win():

    third_window = tk.Toplevel(root)
    third_window.geometry('350x450+800+200')
    third_window.configure(bg='#373234')

    lweight = Label(third_window,font = 'inter 15 bold',text= 'Ваш вес',background='#f3ece4')
    lweight.pack(pady=25)

    eweight = ttk.Entry(third_window)
    eweight.pack()


    lheight = Label(third_window,font = 'inter 15 bold', text= 'Ваш рост',background='#f3ece4')
    lheight.pack(pady=25)

    eheight = ttk.Entry(third_window)
    eheight.pack()

    lage = Label(third_window, font='inter 15 bold', text='Ваш возраст',background='#f3ece4')
    lage.pack(pady=25)

    eage = ttk.Entry(third_window)
    eage.pack()
#-----------------------------------------------------------------------------------------------------------------------
# Функция для расчета калорий


    def set_call():
        weight = int(eweight.get())
        height = int(eheight.get())
        age = int(eage.get())

        call1 = weight * 10
        call2 = 7 * height
        call3 = 5 * age

        total_call = call1 + call2 + call3
        lcall2.config(text=total_call)

    btn1 = Button(third_window,text= 'Ввод',font = 'inter 15 bold',command=set_call).pack(pady = 25)


#-----------------------------------------------------------------------------------------------------------------------
# Виджеты мейн окна

lcall1 = Label(text = 'Ваша норма калорий',width=33,font='inter 15 bold',background='#f3ece4')
lcall2 = Label(text = '-',width=33,font='inter 15 bold',background='#f3ece4')


lcall1.pack(pady=5)
lcall2.pack(pady=5)

btn_third_window = Button(text='Ввод данных',font = 'inter 15 bold',width=33,command=third_win,background='#f3ece4').pack(pady=10)


#-----------------------------------------------------------------------------------------------------------------------
# Таблица с продуктами
columns = ["Продукт", "Калории"]
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(pady=10)
# tree.insert("", "end", values=())


#-----------------------------------------------------------------------------------------------------------------------
# Кнопка добавления продукта
btn_second_window = Button(text='Добавить',font = 'inter 15 bold',width=33,command=second_win,background='#f3ece4').pack(pady=10)


#-----------------------------------------------------------------------------------------------------------------------
# Смена темы

def change_theme():
    current_bg = root.cget("bg")
    new_bg = "#e8dccc" if current_bg == "#373234" else "#373234"
    root.configure(bg=new_bg)


change_theme_button = Button(root, text="☀", command=change_theme)
change_theme_button.pack(anchor = SE, expand=1)

#-----------------------------------------------------------------------------------------------------------------------
# Жоски вывод
root.mainloop()