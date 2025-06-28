import numpy as np
import matplotlib.pyplot as plt

# Оголошуємо константи
e = np.e
const = -e**3 + 3 * e**2 - 3  # це все, що не залежить від x

# Функція
def f(x):
    return np.exp(x) - 2 * x + const

# Похідні
def f_prime(x):
    return np.exp(x) - 2

def f_double_prime(x):
    return np.exp(x)


def g(x):
    return np.log(2 * x - const)

def simple_iteration(x0, eps):
    steps = [x0]
    while True:
        if 2 * x0 - const <= 0:  # захист від логарифма від від’ємного
            print("Некоректне значення для log, ітерація зупинена.")
            break
        x1 = g(x0)
        steps.append(x1)
        if abs(x1 - x0) < eps:
            break
        x0 = x1
    return x1, steps


# Метод половинного ділення
def bisection(a, b, eps):
    steps = []
    while abs(b - a) > eps:
        c = (a + b) / 2
        steps.append(c)
        if abs(f(c)) < eps:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, steps

# Метод хорд
def chord_method(a, b, eps):
    steps = []
    while abs(b - a) > eps:
        fa, fb = f(a), f(b)
        x = b - fb * (b - a) / (fb - fa)
        steps.append(x)
        if abs(f(x)) < eps:
            break
        if f(x) * f(a) < 0:
            b = x
        else:
            a = x
    return x, steps

# Метод Ньютона
def newton_method(x0, eps):
    steps = [x0]
    while True:
        x1 = x0 - f(x0)/f_prime(x0)
        steps.append(x1)
        if abs(x1 - x0) < eps:
            break
        x0 = x1
    return x1, steps

# Метод простої ітерації
def simple_iteration(x0, eps):
    steps = [x0]
    while True:
        x1 = g(x0)
        steps.append(x1)
        if abs(x1 - x0) < eps:
            break
        x0 = x1
    return x1, steps

# Графік
def plot_steps(steps, method_name):
    x_vals = np.linspace(0, 3, 400)
    y_vals = f(x_vals)
    plt.figure()
    plt.plot(x_vals, y_vals, label='f(x)')
    plt.axhline(0, color='black', linestyle='--')
    plt.plot(steps, [f(x) for x in steps], 'ro-', label='iterations')
    plt.title(f'Метод: {method_name}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Основна частина
a, b = 1, 2  # взято з розумного припущення графіка
eps = 1e-5

root_bis, steps_bis = bisection(a, b, eps)
root_chord, steps_chord = chord_method(a, b, eps)
root_newton, steps_newton = newton_method(b, eps)
root_iter, steps_iter = simple_iteration(1.5, eps)

print("Половинне ділення:", root_bis)
print("Хорд:", root_chord)
print("Ньютона:", root_newton)
print("Проста ітерація:", root_iter)

# Графіки
plot_steps(steps_bis, "Половинного ділення")
plot_steps(steps_chord, "Хорд")
plot_steps(steps_newton, "Ньютона")
plot_steps(steps_iter, "Простої ітерації")
