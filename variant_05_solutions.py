"""
Лабораторна робота №5: Варіант 5
Студент: Рубцов Михаїл
Група: EIP30
"""

def solve_iteration(f: function, x_0: float, e: float, c: float):
    def phi(x: float) -> float:
        return x + c * f(x)
    prev = x_0
    x = phi(prev)
    iterations = []
    count = 0
    while abs(x - prev) > e:
        prev = x
        x = phi(prev)
        if abs(phi(x) - x) >= abs(x - prev):
            return ("cannot be calculated, try to change x_0 or c", count, iterations)
        count += 1
        iterations.append(f"Iteration {count}: x = {x}")
    return (x, count, iterations)

def save_results_to_file(results: tuple):
    (root, count, iterations) = results
    with open("results_variant_05.txt", "w", encoding = "utf-8") as file:
        file.write(f"Root: {root:.6f}\n") if type(root) == float else file.write(f"Root: {root}\n")
        file.write("Calculations:\n")
        for i in range(count):
            file.write(f"{iterations[i]}\n")

def main():
    def f(x: float) -> float:
        return x ** 4 - 13 * x ** 2 + 36 - 1 / x
    x_0 = 1
    e = 0.00006
    c = 0.05    #Додатковий параметр, який впливає на функцію phi(x)
    # Якщо c зробити менше по модулю, то корінь знайдеться ймовірніше, але буде більше ітерацій
    results = solve_iteration(f, x_0, e, c)
    save_results_to_file(results)

main()
