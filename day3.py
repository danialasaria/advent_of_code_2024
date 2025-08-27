import re
with open('data3.txt', 'r') as file:
    all_text = file.read()
    
#pattern matched text mul, parenthesis (, group 1 = 1 or more digits
#literal comma, group2=one or more gitis, parentehsis )
all_matches = re.findall(r'mul\((\d+),(\d+)\)', all_text)
total=0
for match in all_matches:
    n1,n2 = match
    total+=int(n1)*int(n2)
print(total)