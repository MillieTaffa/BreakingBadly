"""
BreakItTillYouMakeIt - Text & Math Utility Functions
Author: Your Name
Instructions: Implement each function below according to the docstrings.
Then write unit tests to verify correctness.
"""

def count_words(text: str) -> dict:
    text = text.lower()
    words = text.split
    word_count = {}

    for word in words:
        word = word.strip('.,!?":;()')
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1
    return word_count


def pascals_triangle_row(n: int) -> list[int]:
    row = [1]
    for i in range(1,n +1):
        next_value = row[i -1] * (n-i+1) // i
        row.append(next_value)


def calculator(a: float, b: float, op: str) -> float:
    if op == "+":
        return a + b
    elif op == "-":
        return a-b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ValueError("No divide by zero!")
        return a/b
    else:
        raise ValueError(f"Invalid op '{op}'")


def reverse_words(text: str) -> str:
    words = text.split()
    reversed_word = words[::-1]
    return " ".join(reversed_word)


def factorial(n: int) -> int:
    if n <0:
        raise ValueError("Factorials is not defined")
    result = 1
    for i in range(2,n+1):
        result *=i
    return result


if __name__ == "__main__":
    print("BreakItTillYouMakeIt functions loaded. Run your tests to verify.")
