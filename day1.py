with open('data1.txt', 'r') as file:
    first_column, second_column = [],[]
    for line in file:
        line = line.split()
        first_column.append(int(line[0]))
        second_column.append(int(line[1]))
    total_difference = 0
    for _ in range(1000):
        first_min = min(first_column)
        second_min = min(second_column)
        first_column.remove(first_min)
        second_column.remove(second_min)
        total_difference+=abs(first_min-second_min)
        
    print(total_difference)