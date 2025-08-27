import re
with open('data7.txt','r') as file:
    #All sequences of 1 more numbers
    equations = [list(map(int, re.findall(r'\d+', l))) for l in file]
    res=0
    
    def recurse(goal, eq):
        if len(eq)<2:
            return goal==eq[0]
        
        #try 2 paths - add or multiply
        firstElement=eq[0]
        add=eq[1:]
        add[0]+=firstElement
        
        multiply=eq[1:]
        multiply[0]*=firstElement
        
        concat = eq[1:]
        concat[0] = int(str(firstElement) + str(concat[0]))
        return recurse(goal, add) or recurse(goal, multiply) or recurse(goal, concat)
        
    #try 
    for equation in equations:
        goal = equation[0]
        if recurse(goal,equation[1:]):
            res+=goal
    print(res)
    