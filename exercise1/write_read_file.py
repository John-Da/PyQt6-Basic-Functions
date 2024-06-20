

textFile = 'numbers.txt'



first_number = float(input("Enter a number: "))
second_number = float(input("Enter a number: "))


print(f"{first_number} + {second_number} = {first_number + second_number}")

with open("numbers.txt" ,'w') as numFile:
     print(f'{first_number} + {second_number} = {first_number+second_number}', file=numFile)
     print('Writing to file numbers.txt')


with open("numbers.txt" , "r" ) as numFile:
     data = numFile.read()
     print('Reading from file numbers.txt')
     print(data)




     