"""
Лабораторна робота №5: Варіант 5
Студент: Рубцов Михаїл
Група: EIP30
"""

def f(x: float) -> float:
    return x ** 4 - 13 * x ** 2 + 36 - 1 / x

def phi(x: float) -> float:
    return f(x) + x

