# solution 1
# import textwrap

# def wrap(string, max_width):
#     string = textwrap.wrap(string, max_width)
#     string = "\n".join(string)
#     return string

# if __name__ == '__main__':
#     string, max_width = input('Enter string: '), int(input('Enter max width: '))
#     result = wrap(string, max_width)
#     print(result)

# solution 2
import textwrap

string = input('Enter string: ')
width = int(input('Enter max width: '))

print(textwrap.fill(string, width))

# solution 3
import textwrap
string = input('Enter a string:')
