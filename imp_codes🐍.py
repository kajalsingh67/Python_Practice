# 💙 Important Python 🐍 Practice Questions.......
# 1	Hello World 
# 2	Input/Output Program  
# 3	Add Two Numbers 
# 4	Subtract Two Numbers 
# 5	Multiply Two Numbers 
# 6	Divide Two Numbers 
# 7	Average of 3 Numbers 
# 8	Area of Circle 
# 9	Area of Rectangle 
# 10 Simple Interest 
# 11 Odd or Even 
# 12 Positive, Negative or Zero
# 13 Largest of Two Numbers
# 14 Largest of Three Numbers 
# 15 Swap Two Numbers 
# 16 Factorial 
# 17 Prime Number 
# 18 Fibonacci Series 
# 19 Multiplication Table 
# 20 Sum of Natural Numbers 
# 21 Reverse Number 
# 22 Palindrome Number
# 23 Armstrong Number
# 24 Count Digits 
# 25 Sum of Digits 
# 26 Leap Year 
# 27 HCF (GCD)
# 28 Power of Number 
# 29 Even & Odd Numbers from 1 to N 
# 30 Alphabet or Digit 

# Q. No. 1
print("Hello World")


# Q. No. 2
a = input("Enter your name: ")
print("Hello", a)


# Q. No. 3
a = 10
b = 20
print("Sum of two numbers:", a + b)


# Q. No. 4
a = 300
b = 25
print("Subtract two numbers:", a - b)


# Q. No. 5
a = 5
b = 20
print("Multiply two numbers:", a * b)


# Q. No. 6
a = 5
b = 20
print("Divide two numbers:", a / b)


# Q. No. 7
a = 7
b = 8
c = 5
total = a + b + c
average = total / 3
print("Average of 3 numbers:", average)


# Q. No. 8
radius = 5
area = 3.14 * radius * radius
print("Area of circle:", area)


# Q. No. 9
length = 8
breadth = 12
area = length * breadth
print("area of rectangle:", area)


# Q. No. 10
P = 500
R = 8
T = 1
interest = (P * R * T) / 100
print("Simple interest:", interest)


# Q. No. 11
a = int(input("Enter your number: "))
if a % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q. No. 12
a = int(input("Enter your number: "))
if a > 0:
    print("Positive number")
elif a < 0:
    print("Negative number")
else:
    print("Zero")


# Q. No. 13
a = int(input("Enter your number: "))
b = int(input("Enter your number: "))

if a >= b:
    print("A is the largest number")
else:
    print("B is the largest number")


# Q. No. 14
a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))

if a >= b and a >= c:
    print("A is the largest number")
elif b >= a and b >= c:
    print("B is the largest number")
else:
    print("C is the largest number")


# Q. No. 15
a = 10
b = 90

a, b = b, a
print(a, b)

# Q. No. 16 - Factorial
# Using for loop.....................
a = 5
fact = 1

for i in range(1, a + 1):
    fact = fact * i

print(fact)


# OR

# Using while loop
a = 4
i = 1
fact = 1

while i <= a:
    fact = fact * i
    i += 1

print(fact)


# Q. No. 17 - Prime Number
a = int(input("Enter your number: "))
count = 0

for i in range(1, a + 1):
    if a % i == 0:
        count = count + 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")


# Q. No. 18 - Fibonacci Series
x = 10
a = 0
b = 1

for i in range(x):
    print(a)
    c = a + b
    a = b
    b = c


# Q. No. 19 - Multiplication Table
a = int(input("Enter your number: "))

for i in range(1, 11):
    print(a, "x", i, "=", a * i)


# Q. No. 20 - Sum of Natural Numbers
a = 5
total = 0

for i in range(1, a + 1):
    total += i

print(total)

# 21. Reverse Number
n = 12345
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse Number:", reverse)


# 22. Palindrome Number
n = 129
original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


# 23. Armstrong Number
n = 153
original = n
total = 0

while n > 0:
    digit = n % 10
    total = total + (digit * digit * digit)
    n = n // 10

if original == total:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


# 24. Count Digits
n = 12345
count = 0

while n > 0:
    digit = n % 10
    count = count + 1
    n = n // 10

print("Number of Digits:", count)


# 25. Sum of Digits
n = 12345
total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print("Sum of Digits:", total)


# 26. Leap Year
year = 2026

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# 27. HCF (GCD)
a = 12
b = 18

while b != 0:
    a, b = b, a % b

print("HCF (GCD):", a)


# 28. Power of Number
a = 2
b = 5

power = a ** b

print("Power:", power)


# 29. Even & Odd Numbers from 1 to N
n = 10

print("Even Numbers:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)

print("Odd Numbers:")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)


# 30. Alphabet or Digit
a = input("Enter a character: ")

if a.isalpha():
    print("Alphabet")
elif a.isdigit():
    print("Digit")
else:
    print("Special Character")


