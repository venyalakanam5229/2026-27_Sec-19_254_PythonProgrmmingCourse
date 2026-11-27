  def sum_values(*args):
    total = 0
    for value in args:
        total += value
    return total
print(sum_values(11, 22, 33))
print(sum_values(144, 120, 113, 441))
