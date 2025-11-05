def countChickensAndRabbits(numberHeads, numberLegs):
    no_solution ='No solutions!'
    for i in range(numberHeads+1):
        j = numberHeads - i
        if 2 * i + 4 * j==numberLegs:
            return i, j
    return no_solution

numberHeads = 35
numberLegs = 94
solutions=countChickensAndRabbits(numberHeads, numberLegs)
print(solutions)