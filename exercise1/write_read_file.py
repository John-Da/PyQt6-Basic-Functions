number1 = float(input("Enter a number: "))
number2 = float(input("Enter a number: "))

print(f"{number1} + {number2} = {number1 + number2}")


with open("numbers.txt" ,'w') as numb:
     print(f'{number1} + {number2} = {number1+number2}', file=numb)
     print('Writing to numbers.txt')

with open("numbers.txt" , "r" ) as readFile:
     reading = readFile.read()
     print('Reading from numbers.txt')
     print(reading)