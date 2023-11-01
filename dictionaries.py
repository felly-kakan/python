#declared using {}
student= {
    "name":"felly kakan",
    "reg_no":123,
    "is_verified":True
}
#update the dictionary
student["age"]=20
print(student.get("name"))
print(student.get("reg_no"))
print(student.get("age"))


phone=input("phone:")
dgit_mapping={
"1" : "one",
"2" :"two",
"3" : "three",
"4" : "four",
"5" : "five",
"6" : "six",
"7" : "seven",
"8" : "eight",
"9" : "nine"
}
output=""
for k in phone:
 output+=  dgit_mapping.get(k,"") +  (" ")

print(output)






