import random


def random_integer(min_value, max_value):
    """
    Generates a random integer between min_value and max_value.
    
    Parameters:
    min_value (int): The minimum value for the random number.
    max_value (int): The maximum value for the random number.
    
    Returns:
    int: A random integer within the given range.
    """
    return random.randint(min_value, max_value)


def random_operator():
    """
    Randomly selects one of the three basic arithmetic operators: +, -, or *.
    
    Returns:
    str: A randomly chosen operator.
    """
    return random.choice(['+', '-', '*'])


def result(n1, n2, operator):
    """
    Calculates the result of a math operation based on two numbers and an operator.
    
    Parameters:
    n1 (int): The first number.
    n2 (int): The second number.
    operator (str): The operator for the operation, either '+', '-', or '*'.
    
    Returns:
    tuple: A tuple containing the problem string and the result of the operation.
    """
    problem = f"{n1} {operator} {n2}"
    if operator == '+':
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2
    else:  # multiplication operator '*'
        result = n1 * n2
    return problem, result

def math_quiz():
    # Variable to store the player's score.
    score = 0
    # Total number of questions in the quiz.
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
         # Generate random numbers and an operator.
        n1 = random_integer(1, 10)
        n2 = random_integer(1, 5)
        operator = random_operator()

        # Calculate the problem and answer.
        PROBLEM, CORRECT_ANSWER =result(n1, n2, operator)
        print(f"\nQuestion: {PROBLEM}")

        # user's answer with error handling.
        while True:# 无限循环，直到用户输入有效的整数
            try:
                user_answer = int(input("Your answer: "))   # 尝试将用户的输入转换为整数
                break  # 如果输入有效，则退出循环
            except ValueError:# 如果发生 ValueError，说明输入无法转换为整数
                print("Error. Please enter a valid integer.")
                
        # Check the user's answer.
        if useranswer == CORRECT_ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {CORRECT_ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
