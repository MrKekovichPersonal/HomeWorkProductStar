def sum_from_user_input(amount_of_numbers: int) -> int:
    """
    Calculates the sum of a given amount of numbers provided by the user.

    Args:
        amount_of_numbers (int): The number of numbers the user will input.

    Returns:
        int: The sum of the user input numbers.
    """

    if amount_of_numbers <= 0:
        raise ValueError(f"Incorrect input: {amount_of_numbers}. Must be greater than 0.")

    while True:
        try:
            user_input_numbers = [int(input(f"Enter {i + 1} number (integer): "))
                                  for i in range(amount_of_numbers)]

            return sum(user_input_numbers)
        except ValueError:
            print(f"Incorrect input.")


if __name__ == "__main__":
    NUMBER_OF_USER_INPUT = 4  # the amount of numbers we want user to enter
    print(sum_from_user_input(NUMBER_OF_USER_INPUT))