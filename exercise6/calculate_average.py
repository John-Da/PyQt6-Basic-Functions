def calculate_average(*numbers, round_to=2):
    number = len(numbers)
    if number == 0:
        return 0
    else:
        avg = sum(numbers) / len(numbers)
        answer = round(avg, round_to) 
        return answer




print(calculate_average(100, 120, 130))
print(calculate_average(10.5, 20.5, 30.5, round_to=1))
print(calculate_average())