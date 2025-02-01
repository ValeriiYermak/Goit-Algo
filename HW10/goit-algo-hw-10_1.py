"""
Завдання 1. Оптимізація виробництва

Компанія виробляє два види напоїв: "Лимонад" і "Фруктовий сік". Для виробництва цих напоїв використовуються різні
інгредієнти та обмежена кількість обладнання. Задача полягає у максимізації виробництва, враховуючи обмежені ресурси.

Умови завдання:
1. "Лимонад" виготовляється з "Води", "Цукру" та "Лимонного соку".
2. "Фруктовий сік" виготовляється з "Фруктового пюре" та "Води".
3. Обмеження ресурсів: 100 од. "Води", 50 од. "Цукру", 30 од. "Лимонного соку" та 40 од. "Фруктового пюре".
4. Виробництво одиниці "Лимонаду" вимагає 2 од. "Води", 1 од. "Цукру" та 1 од. "Лимонного соку".
5. Виробництво одиниці "Фруктового соку" вимагає 2 од. "Фруктового пюре" та 1 од. "Води".

Використовуючи PuLP, створіть модель, яка визначає, скільки "Лимонаду" та "Фруктового соку" потрібно виробити для
максимізації загальної кількості продуктів, дотримуючись обмежень на ресурси. Напишіть програму, код якої максимізує
загальну кількість вироблених продуктів "Лимонад" та "Фруктовий сік", враховуючи обмеження на кількість ресурсів.
"""

import pulp

# initialization of model
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Definition of variables
Lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")  # the quantity of Lemonade
fruit_juice = pulp.LpVariable("fruit_juice", lowBound=0, cat="Integer")  # the quantity of fruit_juice

# x <=100 # water
# y<= 50 #suger
# z <=30 #Lemon juice
# f <=40 #Fruit puree

model += Lemonade + fruit_juice, "Total_Production"

# Adding restrictions
model += 2 * Lemonade + 1 * fruit_juice <= 100  # Restriction of water
model += 1 * Lemonade <= 50                     # Restriction of sugar
model += 1 * Lemonade <= 30                     # Restriction of lemon juice
model += 2 * fruit_juice <= 40                  # Restriction of Fruit puree

# Solution of the model
model.solve()

# Display of results
print("Solving Status:", pulp.LpStatus[model.status])
print("The quantity lemonade for production:", Lemonade.varValue)
print("The quantity fruit_juice for production:", fruit_juice.varValue)
print("Total quantity of products:", int(pulp.value(model.objective)))
