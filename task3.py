
c = input('Enter the string: ')
probel = c.count(' ')
num = [c.count(x) for x in c if x in '0123456789']
prep = [c.count(x) for x in c if x in ".,:!@?-"]
print(f'Letters: {len(c)-probel-len(num)-len(prep)}')
print(f'Spaces: {probel}')
print(f'Numbers:{len(num)}')
print(f'Punctuation marks {len(prep)}')
