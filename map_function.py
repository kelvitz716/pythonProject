store = [("shirt",20),
         ("short",30),
         ("trouser",40),
         ("socks",5)]

data = lambda data:(data[0],data[1]*140)
to_dollars = map(data,store)

for i in to_dollars:
    print(i)

