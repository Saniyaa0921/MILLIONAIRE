questions = [
    ["What is the capital of India?", "Mumbai", "New Delhi", "Kolkata", "Chennai", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["Which programming language is known for AI and Machine Learning?", "Python", "HTML", "CSS", "SQL", 1],
    ["Which keyword is used to define a function in Python?", "function", "define", "def", "fun", 3],
    ["Who is known as the Missile Man of India?", "C. V. Raman", "A. P. J. Abdul Kalam", "Homi Bhabha", "Vikram Sarabhai", 2]
]

prizes = [5000, 10000, 32000, 45000, 50000]

total = 0

for i, question in enumerate(questions):

    print("\n" + question[0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    ans = int(input("Enter your answer (1-4): "))

    if ans == question[5]:
        print(" Correct Answer!")
        total = prizes[i]
        print(f"You won ₹{prizes[i]}")
    else:
        print(" Wrong Answer!")
        print(f"The correct answer was option {question[5]}")
        print("Better luck next time!")
        break

print(f"\nYour total winning amount is ₹{total}")