"""
1. Обчисліть значення інтеграла функції за допомогою методу Монте-Карло, інакше кажучи, знайдіть площу під цим графіком
(сіра зона).

2. Перевірте правильність розрахунків, щоб підтвердити точність методу Монте-Карло, шляхом порівняння отриманого
результату та аналітичних розрахунків або результату виконання функції quad. Зробіть висновки.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Кількість випадкових точок для методу Монте-Карло
N = 10000000

# Метод Монте-Карло
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)
points_under_curve = np.sum(y_random <= f(x_random))
area_monte_carlo = (points_under_curve / N) * (b - a) * f(b)

# Аналітичний розрахунок
area_analytical = (b**3 / 3) - (a**3 / 3)

# Перевірка за допомогою функції quad
area_quad, error = quad(f, a, b)

# Виведення результатів
print(f"Площа під кривою (Монте-Карло): {area_monte_carlo}")
print(f"Площа під кривою (Аналітичний розрахунок): {area_analytical}")
print(f"Площа під кривою (quad): {area_quad}")

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()