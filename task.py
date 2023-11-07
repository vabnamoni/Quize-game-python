class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def play(self):
        for question in self.questions:
            print(question.question)
            for i, option in enumerate(question.options, start=1):
                print(f"{i}. {option}")
            user_choice = input("Enter the number of your answer: ")
            try:
                user_choice = int(user_choice)
                if 1 <= user_choice <= len(question.options):
                    if question.check_answer(user_choice):
                        print("Correct!\n")
                        self.score += 1
                    else:
                        print("Incorrect!\n")
                else:
                    print("Invalid choice. Please choose a valid option.\n")
            except ValueError:
                print("Invalid input. Please enter a number.\n")
        print(f"Quiz complete! Your score: {self.score}/{len(self.questions)}")

# Create quiz questions
questions = [
    Question("What does HTML stand for?", ["Hyper Text Markup Language", "Hyperlink and Text Markup Language", "Home Tool Markup Language", "Hyper Text Manipulation Language"], 1),
    Question("Which programming language is often used for web development?", ["Python", "Java", "HTML", "C++"], 3),
    Question("What does IDE stand for?", ["Integrated Development Environment", "Internet Development Environment", "Interface Design Environment", "Integrated Design Environment"], 1),
    Question("What is the result of 3 + 5?", ["7", "8", "9", "10"], 2),
    Question("What is a loop in programming?", ["A type of fruit", "A tool for cutting paper", "A repetitive sequence of instructions", "A type of dance"], 3),
    Question("Which symbol is used for comments in Python?", ["//", "/* ... */", "#", "--"], 3),
    Question("What is the file extension for a Python script?", [".pyt", ".script", ".pyscript", ".py"], 4),
    Question("Which data type is used to store a sequence of characters in Python?", ["integer", "string", "float", "list"], 2),
    Question("What is the purpose of a function in programming?", ["To create loops", "To display text on the screen", "To store data", "To perform a specific task"], 4),
    Question("What is the result of 2 * 3?", ["5", "6", "7", "8"], 2)
]

# Initialize the quiz game
quiz = QuizGame(questions)

# Start the quiz
quiz.play()