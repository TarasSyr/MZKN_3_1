import numpy as np
import matplotlib.pyplot as plt

# Параметри
f_min = 1e9  # Мінімальна частота
f_max = 70e9  # Максимальна частота
step = 1e7  # Крок дискретизації
step_zero = 1e7  # Крок для пошуку нулів
t = 1e-9  # Час


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


# Оновлена функція для побудови графіка та пошуку нулів
def graphMaxMinZeroDrawShow(phi1, phi2=0):
    plt.figure(figsize=(18, 8))
    plt.xlabel("Частота (ГГц)")
    plt.ylabel("Інтенсивність")
    plt.title("Залежність інтенсивності сигналу I від частоти f")
    plt.grid(True)

    def forDrawing(phi):
        frequencies = np.arange(f_min, f_max, step)
        I = np.sin(2 * np.pi * frequencies * t + phi)

        # Функція для пошуку нулів
        I_for_zeroes = lambda f: np.sin(2 * np.pi * f * t + phi)

        # Пошук максимумів і мінімумів
        max_index = np.argmax(I)
        max_I = I[max_index]
        max_f = frequencies[max_index]
        min_index = np.argmin(I)
        min_I = I[min_index]
        min_f = frequencies[min_index]

        list_zero_function_new = []
        # Точне знаходження нулів методом бісекції
        for i in range(1, len(frequencies)):
            if np.sign(I[i - 1]) != np.sign(I[i]):  # Якщо зміна знаку
                zero_f = bisection_method(I_for_zeroes, frequencies[i - 1], frequencies[i])
                if zero_f is not None:
                    list_zero_function_new.append(zero_f)

        # Побудова графіка
        if phi == 0:
            text = "I(f)"
        elif phi == np.pi / 2:
            text = "I(f)+p/2"
        else:
            text = f"I(f)+{phi}"
        plt.plot(frequencies, I, label=text)
        plt.annotate(f'Max: {max_I:.2f}', xy=(max_f, max_I), xytext=(max_f + 1e9, max_I),
                     arrowprops=dict(facecolor='red', shrink=0.05))

        # Нанесення точок максимумів, мінімумів і нулів
        plt.plot(frequencies[max_index], max_I, "ro")
        plt.plot(frequencies[min_index], min_I, "ro")
        for zero_f in list_zero_function_new:
            plt.plot(zero_f, 0, "go")

        plt.annotate(f'Min: {min_I:.2f}', xy=(min_f, min_I), xytext=(min_f + 1e9, min_I - 0.1),
                     arrowprops=dict(facecolor='red', shrink=0.05))
        plt.grid(True)
        plt.legend()

    if phi2 == 0:
        forDrawing(phi1)
    elif phi2 != 0:
        forDrawing(phi1)
        forDrawing(phi2)
    plt.show()


# Виклик функції
graphMaxMinZeroDrawShow(0, np.pi / 2)
graphMaxMinZeroDrawShow(np.pi / 4)
graphMaxMinZeroDrawShow(np.pi / 8)