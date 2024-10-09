import numpy as np
import matplotlib.pyplot as plt

t = 1e-9  # час у секундах
phi = 0  # фаза
f_min = 10e9  # мінімальна частота 10 ГГц
f_max = 70e9 + 0.2e9  # максимальна частота 70 ГГц
step = 0.2e9  # крок 0.2 ГГц
step_zero = 1e5
p = np.pi
frequencies = np.arange(f_min, f_max, step)
I = np.sin(2 * np.pi * frequencies * t + phi)


# Запис у файл
with open("test.txt", "w", encoding='utf-8') as f:
    f.write("Залежність інтенсивності сигналу I від частоти f: \n")
    f.write("I:       ")
    for i in range(len(I)):
        if I[i] < 0:
            f.write(f"{I[i]:.9e} ")
        else:
            f.write(f"{I[i]:.10e} ")
    f.write("\n")
    f.write("Частоти: ")
    f.write(" ".join([f"{x:.10e}" for x in frequencies]) + "\n")

with open("test.txt", "r", encoding="utf-8") as output:
    contentOutput = output.read()
    print(f"Вміст файлу:\n{contentOutput}")


def graphMaxMinZeroDrawShow(phi1, phi2=0):
    plt.figure(figsize=(18, 8))
    plt.xlabel("Частота (ГГц)")
    plt.ylabel("Інтенсивність")
    plt.title("Залежність інтенсивності сигналу I від частоти f")
    plt.grid(True)
    def forDrawing(phi):
        frequencies = np.arange(f_min, f_max, step)
        I = np.sin(2 * np.pi * frequencies * t + phi)
        max_index = np.argmax(I)
        max_I = I[max_index]
        max_f = frequencies[max_index]
        min_index = np.argmin(I)
        min_I = I[min_index]
        min_f = frequencies[min_index]
        list_min_x = []
        list_max_x = []
    # Нуль функції-значення аргумента(х), при якому значення функції(у) дорівнює нулю
        list_zero_function = []  # список з нулями функції, котрий і є списком іксів, при яких графік перетинає вісь ОХ(абсцис)
        frequencies_for_zeroes = np.arange(f_min, f_max, step_zero)
        I_for_zeroes = np.sin(2 * np.pi * frequencies_for_zeroes * t + phi)
        I_for_zeroes_r = np.round(I_for_zeroes, 5)
        I_rounded = np.round(I, 10)

        for i in range(len(I)):
            if max(I_rounded) == I_rounded[i]:
                list_max_x.append(frequencies[i])
            elif min(I_rounded) == I_rounded[i]:
                list_min_x.append(frequencies[i])

        for i in range(int((f_max - f_min) / step_zero)):
            if I_for_zeroes_r[i] == 0:
                list_zero_function.append(frequencies_for_zeroes[i])
        print(list_max_x, "\n", list_min_x, "\n", list_zero_function)

        # Графік
        if phi==0:
            text="I(f)"
        elif phi==p/2:
            text="I(f)+p/2"
        elif phi==p/4:
            text = "I(f)+p/4"
        elif phi==p/8:
            text = "I(f)+p/8"
        else:
            text = f"I(f)+{phi}"
        plt.plot(frequencies, I, label=text)
        plt.annotate(f'Max: {max_I:.2f}', xy=(max_f, max_I), xytext=(max_f + 1e9, max_I),
                     arrowprops=dict(facecolor='red', shrink=0.05))
        for i in range(len(list_max_x)):
            plt.plot(list_max_x[i], max_I, "ro")
        for i in range(len(list_min_x)):
            plt.plot(list_min_x[i], min_I, "ro")
        for i in range(len(list_zero_function)):
            plt.plot(list_zero_function[i], 0, "go")
        plt.annotate(f'Min: {min_I:.2f}', xy=(min_f, min_I), xytext=(min_f + 1e9, min_I - 0.1),
                     arrowprops=dict(facecolor='red', shrink=0.05))

        plt.grid(True)
        plt.legend()

    if phi2==0:
        forDrawing(phi1)
    elif phi2!=0:
        forDrawing(phi1)
        forDrawing(phi2)
    plt.show()

def circleDiagram(phi):
    frequencies = np.arange(f_min, f_max, step)
    I = np.sin(2 * np.pi * frequencies * t + phi)
    frequencies_for_zeroes = np.arange(f_min, f_max, step_zero)
    I_for_zeroes = np.sin(2 * np.pi * frequencies_for_zeroes * t + phi)
    I_for_zeroes_r = np.round(I_for_zeroes, 5)
    I_rounded = np.round(I, 10)
    posFirstList=[]
    posSecondList=[]
    posThirdList=[]
    negFirstList=[]
    negSecondList=[]
    negThirdList=[]
    posFirstRange=[]
    for i in range(len(frequencies_for_zeroes)):
        freq=frequencies_for_zeroes[i]
        if I_for_zeroes[i]>0 and f_min<freq<30e9:
            posFirstList.append(I_for_zeroes[i])
        elif I_for_zeroes[i]>0 and 31e9<freq<50e9:
            posSecondList.append(I_for_zeroes[i])
        elif I_for_zeroes[i]>0 and 51e9<freq<=70e9:
            posThirdList.append(I_for_zeroes[i])
        elif I_for_zeroes[i]<0 and f_min<freq<30e9:
            negFirstList.append(I_for_zeroes[i])
        elif I_for_zeroes[i] < 0 and 31e9 < freq< 50e9:
            negSecondList.append(I_for_zeroes[i])
        elif I_for_zeroes[i] < 0 and 51e9 < freq <= 70e9:
            negThirdList.append(I_for_zeroes[i])

    labels="+, 10-30", "+, 31-50", "+, 51-70", "-, 10-30", "-, 31-50", "-, 51-70"
    posnegcount=[(len(posFirstList)),(len(posSecondList)),(len(posThirdList)),(len(negFirstList)), (len(negSecondList)), (len(negThirdList))]
    fig, ax = plt.subplots()
    ax.pie(posnegcount, labels=labels, autopct='%1.4f%%')
    plt.axis('equal')
    plt.show()

circleDiagram(p/2)
#graphMaxMinZeroDrawShow(0, p / 2 )
#graphMaxMinZeroDrawShow(p / 4)
#graphMaxMinZeroDrawShow(p / 8)