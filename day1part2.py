with open("data1.txt", 'r') as file:
    first_column, second_column = [],[]
    for line in file:
        line = line.split()
        first_column.append(int(line[0]))
        second_column.append(int(line[1]))
    similarity_score = 0
    for e in first_column:
        similarity_score += e * second_column.count(e)
    print(similarity_score)