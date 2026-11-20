"""
Лабораторна робота №5: Варіант 5
Студент: Рубцов Михаїл
Група: EIP30
"""

from typing import Callable

def solve_iteration(f: Callable[[float], float], x_0: float, e: float, c: float, n: int):
    def phi(x: float) -> float:
        return x + c * f(x)
    iterations = []
    count = 0
    x = x_0
    root = None
    while abs(phi(x) - x) > e:
        if count + 1 >= n:
            root = "required accuracy is not reached, quantity of iterations is too large"
            break
        if abs(phi(phi(x)) - phi(x)) >= abs(phi(x) - x):
            root = "cannot be calculated, try to change x_0 or c"
            break
        x = phi(x)
        count += 1
        iterations.append(x)
    x = phi(x)
    count += 1
    iterations.append(x)
    if root is None:
        root = x
    return (root, count, iterations)

def save_results_to_file(results: tuple):
    (root, count, iterations) = results
    iteration_length = 0
    for x in iterations:
        if len(str(x)) > iteration_length:
            iteration_length = len(str(x))
    with open("results_variant_05.txt", "w", encoding = "utf-8") as file:
        file.write(f"Root: {root:.6f}\n") if type(root) == float else file.write(f"Root: {root}\n")
        file.write("Calculations:\n")
        count_length = len(str(count))
        file.write((count_length + iteration_length + 7) * '_' + '_\n')
        file.write('| № ' + count_length * ' ' + '| x' + iteration_length * ' ' + '|\n')
        file.write('|' + (count_length + 3) * '_' + '|' + (iteration_length + 2) * '_' + '|\n')
        for i in range(count):
            file.write(f'| {i + 1}' + (count_length - len(str(i + 1)) + 2) * ' ' + '| ' +
                        f'{iterations[i]}' + (iteration_length - len(str(iterations[i])) + 1) * ' ' + '|\n')
            file.write('|' + (count_length + 3) * '_' + '|' + (iteration_length + 2) * '_' + '|\n')

def main():
    def f(x: float) -> float:
        return x ** 4 - 13 * x ** 2 + 36 - 1 / x
    x_0 = 1
    e = 0.00006
    c = 0.05    # Додатковий параметр, який впливає на функцію phi(x)
    # Якщо c зробити менше по модулю, то корінь знайдеться ймовірніше, але буде більше ітерацій
    # Також зауважимо, що для нашого критерію зупинки має виконуватись phi'(x) < 0, а отже c треба підбирати таким,
    # щоб для довільного x з меж, у яких шукаємо корінь виконувалося с*f'(x) < -1, інакше корінь знайдеться з недостатньою точністю
    # Тобто для довільної f та довільного x_0 можна підібрати c аналітично
    n = int(input("Enter n: ")) # Максимальна кількість ітерацій
    results = solve_iteration(f, x_0, e, c, n)
    save_results_to_file(results)
    with open("results_variant_05.txt", "r", encoding = "utf-8") as file:
        for line in file:
            print(line, end="")

main()
