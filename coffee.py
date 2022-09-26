print("A.coffee      RS:10")
print("B.cold coffee RS:30")
print("C.Tea         Rs:50")
print("D.Milk shake  RS:70")

coffee=10
coldcoffee=30
Tea=50
Milkshake=70

G=input("Enter the drink you want:")
H=int(input("No of drink's:"))
if G =="coffee" or "cold offee" or "Tea" or "Milk shake":
  print(G)
  if G=="coffee":
     output=coffee*H
     print("Your bill amount is:",output)
  elif G=="cold coffee":
    output=coldcoffee*H
    print("Your bill amount is:", output)
  elif G=="Tea":
    output=Tea*H
    print("Your bill amount is:", output)
  elif G=="Milk shake":
    output=Milkshake*H
    print("Your bill amount is:", output)
  else:
    print("Enter the valid no:")