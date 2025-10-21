def calculate(n):
    print(round(sum(map(lambda x: x/(x+1), range(1, n+1))), 2))

calculate(5)