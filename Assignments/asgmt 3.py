for i in range (1,11):
    print(i)


i = 2
while i <= 20:
    print(i)
    i=i+2


N = 10
sum = 0
for i in range(1, N + 1):
    sum=sum+i
print("Sum:", sum)


number = 12345
sum_of_digits = 0
while number > 0:
    digit = number % 10
    sum_of_digits=sum_of_digits+digit
    number=number//10
print("Sum of digits:", sum_of_digits)


num = 5
i = 1
while i <= 10:
    print(num, 'x', i, '=', num * i)
    i=i+1


input_string = "hello"
reversed_string = ""
for char in input_string:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)
