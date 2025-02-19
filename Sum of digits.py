def sum_of_digits(num):
  sum = 0
  t = num

  while t > 0:
    sum += t % 10
    t //= 10

  return sum
