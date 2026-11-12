"""
Лабораторна робота №5: Варіант 5
Студент: Рубцов Михаїл
Група: EIP30
"""

def f(x: float) -> float:
    return x ** 4 - 13 * x ** 2 + 36 - 1 / x

x_0 = 1
e = 0.00006
c = 0.05

def solve_iteration(func = f, zero_value = x_0, min_diff = e, coeff = c):
    def phi(x: float) -> float:
        return x + coeff * func(x)
    prev = zero_value
    x = phi(prev)
    count = 0
    while abs(x - prev) > min_diff:
        prev = x
        x = phi(prev)
        if abs(phi(x)-x) >= abs(x - prev):
            return "Result cannot be calculated, try to change x_0 or c"
        count += 1
        print(f"Iteration {count}: x =", x)
    return f"After {count} iterations we got x = {x}"
