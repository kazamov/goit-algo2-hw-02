from optimize_printing import test_printing_optimization
from rod_cutting_problem import rod_cutting_problem_tests

if __name__ == "__main__":
    print(f"Завдання 1. Оптимізація черги 3D-принтера в університетській лабораторії\n")
    test_printing_optimization()

    print(f"\nЗавдання 2. Оптимальне розрізання стрижня для максимального прибутку")
    rod_cutting_problem_tests()