students = [("squidward","F","60"),
            ("sandy","A","33"),
            ("patrick","D","36"),
            ("spongebob","B","20"),
            ("Mr. krabs","C","78")]

age = lambda age:age[2]
students.sort(key=age,reverse=True)
for i in students:
    print(i)




