import numpy as np
import matplotlib.pyplot as plt

t = 1e-9  # час у секундах
phi = 0  # фаза
f_min = 10e9  # мінімальна частота 10 ГГц
f_max = 70e9 + 0.2e9  # максимальна частота 70 ГГц
step = 1e7  # крок 0.2 ГГц
step_zero = 1e7
p = np.pi
frequencies = np.arange(f_min, f_max, step)
I = np.sin(2 * np.pi * frequencies * t + phi)

# Функція для знаходження нуля методом бісекції
def bisection_method(f, a, b, tol=1e-5):
    """Знаходження нуля функції f між a і b за допомогою методу бісекції"""
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        return None  # Якщо функція не змінює знак на інтервалі, немає нуля
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        fc = f(c)
        if fc == 0:
            return c
        elif fa * fc < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

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

def bisection_method(f, a, b, tol=1e-5):
    """Знаходження нуля функції f між a і b за допомогою методу бісекції"""
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        return None  # Якщо функція не змінює знак на інтервалі, немає нуля
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        fc = f(c)
        if fc == 0:
            return c
        elif fa * fc < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

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
        I_for_zeroes_bisect = lambda f: np.sin(2 * np.pi * f * t + phi)
        step_for_zero=1e4
        frequencies_for_zeroes_new=[]
        list_zero_function_new=[]


        #точніше вираховування нулів, перший метод
        for i in range(len(I_for_zeroes)):
            if np.sign(I_for_zeroes[i-1])>0 and np.sign(I_for_zeroes[i])<0 or np.sign(I_for_zeroes[i-1])<0 and np.sign(I_for_zeroes[i])>0:
                frequencies_for_zeroes_min=frequencies_for_zeroes[i-1]
                frequencies_for_zeroes_max=frequencies_for_zeroes[i]
                frequencies_for_zeroes_new=np.arange(frequencies_for_zeroes_min,frequencies_for_zeroes_max,step_for_zero)
                I_for_zeroes_new = np.sin(2 * np.pi * frequencies_for_zeroes_new * t + phi)
                for i in range(len(I_for_zeroes_new)):
                    if np.round(I_for_zeroes_new[i], 10)==0:
                       list_zero_function_new.append(frequencies_for_zeroes_new[i])

        #точніше вираховування нулів, другий метод(дуже точний)
        """for i in range(len(I_for_zeroes)):
            if np.sign(I_for_zeroes[i-1])>0 and np.sign(I_for_zeroes[i])<0 or np.sign(I_for_zeroes[i-1])<0 and np.sign(I_for_zeroes[i])>0:
                frequencies_for_zeroes_before_sign_change=frequencies_for_zeroes[i-1]      #(x1) - ікс перед зміною знака функції
                frequencies_for_zeroes_after_sign_change=frequencies_for_zeroes[i]        #(x2) - ікс після зміни знака функції

                I_before_sign_change = I_for_zeroes[i - 1]     #значення функції до зміни знаку(y1)
                I_after_sign_change = I_for_zeroes[i]         #значення функції після зміни знаку(y1)


                # Лінійна інтерполяція
                zero_frequency = (frequencies_for_zeroes_before_sign_change - I_before_sign_change *
                                  (frequencies_for_zeroes_after_sign_change - frequencies_for_zeroes_before_sign_change) / (I_after_sign_change - I_before_sign_change))

                list_zero_function_new.append(zero_frequency)"""

        #третій метод: комбінований
        """for i in range(len(I_for_zeroes)):
            if np.sign(I_for_zeroes[i-1])>0 and np.sign(I_for_zeroes[i])<0 or np.sign(I_for_zeroes[i-1])<0 and np.sign(I_for_zeroes[i])>0:
                frequencies_for_zeroes_before_sign_change=frequencies_for_zeroes[i-1]      #(x1) - ікс перед зміною знака функції
                frequencies_for_zeroes_after_sign_change=frequencies_for_zeroes[i]        #(x2) - ікс після зміни знака функції

                I_before_sign_change = I_for_zeroes[i - 1]     #значення функції до зміни знаку(y1)
                I_after_sign_change = I_for_zeroes[i]         #значення функції після зміни знаку(y1)

                frequencies_for_zeroes_new = np.arange(frequencies_for_zeroes_before_sign_change, frequencies_for_zeroes_after_sign_change, step_for_zero)
                for i in range(len(frequencies_for_zeroes_new)):
                    I_new=(np.sin(2 * np.pi * frequencies_for_zeroes_new[i] * t + phi))
                    if np.sign(I_new) == 0 or np.sign(I_new) != np.sign(I_before_sign_change):  #умова зміни знаку
                        zero_frequency = (frequencies_for_zeroes_before_sign_change - I_before_sign_change *
                                          (frequencies_for_zeroes_new[i] - frequencies_for_zeroes_before_sign_change) / (I_new - I_before_sign_change))
                        list_zero_function_new.append(zero_frequency)
                        break"""

        """frequencies_for_zeroes = np.arange(f_min + phi, f_max + phi, step_zero)
        I_for_zeroes = np.sin(2 * np.pi * frequencies_for_zeroes * t + phi)

        step_for_zero = 1e-3  # Менший крок для більшої точності

        for i in range(1, len(I_for_zeroes)):
            # Перевіряємо зміну знака
            if (I_for_zeroes[i - 1] * I_for_zeroes[i]) < 0:
                frequencies_for_zeroes_before_sign_change = frequencies_for_zeroes[i - 1]
                frequencies_for_zeroes_after_sign_change = frequencies_for_zeroes[i]

                I_before_sign_change = I_for_zeroes[i - 1]
                I_after_sign_change = I_for_zeroes[i]

                # Визначаємо точний нуль через лінійну інтерполяцію
                zero_frequency = (frequencies_for_zeroes_before_sign_change - I_before_sign_change * 
                                  (frequencies_for_zeroes_after_sign_change - frequencies_for_zeroes_before_sign_change) /
                                  (I_after_sign_change - I_before_sign_change))

                list_zero_function_new.append(zero_frequency)"""

        #метод середини відрізків
        """for i in range(len(I_for_zeroes)):
            if np.sign(I_for_zeroes[i-1])>0 and np.sign(I_for_zeroes[i])<0 or np.sign(I_for_zeroes[i-1])<0 and np.sign(I_for_zeroes[i])>0:
                frequencies_for_zeroes_min=frequencies_for_zeroes[i-1]
                frequencies_for_zeroes_max=frequencies_for_zeroes[i]
                x1=frequencies_for_zeroes_min   # xc = (x1 + x2)/2, yc =(y1 + y1)/2 ;
                x2=frequencies_for_zeroes_max
                xc=(x1 + x2)/2
                list_zero_function_new.append(xc)"""

        #комбінований 2
        """for i in range(len(I_for_zeroes)):
            if np.sign(I_for_zeroes[i-1])>0 and np.sign(I_for_zeroes[i])<0 or np.sign(I_for_zeroes[i-1])<0 and np.sign(I_for_zeroes[i])>0:
                frequencies_for_zeroes_min=frequencies_for_zeroes[i-1]
                frequencies_for_zeroes_max=frequencies_for_zeroes[i]
                frequencies_for_zeroes_new=np.arange(frequencies_for_zeroes_min, frequencies_for_zeroes_max, step_for_zero)
                I_for_zeroes_new=np.sin(2 * np.pi * frequencies_for_zeroes_new * t + phi)
                for i in range(len(I_for_zeroes_new)):
                    if np.sign(I_for_zeroes_new[i - 1]) > 0 and np.sign(I_for_zeroes_new[i]) < 0 or np.sign(
                        I_for_zeroes_new[i - 1]) < 0 and np.sign(I_for_zeroes_new[i]) > 0:
                        x1=frequencies_for_zeroes_new[i-1]
                        x2=frequencies_for_zeroes_new[i]
                        xc=(x1 + x2)/2       # xc = (x1 + x2)/2, yc =(y1 + y1)/2 ;
                        list_zero_function_new.append(xc)"""

        #дуже точний(напевно найточніший)
        """for i in range(1, len(frequencies)):
            if np.sign(I[i - 1]) != np.sign(I[i]):  # Якщо зміна знаку
                zero_f = bisection_method(I_for_zeroes_bisect, frequencies[i - 1], frequencies[i])
                if zero_f is not None:
                    list_zero_function_new.append(zero_f)"""

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
        for i in range(len(list_zero_function_new)):
            plt.plot(list_zero_function_new[i], 0, "go")
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

"""def circleDiagram(phi):
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
    plt.show()"""

def circleDiagram(phi):
    frequencies = np.arange(f_min, f_max, step)
    I = np.sin(2 * np.pi * frequencies * t + phi)
    posFirstList = []
    posSecondList = []
    posThirdList = []
    negFirstList = []
    negSecondList = []
    negThirdList = []
    posFirstRange = []

    for i in range(len(frequencies)):
        freq = frequencies[i]
        if I[i] > 0 and f_min < freq < 30e9:
            posFirstList.append(I[i])
        elif I[i] > 0 and 31e9 < freq < 50e9:
            posSecondList.append(I[i])
        elif I[i] > 0 and 51e9 < freq <= 70e9:
            posThirdList.append(I[i])
        elif I[i] < 0 and f_min < freq < 30e9:
            negFirstList.append(I[i])
        elif I[i] < 0 and 31e9 < freq < 50e9:
            negSecondList.append(I[i])
        elif I[i] < 0 and 51e9 < freq <= 70e9:
            negThirdList.append(I[i])

    posnegcount = [(len(posFirstList)), (len(negFirstList))]
    fig, ax = plt.subplots()
    labels="Positive, 0-30GHz,", "Negative, 0-30GHz"
    #ax.pie(posnegcount, labels=labels, autopct='%1.4f%%')
    labels_with_values = [f'{label}: {count}' for label, count in zip(labels, posnegcount)]
    ax.pie(posnegcount, labels=labels_with_values, autopct='%1.4f%%')
    plt.axis('equal')
    plt.show()

    posnegcount = [(len(posSecondList)), (len(negSecondList))]
    fig, ax = plt.subplots()
    labels = "Positive, 31-50GHz,", "Negative, 31-50GHz"
    labels_with_values = [f'{label}: {count}' for label, count in zip(labels, posnegcount)]
    ax.pie(posnegcount, labels=labels_with_values, autopct='%1.4f%%')
    plt.axis('equal')
    plt.show()

    posnegcount = [(len(posThirdList)), (len(negThirdList))]
    fig, ax = plt.subplots()
    labels = "Positive, 51-70GHz,", "Negative, 51-70GHz"
    labels_with_values = [f'{label}: {count}' for label, count in zip(labels, posnegcount)]
    ax.pie(posnegcount, labels=labels_with_values, autopct='%1.4f%%')
    plt.axis('equal')
    plt.show()

circleDiagram(p/2)
graphMaxMinZeroDrawShow(0, np.pi / 2 )
graphMaxMinZeroDrawShow(p / 4)
graphMaxMinZeroDrawShow(p / 8)