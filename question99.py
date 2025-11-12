if __name__ == '__main__':
    n = int(input())
    set1 = set(map(int,input().split()))

    m = int(input())
    set2 = set(map(int, input().split()))

    answer = list(set1 ^ set2)
    answer.sort()
    for i in answer:
        print(i)