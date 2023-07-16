
for fizzbuzz in range (1,101):
  if fizzbuzz%3==0 and fizzbuzz%5==0:
   print("fizzbuzz")
  elif fizzbuzz%5==0:
   print("buzz")
  elif fizzbuzz%3==0:
   print("fizz")
  else:
   print(fizzbuzz)
  