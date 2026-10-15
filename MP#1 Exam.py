"""

<Trejo Young, Brian>
MP#1 Exam
"""

z = int(input("Tell me your current score."))

if z >= 90 and z <= 100:
    print("your score is Grade A")
    print("Great work there!")
elif z >= 80 and z <= 89:
    print("Your score is Grade B")
    print("Great work there!")
elif z >= 70 and z <= 79:
    print("Your score is Grade C")
    print("Keep on practicing!")
elif z >= 60 and z <= 69:
    print("Your score is Grade D")
    print("Keep on practicing!")
elif z <= 59:
    print("Your score is Grade F")
    print("Keep on practicing!")