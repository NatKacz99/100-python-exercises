# solution 1:
def printValue(wordFirst, wordSecond):
    length1 = len(wordFirst)
    length2 = len(wordSecond)
    if length1 > length2:
        print(wordFirst)
    elif length1 < length2:
        print(wordSecond)
    else:
        print(wordFirst)
        print(wordSecond)

wordFirst, wordSecond = input().split()
printValue(wordFirst, wordSecond)

# solution 2:
def func(word1, word2): return print(max((word1, word2), key=len)) if len(
    word1) != len(word2) else print(word1 + '\n' + word2)
