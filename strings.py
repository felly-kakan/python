#'''ttttttt'''-----tripple quotes is used for multiple lines
g='''you going to school
my name is felly
im 40 yrs of age'''
print(g)

course='python for "Beginners"'
#prints character at position 0(p)
print(course[0])
#prints character at position 0 to 3 but it excludes 3(pyt)
print(course[0:3])

#prints all the characters(python for "Beginners")
print(course[0:])
#prints all the characters from psn 1(ython for "Beginners")
print(course[1:])

#formated strings use (f)(eg. print ="john [smith ] is a coder")
fname="john"
lname="smith"
msg=f'{fname} [{lname}] is a coder'
print(msg)
#IN OPERATORS returns whether s true or not
print('python' in course)
print('man' in course)
course.upper