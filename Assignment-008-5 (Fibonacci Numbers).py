def fibonacci(num_min, num_max) :
  fibonacci = []
  a = num_min
  while a <= num_max :
    fibonacci.append(a)
    if len(fibonacci) < 2 :
      a += a
    else :
      a = fibonacci[-1] + fibonacci[-2]
  return fibonacci
print(fibonacci(1, 55))
