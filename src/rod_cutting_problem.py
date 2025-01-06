from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через мемоізацію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
    
    memo = {}

    def recurse(n):
        if n == 0:
            return 0, []
        if n in memo:
            return memo[n]
        max_val = float('-inf')
        best_combo = []
        for i in range(1, n + 1):
            val, combo = recurse(n - i)
            candidate = prices[i - 1] + val
            if candidate > max_val:
                max_val = candidate
                best_combo = [i] + combo
        memo[n] = (max_val, best_combo)
        return memo[n]

    max_profit, combo = recurse(length)
    return {
        "max_profit": max_profit,
        "cuts": combo,
        "number_of_cuts": len(combo) - 1 if combo else 0
    }

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через табуляцію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
    
    dp = [0] * (length + 1)
    cut_tracker = [[] for _ in range(length + 1)]

    for i in range(1, length + 1):
        max_val = float('-inf')
        best_combo = []
        for j in range(1, i + 1):
            candidate = prices[j - 1] + dp[i - j]
            if candidate > max_val:
                max_val = candidate
                best_combo = [j] + cut_tracker[i - j]
        dp[i] = max_val
        cut_tracker[i] = best_combo

    return {
        "max_profit": dp[length],
        "cuts": cut_tracker[length],
        "number_of_cuts": len(cut_tracker[length]) - 1 if cut_tracker[length] else 0
    }

def rod_cutting_problem_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        # Тест 1: Базовий випадок
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        # Тест 2: Оптимально не різати
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        # Тест 3: Всі розрізи по 1
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # Тестуємо табуляцію
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\nПеревірка пройшла успішно!")

if __name__ == "__main__":
    rod_cutting_problem_tests()
