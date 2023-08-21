def shout(n):
    if n < 1:
        return
    print('SHOUT')
    shout(n-1)

print( shout(10000) )

