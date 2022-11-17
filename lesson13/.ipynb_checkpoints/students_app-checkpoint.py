from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd

students_info = pd.read_excel("students_data.xlsx", index_col = 0)

def read_info():
    '''
        Чтение инормации при нажжатии кнопки
        "Прочитать"
    '''
    name = name_entr.get()
    group = group_entr.get()
    marks = [
        int(mark) 
        for mark in marks_entr.get().split(",")
    ]
    
    stud_info = pd.Series(
        [group] + marks,
        index = students_info.columns
    )
    
    students_info.loc[name,:] = stud_info
    
def plot_info():
    '''
        Представление об успеваемости студенотов в виде графка
    '''
    plt.boxplot(
        students_info.loc[:, "Оценка 1":].T,
        labels = students_info.index
    )
    
    plt.show()
    
    
# формирование окончки
root = Tk()

name_frame = Frame(); name_frame.pack()
Label(name_frame, text = "Имя").pack(side = LEFT)
name_entr = Entry(name_frame); name_entr.pack(side = LEFT)

group_frame = Frame(); group_frame.pack()
Label(group_frame, text = "Группа").pack(side = LEFT)
group_entr = Entry(group_frame); group_entr.pack(side = LEFT)


marks_frame = Frame(); marks_frame.pack()
Label(
    marks_frame, 
    text = "Оценки через запятую (5 шт)"
).pack(side = LEFT)
marks_entr = Entry(marks_frame); marks_entr.pack(side = LEFT)


Button(
    text = "Считать ученика",
    command = read_info
).pack()
Button(
    text = "Статистика по ученикам",
    command = plot_info
).pack()

root.mainloop()

students_info.to_excel("students_data.xlsx")