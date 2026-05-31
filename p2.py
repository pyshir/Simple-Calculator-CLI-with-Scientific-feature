"""
2. Simple Calculator CLI
Concepts: functions, loops, error handling

Features:
+ - * / % - done
invalid input handle - done
loop দিয়ে multiple calculation - done
history save - done

Extra:
scientific mode calculation add করো
Square root → √25 = 5
Power → 2^3 = 8
Sin/Cos/Tan
"""
import inflect
import math
# inflect module has been used for (1st, 2nd, 3rd ordinal but not necessary in operation)
p = inflect.engine()

# Function to save history
def history_save(x):
    with open('history.txt', 'a') as f:
        f.write(f'{x}\n')

mod = input('1.Normal\n2.Scientific')

#Normal Mode
if mod == '1':
    operation = input('1.Addition\n2.Subtraction\n3.Multiplication\n4.Dividation\n5.Modulus\nWhat do you want to do?\n')

    # Addition (used a module inflect)
    if operation == '1':
        history_save("Addition")
        numbers = int(input('how many numbers do you want to add (1 to infinity)\n'))
        if numbers == 0:
            x = "Invalid input"
            print(x)
            history_save(x)
        else:
            total = 0
            for i in range(numbers):
                num_input = int(input(f'Enter {p.ordinal(i+1)}  number\n'))
                total += num_input
            print(f'Total is, {total}')
            history_save(total)

    # Substraction
    if operation == '2':
        history_save("substraction")
        num1 = int(input('Enter 1st number (2nd - 1st)\n'))
        num2 = int(input('Enter 2nd number (2nd - 1st)\n'))
        substraction = num2 - num1
        print(f'Answer is, {substraction}')
        history_save(substraction)

    # Multiplication
    if operation == '3':
        history_save("multiplication")
        numbers = int(input('how many numbers do you want to multiply (1 to infinity)\n'))
        if numbers >= 1:
            total = 1
            for i in range(numbers):
                num = int(input(f'Enter {p.ordinal(i+1)} number'))
                total *= num
            print(f'Answer is, {total}')
            history_save(total)
        else:
            print('Invalid input')
            history_save('Invalid input')

    # Division
    if operation == '4':
        history_save("division")
        num1 = int(input('Enter 1st number (1st will divided by 2nd)\n'))
        num2 = int(input('Enter 2nd number (1st will divided by 2nd)\n'))
        answer = round((num1 / num2), 2)
        print(f'Answer is, {answer}')
        history_save(answer)

    # Modulus
    if operation == '5':
        history_save("Modulus")
        num1 = int(input('Enter 1st number (1st will divided by 2nd)\n'))
        num2 = int(input('Enter 2nd number (1st will divided by 2nd)\n'))
        modulus = num1 % num2
        print(f'Answer is, {modulus}')
        history_save(modulus)

#Scientific Mode
elif mod == '2':
    operation = input('1.Squr Root\n2.Power\n3.SIN\n4.COS\n5.TAN\nWhat do you want to do?\n')
    if operation == '1':
        num = int(input('Enter a number \n'))
        sqr_root = num**0.5
        print(f'Answer is, {sqr_root}')
        history_save(f'{num}^0.5 = {sqr_root}')
    elif operation == '2':
        num1 = int(input('Enter a number\n'))
        num2 = int(input('Enter power\n'))
        power = num1**num2
        print(f'Answer is, {power}')
        history_save(f'{num1}^{num2} = {power}')
    elif mod == '3':
        num = int(input('Enter Angle in Degree \n'))
        total = math.sin(math.radians(num))
        print(f'Answer is, {total}')
        history_save(f'Sin{num}° = {total}')
    elif mod == '4':
        num = int(input('Enter Angle in Degree \n'))
        total = math.cos(math.radians(num))
        print(f'Answer is, {total}')
        history_save(f'Cos{num}° = {total}')
    elif mod == '5':
        num = int(input('Enter Angle in Degree \n'))
        total = math.tan(math.radians(num))
        print(f'Answer is, {total}')
        history_save(f'Tan{num}° = {total}')

