'''
3. Умови (if)
Задача:
Користувач вводить свій вік.
Якщо йому 18 або більше — виведи "Доступ дозволено",
інакше — "Доступ заборонено".
'''
age = int(input("How old are you?"))
if age >= 18:
    print("Access allowed")
else:
    print("Access denied")