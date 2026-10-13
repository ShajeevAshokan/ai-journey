import random

QUESTIONS = [
    {"question": "Which keyword defines a function?",
    "options": ["func", "def", "define", "lambda"], "answer": "def"},
    {"question": "What does len([1, 2, 3]) return?",
    "options": ["2", "3", "4", "1"], "answer": "3"},
    {"question": "Which type is immutable?",
    "options": ["list", "dict", "tuple", "set"], "answer": "tuple"},
    {"question": "What is 7 // 2?",
    "options": ["3.5", "3", "4", "1"], "answer": "3"},
    {"question": "What does input() always return?",
    "options": ["int", "float", "str", "bool"], "answer": "str"},
]

def ask(question):
    options = question["options"][:]       # copy, so shuffling doesn't change the original
    random.shuffle(options)
    print("\n" + question["question"])
    for number, option in enumerate(options, start=1):
        print(f"  {number}. {option}")
    while True:
        text = input("Your answer (number): ").strip()
        if text.isdigit() and 1 <= int(text) <= len(options):
            return options[int(text) - 1] == question["answer"]
        print(f"Enter a number from 1 to {len(options)}.")

def main():
    questions = QUESTIONS[:]
    random.shuffle(questions)
    score = 0
    for q in questions:
        if ask(q):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The answer was: {q['answer']}")
    percent = score / len(questions) * 100
    print(f"\nYou scored {score}/{len(questions)} ({percent:.0f}%).")


if __name__ == "__main__":
    main()