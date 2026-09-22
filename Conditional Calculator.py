"""
Filename: conditional Calcualator.py
Author: <Trejo Young, Brian>
Created: <09/22/2026>
Instructor: Burgess
"""

print("This will be a Conditional Calculator for coding")
q1 = int(input("put in your first number "))
op = input("put in your operation (+,-,*,/) ")
q2 = int(input("put in your second number "))

if op == "+":
    print(f"{q1} + {q2} = {q1 + q2}")
elif op == "-":
    print(f"{q1} - {q2} = {q1 - q2}")
elif op == "*":
    print(f"{q1} * {q2} = {q1 * q2}")
elif op == "/":
    print(f"{q1} / {q2} = {q1 / q2}")

