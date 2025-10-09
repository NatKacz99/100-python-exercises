from pprint import pprint
sentence = input("Enter your sentence: ").split()

pprint({i:sentence.count(i) for i in sentence})
