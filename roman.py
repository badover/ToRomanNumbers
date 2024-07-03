def int_to_roman(num):
    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''

    for i in range(len(value)):
        while num >= value[i]:
            roman_num += symbol[i]
            num -= value[i]
    return roman_num

print(int_to_roman(int(input('Your num: '))))
