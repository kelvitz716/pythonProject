students = (("squidward","F","60"),
            ("sandy","A","33"),
            ("patrick","D","36"),
            ("spongebob","B","20"),
            ("Mr. krabs","C","78"))

age = lambda age:age[2]
#students.sort(key=age,reverse=True) #this sorts a tuple inside a list
sorted_students = sorted(students, key=age,reverse=True)    #this sorts a tuple inside an tuple
for i in sorted_students:
    print(i)




