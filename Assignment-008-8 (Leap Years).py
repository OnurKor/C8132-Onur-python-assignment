leap = int(input("enter a leap year: "))
condition = (leap%400 == 0) or (leap % 4 == 0 and leap%100 != 0 )
if condition :
  print(leap, "is leap year")
else:
  print(leap, "is not leap year")
