vetor = ['w','e',0,'h',3,'x', 'g', 10]

def get_numbers(num):

    numbers = []

    for number in num:
        if type(number) != int:
         numbers.append(number)
    return numbers

def get_string(strs):

    strings = []

    for string in strs:
        if type(string) != str:
         strings.append(string)
    return strings

print(vetor)
print(get_numbers(vetor))
print(get_string(vetor))


   