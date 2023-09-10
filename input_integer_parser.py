print('Enter some numbers in one line')
raw_input = input()
split_input = raw_input.split()
parsed_input = list()
for raw in split_input:
    parsed_input.append(int(raw))
parsed_input.sort()
print(f'your result: {parsed_input}')
