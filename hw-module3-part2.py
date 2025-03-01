from random import randint

def get_numbers_ticket(min, max, quantity):
    result_array = set()

    if min < 1 or max > 1000 or min > 1000 or max < 1 or min > max or max - min < quantity:
      return sorted(list(result_array))
    else:
        while len(result_array) != quantity:
            value = randint(min, max)
            result_array.add(value)

        return sorted(list(result_array))

print(f'"Ваші лотерейні числа:"{get_numbers_ticket(2,10,2)}')

