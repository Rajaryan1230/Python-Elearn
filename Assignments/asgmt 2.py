a = 100
b = 2
c = 10
d = 3
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(c/d)
print(c%d)
print(c**d)


num1 = 50
num2 = 25
print(num1>num2)
print(num1<num2)
print(num1>=num2)
print(num1<=num2)
print(num1==num2)
print(num1!=num2)


x = True
y = False
print(x  and  y)
print(x  or  y)
print(not x)
print(not y)


list1 = [1,2,3]
list2 = [1,2,3]
print(list1 is list2)
print(list1 is not list2)


list3 = [4,5,6]
print(5 in list3)
print(3 not in list3)


str1 = 'Hello'
str2 = 'World'
print(str1 + ' ' + str2)
print(str1*5)


score = int(input('Enter your score from 0-100:'))
def calc_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 90:
        return 'B'
    elif 70 <= score <= 80:
        return 'C'
    elif 60 <= score <= 70:
        return 'D'
    elif 0 <= score <= 60:
        return 'F'
    else:
        return 'Invalid Score'
grade = calc_grade(score)
print('The grade for the score', score, 'is:', grade)


age = int(input('Enter your age:'))
def calc_age_category(age):
    if 60 <= age <= float('inf'):
        return 'Senior'
    elif 18 <= age <= 60:
        return 'Adult'
    elif 13 <= age <= 18:
        return 'Teen'
    elif 0 <= score <= 13:
        return 'Child'
    else:
        return 'Invalid Age Intered'
category = calc_age_category(age)
print('The age category for your age', age, 'is:', category)


age_vote = int(input('What is your age:'))
if age_vote >= 18:
    print('You are eligible to vote!')
else:
    print('You are NOT eligible to vote!')


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1, 2, 3, 4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
