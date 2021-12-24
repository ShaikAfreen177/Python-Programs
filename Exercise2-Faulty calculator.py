"""
Python Exercise 2: Faulty Calculator Solution
In Exercise-2, we need to create a faulty calculator.
I am going to present the scenario and details related to the exercise here too.

Scenario:
Suppose that you are an invigilator in an exam. A calculator is not allowed for the exam. You discover somehow that
students are planning to cheat in exams, using a calculator program in Python language. Somehow you get your hands on
the calculator program and now you want to alter few results in the calculator with your own provided results, so you
can catch the students who are trying to cheat using the calculator program.

The user will provide the following inputs:

Operator
The two numbers, between which the operator is applied
All the results will be correct, except for these few:

45 * 3 = 555
56+9 = 77
56/6 = 4
"""

print("Enter 1st Number")
num1 = int(input())
print('Enter 2nd Number')
num2 = int(input())
print('so What you Want?'+'+,-,/,%,*')
num3 =input()

if num1 ==45 and num2==3 and num3=='*':
    print("555")
elif num1 == 56 and num2 == 9 and num3 == '+':
        print("77")
elif num1 == 56 and num2 == 6 and num3 == '/':
        print("4")
elif num3=='*' :
    num4=num1*num2
    print(num4)
elif num3 == '+':
    plus=num2+num1
    print(plus)
elif num3 == '/':
    Dev=num2/num1
    print(Dev)
elif num3 == '-':
    Dev=num2-num1
    print(Dev)
elif num3 == '%':
    percent=num2%num1
    print(percent)
else:
    print("Error! Please check your input")