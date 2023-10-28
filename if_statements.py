name=input("please enter your name ")
if len(name)<3:
    print("name must be at least 3 characters")
elif len(name)>50:
    print("name can be maximum of 50 long")
else:
    print("name looks good!")    
    #eg 2
    weight=input("weight: ") 
unit=input("lb(s) or kg(s): ")
if unit.upper()=="L":
 converted=0.45*int(weight)
 print(converted, "kgs") 
else :
 converted=int(weight)/0.45
 print(converted, "lbs")