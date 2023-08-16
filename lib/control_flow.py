#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

print(admin_login("sudo", "12345"))
print(admin_login("admin", "12345"))
print(admin_login("ADMIN", "12345"))

def hows_the_weather(temperature):
    # your code here
        if temperature < 40:
         return "It's brisk out there!"
        elif 40 <= temperature <= 65:
            return "It's a little chilly out there!"
        elif temperature > 85:
            return "It's too dang hot out there!"
        else:
            return "It's perfect out there!"
    
print(hows_the_weather(33))
print(hows_the_weather(99))
print(hows_the_weather(55))
print(hows_the_weather(75))

def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5== 0:
        return "FizzBuzz"
    elif num % 3==0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

print(fizzbuzz(0))
print(fizzbuzz(33))
print(fizzbuzz(50))

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero!"
    else:
        print("Invalid operation!")
        return None

print(calculator("+", 1, 1))
print(calculator("-", 3, 1))
print(calculator("*", 3, 2))
print(calculator("/", 4, 2))
print(calculator("nope", 4, 2))

