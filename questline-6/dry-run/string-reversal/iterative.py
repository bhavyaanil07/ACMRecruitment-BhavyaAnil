def reverse_iterative(s):
    char_list = list(s)
    for i in range(len(char_list) // 2):
        char_list[i], char_list[len(char_list) - 1 - i] = char_list[len(char_list) - 1 - i], char_list[i]
    return "".join(char_list)
my_string = input('enter a string')
reversed_string = reverse_iterative(my_string)
print(reversed_string) 