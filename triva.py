class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def display_question(self):
        print(self.question)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")
        print()

    def check_answer(self, selected_option):
        return selected_option == self.correct_answer


def run_trivia_game(questions):
    player_scores = [0, 0]

    for player in range(2):
        print(f"Player {player + 1}'s turn:")
        for question in questions:
            question.display_question()
            selected_option = 0
            while selected_option not in [1, 2, 3, 4]:
                try:
                    selected_option = int(input("Select your answer (1-4): "))
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 4.")

                if selected_option not in [1, 2, 3, 4]:
                    print("Invalid input. Please enter a number between 1 and 4.")

            if question.check_answer(selected_option):
                print("Correct! You earned a point.")
                player_scores[player] += 1
            else:
                print("Incorrect. The correct answer was option", question.correct_answer)

    print("\nGame Over!\nPlayer 1's score:", player_scores[0], "\nPlayer 2's score:", player_scores[1])

    if player_scores[0] > player_scores[1]:
        print("Player 1 wins!")
    elif player_scores[1] > player_scores[0]:
        print("Player 2 wins!")
    else:
        print("It's a tie!")


# Sample trivia questions
questions_data = [
    ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 3),
    ("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], 1),
    ("What is the largest mammal in the world?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], 2),
    ("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], 2),
    ("Which country is known as the Land of the Rising Sun?", ["China", "Japan", "South Korea", "Vietnam"], 2),
    ("What is the chemical symbol for gold?", ["Au", "Ag", "Fe", "Hg"], 1),
    ("In which year did the Titanic sink?", ["1905", "1912", "1920", "1931"], 2),
    ("What is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], 4),
    ("Who painted the Mona Lisa?", ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"], 2),
    ("What is the capital of Australia?", ["Sydney", "Melbourne", "Canberra", "Brisbane"], 3),
    # Add more questions here
]

# Create Question objects
trivia_questions = [Question(q, opts, ans) for q, opts, ans in questions_data]

# Run the trivia game
run_trivia_game(trivia_questions)
