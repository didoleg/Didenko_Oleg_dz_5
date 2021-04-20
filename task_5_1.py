def odd_nums(val):
    number = 1
    while number < val + 1:
        if number % 2 != 0:
            yield number
        number += 1


odd_to_15 = odd_nums(15)
print(type(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
