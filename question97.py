def alphabetRangoli(n):
    lst = list(map(chr, range(97, 123)))
    x = lst[n - 1::-1] + lst[1:n]
    middle = len('-'.join(x))
    for i in range(1, n):
        print('-'.join(lst[n - 1:n-1:-1] + lst[n - i:n]).center(middle, '-'))
    for i in range(n, 0, -1):
        print('-'.join(lst[n - 1:n - i:-1] + lst[n - i:n]).center(middle, '-'))

alphabetRangoli(3)