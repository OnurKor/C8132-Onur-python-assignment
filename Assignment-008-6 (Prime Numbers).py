def prime(lim) :
  a = False
  prime = []
  for i in range(2, lim+1) :
    for j in range(2, i) :
      if i%j == 0 :
        a = False
        break
      else :
        a = True
    if a or i == 2 :
      prime.append(i)
  return prime
limit = int(input("Please enter a number: "))
print(prime(limit))
