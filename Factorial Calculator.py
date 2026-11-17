"""
Filename: Factorial Calculator.py
Author: <Trejo Young, Brian>
Created: <11/17/2026>
Instructor: Burgess
"""


def factorial():
    # Write your code here
    x = int(input("Enter a non-negative letter "))
    if x == 0:
        print("0!=1")
    else: x
        total = 1
        print(f"{x}!=", end="")
        for i in range(x, 0, -1):
            total *= i
            print(f"{i}*", end="")
        print("\ntotal is", total)

# You should not need to change any code below this point
def main():
    print("This program computes factorials and displays their intermediate calculations.")
    running = "y"
    while running == "y":
        factorial()
        running = input("Do another calculation? (y/N)\n").lower()
    print("Thank you for using this factorial calculator!")

if __name__ == "__main__":
    main()