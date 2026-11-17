"""
Filename: Factorial Calculator.py
Author: <Trejo Young, Brian>
Created: <11/17/2026>
Instructor: Burgess
"""

x=int(input("Enter a non-negative letter "))

total=1
print(f"{x}!=",end="")
for i in range(x,0,-1):
    total *=i
    print(f"{i}*",end="")
print("\ntotal is",total)