from tkinter.messagebox import showinfo

import numpy as np
from numpy.fft import rfft, rfftfreq
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox

import numpy as np
from numpy.fft import rfft, rfftfreq, fft, fftfreq, irfft
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox

SAMPLE_RATE = 200
F_FROM = 8

window = Tk()
window.geometry('650x350')
menu = Menu()
window.config(menu=menu)


def remove_f(a):
    N = len(a)
    TIME = N // SAMPLE_RATE
    from_i = F_FROM * TIME * 2
    new_a = a.copy()
    for i in range(from_i, N):
        new_a[i] = 0 + 0j
        print(a[i])
    return new_a


def show_graph(y):
    if y is None:
        plt.text(0.1, 1.1, 'Ошибка чтения файла')
        plt.show()
    elif len(y) == 0:
        plt.text(0.1, 1.1, 'Ошибка чтения файла')
        plt.show()
    else:
        N = len(y)
        x = np.linspace(0, len(y) / SAMPLE_RATE, N, endpoint=False)
        plt.plot(sorted(x), y)
        plt.show()


def show_all(y):
    yf = rfft(y)
    N = len(yf)
    xf = rfftfreq(len(y), 1 / SAMPLE_RATE)

    new_yf = remove_f(yf)
    new_y = irfft(new_yf)
    x = np.linspace(0, len(new_y) / SAMPLE_RATE, len(new_y), endpoint=False)

    plt.subplot(2, 2, 1)
    x = np.linspace(0, len(y) / SAMPLE_RATE, len(y), endpoint=False)
    plt.plot(sorted(x), y)

    plt.subplot(2, 2, 2)
    plt.plot(sorted(xf), np.abs(yf))

    plt.subplot(2, 2, 3)

    x = np.linspace(0, len(new_y) / SAMPLE_RATE, len(new_y), endpoint=False)
    plt.plot(sorted(x), new_y, 'g')

    plt.subplot(2, 2, 4)
    new_yf = remove_f(yf)
    xf = rfftfreq(len(y), 1 / SAMPLE_RATE)
    # new_yf = yf[N//2:]
    plt.plot(sorted(xf), np.abs(new_yf), 'g')

    plt.show()


def show_fourie_spectr(y):
    if y is None:
        plt.text(0.1, 1.1, 'Ошибка чтения файла')
        plt.show()
    elif len(y) == 0:
        plt.text(0.1, 1.1, 'Ошибка чтения файла')
        plt.show()
    else:
        yf = rfft(y)
        N = len(yf)
        xf = rfftfreq(len(y), 1 / SAMPLE_RATE)
        # new_yf = yf[N//2:]
        plt.plot(sorted(xf), np.log(np.abs(yf)))
        plt.show()


def show_fourie_spectr_after_filtration(y):
    if y is None:
        plt.text(0.1, 1.1, 'Ошибка чтения файла')
        plt.show()
    elif len(y) == 0:
        plt.text(0.1, 1.1, 'Ошибка чтения файла')
        plt.show()
    else:
        yf = rfft(y)
        new_yf = remove_f(yf)
        xf = rfftfreq(len(y), 1 / SAMPLE_RATE)
        # new_yf = yf[N//2:]
        plt.plot(sorted(xf), np.abs(new_yf))
        plt.show()


def show_graph_after_fourier_filtration(y):
    if y is None:
        plt.text(0.1, 1.1, 'Ошибка чтения файла')
        plt.show()
    elif len(y) == 0:
        plt.text(0.1, 1.1, 'Ошибка чтения файла')
        plt.show()
    else:
        yf = rfft(y)
        new_yf = remove_f(yf)
        new_y = irfft(new_yf)
        x = np.linspace(0, len(new_y) / SAMPLE_RATE, len(new_y), endpoint=False)
        plt.plot(sorted(x), new_y)
        # xf = fftfreq(N, 1 / SAMPLE_RATE)
        # plt.plot(sorted(xf), np.log(np.abs(yf)))
        plt.show()


def compare(y):
    yf = rfft(y)
    x = np.linspace(0, len(y) / SAMPLE_RATE, len(y), endpoint=False)
    plt.plot(sorted(x), y, 'r')

    new_yf = remove_f(yf)
    new_y = irfft(new_yf)
    x = np.linspace(0, len(new_y) / SAMPLE_RATE, len(new_y), endpoint=False)

    plt.plot(sorted(x), new_y, 'g')
    plt.show()


def read_from_file(path, column):
    if path is None:
        path = "/home/apple/python/chmo_ebanoe/Manuk.asc"
    f = open(path, 'r')
    y = []
    line = f.readline()
    while line != '':
        if line.startswith(';'):
            line = f.readline()
            continue
        else:
            y.append(int(line.split()[column]))
        line = f.readline()
    f.close()
    return y

def update():

    returned_values['col'] = int(e1.get())
    print(returned_values['col'])
    returned_values['array'] = read_from_file(returned_values['filename'], returned_values['col'])


def select_file(column):
    col = int(e1.get())
    filetypes = (
        ('text files', '*.asc'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    returned_values['filename'] = filename
    returned_values['array'] = read_from_file(filename, col)


if __name__ == '__main__':
    returned_values = {}
    returned_values['col'] = 0
    returned_values['filename'] = "/home/apple/python/chmo_ebanoe/Manuk.asc"
    returned_values['array'] = read_from_file("/home/apple/python/chmo_ebanoe/Manuk.asc", returned_values['col'])
    open_button = Button(
        window,
        text='Загрузить файл',
        command=lambda: select_file(0)
    )
    open_button.pack()
    btn1 = Button(window, text="Показать график",
                  command=lambda: show_graph(returned_values['array']))
    btn1.pack()
    e1 = Entry(window)
    e1.insert(0, "0")
    e1.pack()

    btn9 = Button(window, text="Применить",
                  command=lambda: update())
    btn9.pack()
    btn2 = Button(window, text="Показать Фурье спектр графика",
                  command=lambda: show_fourie_spectr(returned_values['array']))
    btn2.pack()
    btn5 = Button(window, text="Показать график после преобразования ",
                  command=lambda: show_graph_after_fourier_filtration(returned_values['array']))
    btn5.pack()
    btn6 = Button(window, text="Показать спектр Фурье после преобразования",
                  command=lambda: show_fourie_spectr_after_filtration(returned_values['array']))
    btn6.pack()

    btn7 = Button(window, text="Показать все графики",
                  command=lambda: show_all(returned_values['array']))
    btn7.pack()

    btn8 = Button(window, text="Сравнить графики",
                  command=lambda: compare(returned_values['array']))
    btn8.pack()

    window.mainloop()
