def get_input(file_name):
    with open(file_name, 'r') as input_file:
        return list(map(int, input_file.readlines()))

def part_1(numbers):
    counter = 0
    last = float("inf")
    for x in range(0, len(numbers)):
        if numbers[x] > last:
            counter = counter + 1
        last = numbers[x]
    print(counter)

def part_2(numbers):
    n = 3
    counter = 0
    last = float("inf")
    for i in range(len(numbers)-n+1):
        value = sum(numbers[i:i+n])
        if value > last:
            counter = counter + 1
        last = value
    print(counter)

numbers = get_input('input01.txt')
part_1(numbers)
part_2(numbers)