def get_input(file_name):
    with open(file_name, 'r') as input_file:
         return list(map(str, input_file.readlines()))

def part_1(input):
    horizontal = 0
    depth = 0
    for line in input: 
        command = line.split()
        if command[0] == "forward":
            horizontal += int(command[1])
        elif command[0] == "up":
            depth -= int(command[1])
        else:
            depth += int(command[1])
    print(horizontal * depth)
     

def part_2(input):
    horizontal = 0
    depth = 0
    aim = 0
    for line in input: 
        command = line.split()
        if command[0] == "forward":
            horizontal += int(command[1])
            depth += aim * int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])
        else:
            aim += int(command[1])
    print(horizontal * depth)

numbers = get_input('input02.txt')
#part_1(numbers)
part_2(numbers)