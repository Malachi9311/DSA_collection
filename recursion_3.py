#!/usr/bin/python3

def base10ToString(number):
    binary_string = []

    def str_maker(number):
        if number < 2:
            binary_string.append(number)
            return
        else:
            str_maker(int(number / 2))
            str_maker(number % 2)

    str_maker(number)
    return binary_string


# print(base10ToString(13))
arr = base10ToString(232)
for i in arr:
    print("{}".format(i), end="")
print()
