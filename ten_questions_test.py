class PythonQA:
    def __init__(self,
                 q_a: dict,
                 show_counter: bool = True):
        self.q_a = q_a

        self.show_counter = show_counter
        self.counter = 0

        self.start_test()

    @property
    def q_a(self):
        return self._q_a

    @q_a.setter
    def q_a(self, value: dict):
        if not isinstance(value, dict):
            raise ValueError(f"Value must be type of dict. {type(value)}: {value} was given")
        self._q_a = value

    def start_test(self):
        self.counter = 0
        questions_amount = len(self.q_a)
        try:
            for idx, (question, answer) in enumerate(self.q_a.items()):
                print("-"*10, f"Stage {idx}/{questions_amount}", "-"*10,)
                self._ask_user(question, answer)
        finally:
            # as user will always answer all questions (except for KeyboardInterrupt)
            input(f"\nCorrect answers: {self.counter}/{questions_amount}")

    def _ask_user(self, question, answer):
        while True:
            print(f"Question: {question}")
            user_answer = input(f"Your answer: ")

            if user_answer.strip().lower() == str(answer).lower().strip():
                print("Correct!\n")
                self.counter += 1
                break

            print("Incorrect answer :(\n")


if __name__ == '__main__':
    question_answer = {
        "How many conditional statements are available in Python 3?": 3,

        "How many loop statements are available in Python 3?": 2,

        "Method to format strings in Python 3\n(for example 'Hey, {0}!'.method)": "format",

        "What is the last stable version of Python (for 11th of September 2023)?": 3,

        "Python uses compiler or interpreter? (1; 2)?": 2,

        "Who is the creator of Python?": "Guido van Rossum",

        "Python package manager": "pip",

        "Official Python 3 website is https://.../ (for 11th of September 2023)":  "www.python.org",

        "When Python was created (year according to wiki)?": 1991,

        "What operator concatenates two strings in Python 3?": "+"
    }
    PythonQA(question_answer)
