class Animal:
    def wild():
        print("wild animals are very dangerous")
    def domestic():
        print ("domestic animals are calm")


#calling function with a class        
Animal.wild()
Animal.domestic()

#creating objects of class
An1=Animal()
An1.domestic="cow"
An1.wild="elephant"
print(An1.wild)

