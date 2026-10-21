def my_function():
    """Print a basic hello message."""
    print("Hello from my_function!")


def calculate_economic_intuition(weeks_completed: int) -> str:
    """Calculate economic intuition level based on completed D100 study weeks."""
    intuition_level = weeks_completed * 10
    return f"Week {weeks_completed} in D100: Economic intuition loaded at {intuition_level}%. Becoming a real Data Scientist!"


def backtest_strategy(prices: list[float], signals: list[int]) -> float:
    capital = 1.0
    for i in range(1, len(prices)):
        daily_return = prices[i] / prices[i - 1] - 1
        capital *= 1 + signals[i - 1] * daily_return
    return capital - 1


if __name__ == "__main__":
    my_function()
    print(calculate_economic_intuition(weeks_completed=1))
    print(backtest_strategy([100, 102, 101, 105], [1, 0, 1, 0]))
