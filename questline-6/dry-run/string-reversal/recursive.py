def reverse_recursive(s):
    if len(s) == 0 or len(s) == 1:
        return s
    else:
        return reverse_recursive(s[1:]) + s[0]
my_string = input('enter string')
reversed_string = reverse_recursive(my_string)
print(reversed_string) 