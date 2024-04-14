from tkinter import *
from tkinter import ttk
import tkinter as tk


#-------------------------------------------------------------------------------
# Мейн окно
root = Tk()
root.geometry('750x450')
root.title('pomogite')
root.configure(bg='#042440')


#-------------------------------------------------------------------------------
# Главная строчка кода
print('pomogite')


#-------------------------------------------------------------------------------
# Функция для второго окна
def second_win():


    second_window = tk.Toplevel(root)
    second_window.geometry('350x350+800+200')
    second_window.configure(bg='#031728')

    l1 = Label(second_window,text= 'What To-Do')
    l1.pack(pady=25)
    e1 = ttk.Entry(second_window)
    e1.pack()


    l2 = Label(second_window, text= 'Deadline')
    l2.pack(pady=25)
    e2 = ttk.Entry(second_window)
    e2.pack()

    def get_text():
        name_todo = e1.get()
        data_deadline = e2.get()

        todo_and_deadline = [name_todo,data_deadline]
        tree.insert("", "end", values=(todo_and_deadline))

    btn1 = Button(second_window,text= 'Добавить', command=get_text).pack(pady = 25)


#----------------------------------------------------------------------------
# Кнопка на мейн окне
btn = Button(text='Добавить',font=50,width=25,command=second_win).pack(pady=10)


#----------------------------------------------------------------------------
# Таблица с мейн инф
columns = ["To Do", "Deadline"]
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(pady=10)
# tree.insert("", "end", values=())


#----------------------------------------------------------------------------
# Жоски вывод
root.mainloop()