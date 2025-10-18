entered_sentence = input()

output = ''.join(['Yes' if entered_sentence == 'yes' or entered_sentence =='YES' or entered_sentence =='Yes' else 'No' ])
print(str(output))