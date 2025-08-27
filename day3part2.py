import re
with open('data3.txt', 'r') as file:
    all_text = file.read()
    
#pattern matched text mul, parenthesis (, group 1 = 1 or more digits
#literal comma, group2=one or more gitis, parentehsis )
all_matches = re.findall(r'(mul\((\d+),(\d+)\))|(don\'t\(\))|(do\(\))', all_text)
total=0
do=True
for match in all_matches:
    print(match)
    if match[0] and do:
        total += int(match[1]) * int(match[2])
    elif match[3]:
        do=False
    elif match[4]:
        do=True
print(total)
