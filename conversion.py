weight=input("weight: ") 
unit=input("lb(s) or kg(s): ")
if unit.upper()=="L":
 converted=0.45*int(weight)
 print(converted, "kgs") 
else :
 converted=int(weight)/0.45
 print(converted, "lbs")
 
