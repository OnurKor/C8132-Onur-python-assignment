age = input("Are you a cigarette addict older than 75 years old? (Only Yes or No) ").title().strip()
chronic = input("Do you have a severe chronic disease? (Only Yes or No) ").title().strip()
immune = input("Is your immune system too weak? (Only Yes or No) ").title().strip()
risk = (age == "Yes") or (chronic == "Yes") or (immune == "Yes")

if risk:
  print("You are in risky group")
else :
  print( "You are not in risky group")
